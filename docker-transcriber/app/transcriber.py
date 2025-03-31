import os
import time
import torch
import whisper
import argparse
import subprocess
from pyannote.audio.pipelines import SpeakerDiarization


# Load Models
def load_models(model_size="medium", hf_token=None):
    """Loads Whisper and Pyannote models."""
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load Whisper
    print("Loading Whisper model...")
    whisper_model = whisper.load_model(model_size)

    # Load Pyannote (Speaker Diarization)
    print("Loading Pyannote model...")
    diarization_model = SpeakerDiarization.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token
    ).to(torch.device(device))

    return whisper_model, diarization_model


# Extract Audio from MP4
def extract_audio(mp4_file, wav_file):
    """Extracts audio from an MP4 file as a WAV format for transcription."""
    print(f"Extracting audio from {mp4_file}...")
    command = ["ffmpeg", "-i", mp4_file, "-ac", "1", "-ar", "16000", "-vn", wav_file, "-y"]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(wav_file):
        print(f"Error: Audio extraction failed for {mp4_file}")
        return None

    return wav_file


# Extract Speaker Diarization
def apply_diarization(audio_file, diarization_model):
    """Performs speaker diarization and returns speaker segments."""
    diarization_result = diarization_model(audio_file)

    speaker_segments = []
    speaker_map = {}
    speaker_counter = 1

    for turn, _, speaker in diarization_result.itertracks(yield_label=True):
        if speaker not in speaker_map:
            speaker_map[speaker] = f"SPEAKER_{speaker_counter}"
            speaker_counter += 1
        speaker_segments.append((turn.start, turn.end, speaker_map[speaker]))

    return speaker_segments


# Transcribe Using Whisper
def transcribe_audio(audio_file, model, language="en"):
    """Transcribes the entire audio file using Whisper."""
    print("Transcribing with Whisper...")
    result = model.transcribe(audio_file, language=language)
    return result["segments"]


# Match Transcription with Speakers
def match_speakers(transcription, speaker_segments):
    """Aligns Whisper's transcription with speaker segments."""
    conversation = []
    for start, end, speaker in speaker_segments:
        text = " ".join([seg["text"] for seg in transcription if start <= seg["start"] <= end])
        if text.strip():
            conversation.append(f"[{speaker}] {text}")

    return conversation


# Process a Single Audio File
def process_audio(wav_file, output_file, model_size, language, hf_token):
    whisper_model, diarization_model = load_models(model_size, hf_token)

    # Apply speaker diarization
    speaker_segments = apply_diarization(wav_file, diarization_model)

    # Transcribe audio
    transcription = transcribe_audio(wav_file, whisper_model, language)

    # Match transcription with speaker labels
    conversation = match_speakers(transcription, speaker_segments)

    # Save output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(conversation))

    print(f"Conversation saved to {output_file}")


# Process MP4 File (Fix)
def process_file(file, input_folder, output_folder, model_size, language, hf_token):
    """Processes a single MP4 file: extracts audio, applies diarization, and transcribes."""
    print(f"Processing file: {file}")

    mp4_file = os.path.join(input_folder, file)
    audio_file = os.path.join(output_folder, f"{file}.wav")
    output_text_file = os.path.join(output_folder, f"{file.replace('.mp4', '.txt')}")

    # Extract audio
    extracted_audio = extract_audio(mp4_file, audio_file)
    if not extracted_audio:
        print(f"Skipping {file} due to audio extraction failure.")
        return

    # Transcribe and diarize
    process_audio(audio_file, output_text_file, model_size, language, hf_token)


# Main Execution
def main():
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_size', type=str, default="small", help="Whisper model size")
    parser.add_argument('--language', type=str, default="el", help="Language code for transcription")
    parser.add_argument('--hftoken', type=str, required=True, help="Hugging Face token")
    parser.add_argument('--input_folder', type=str, default="/app/input", help="Folder for MP4 files")
    parser.add_argument('--output_folder', type=str, default="/app/output", help="Folder for transcripts")

    args = parser.parse_args()
    print(f"Using Whisper Model: {args.model_size}")

    os.makedirs(args.output_folder, exist_ok=True)

    # List all MP4 files
    files = [file for file in os.listdir(args.input_folder) if file.endswith(".mp4")]
    if not files:
        print("No MP4 files found in the input folder.")
        return

    print(f"Processing {len(files)} files in parallel...")

    for file in files:
        process_file(file, args.input_folder, args.output_folder, args.model_size, args.language, args.hftoken)

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()

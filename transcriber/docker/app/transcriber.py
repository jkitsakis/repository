import os
import argparse
import subprocess
import pickle
import whisper
import time
import torch
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor, as_completed
from pyannote.audio.pipelines import SpeakerDiarization

# Load Pyannote model once per worker process
diarization_model = None
whisper_model = None  # Store Whisper model globally for reuse


def save_diarization_results(speaker_segments, output_file):
    """Saves speaker diarization results to a file."""
    with open(output_file, "wb") as f:
        pickle.dump(speaker_segments, f)
    print(f"Speaker diarization results saved to {output_file}.")


def load_diarization_results(output_file):
    """Loads speaker diarization results from a file."""
    if os.path.exists(output_file):
        with open(output_file, "rb") as f:
            return pickle.load(f)
    return None


def load_diarization_model():
    """Loads and returns the Pyannote speaker diarization model with GPU support."""
    global diarization_model
    if diarization_model is None:
        print(f"In load_diarization_model - HF_TOKEN:", os.getenv("HF_TOKEN"))
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            diarization_model = SpeakerDiarization.from_pretrained(
                "pyannote/speaker-diarization-3.1",
                use_auth_token=os.getenv("HF_TOKEN")
            )
            diarization_model.to(torch.device(device))
            print(f"Speaker diarization model loaded on {device.upper()}.")
        except Exception as e:
            print(f"Error loading Pyannote model: {e}")
            diarization_model = None
    return diarization_model


def load_whisper_model(model_size):
    """Loads and returns the Whisper model for transcription."""
    global whisper_model
    if whisper_model is None:
        print(f"Loading Whisper model: {model_size}...")
        whisper_model = whisper.load_model(model_size)
    return whisper_model


def extract_audio(mp4_file, output_audio):
    """Extracts audio from an MP4 file as WAV format."""
    if not os.path.exists(mp4_file):
        print(f"File not found: {mp4_file}")
        return None

    print(f"Extracting audio from {mp4_file}...")
    command = ["ffmpeg", "-i", mp4_file, "-ac", "1", "-ar", "16000", "-vn", output_audio, "-y"]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(output_audio):
        print(f"Error: Audio extraction failed for {mp4_file}")
        return None

    return output_audio

# Merges consecutive segments if they are from the same speaker and within 1.5 seconds of each other.
# Reduces small fragments, leading to fewer but longer segments.
# Maintains diarization accuracy while making transcription more efficient.
def apply_diarization(audio_file, min_segment_duration=5.0):
    """Applies speaker diarization and merges short segments."""
    model = load_diarization_model()
    if model is None:
        print("Skipping diarization due to model loading failure.")
        return []

    print(f"Applying speaker diarization on {audio_file}...")
    diarization_result = model(audio_file)

    speaker_segments = []
    speaker_map = {}
    speaker_counter = 1

    # Merge short segments based on a minimum segment duration
    last_end_time = None
    current_segment = []

    for turn, _, speaker in diarization_result.itertracks(yield_label=True):
        # Check if the segment is too short and should be merged with the previous one
        if last_end_time is not None and turn.start - last_end_time < min_segment_duration:
            # Merge this segment with the previous one
            current_segment[1] = turn.end
        else:
            if current_segment:
                # Add the previous segment before starting a new one
                speaker_segments.append(tuple(current_segment))
            # Start a new segment
            speaker_map[speaker] = f"SPEAKER_{speaker_counter}"
            speaker_counter += 1
            current_segment = [turn.start, turn.end, speaker]

        last_end_time = turn.end

    # Add the final segment if any
    if current_segment:
        speaker_segments.append(tuple(current_segment))

    if not speaker_segments:
        print(f"No speakers detected in {audio_file}")

    print(f"Reduced speaker segments: {len(speaker_segments)}")
    return speaker_segments


def transcribe_segment(args):
    """Transcribes a specific time segment of an audio file."""
    audio_file, start, end, model_size, language = args

    # Reload Whisper model inside each worker to prevent deadlocks
    whisper_model = whisper.load_model(model_size)
    temp_file = f"{audio_file}_segment_{start:.2f}_{end:.2f}.wav"

    # Extract segment
    command = ["ffmpeg", "-i", audio_file, "-ss", str(start), "-t", str(end - start), "-ac", "1", "-ar", "16000", "-vn",
               temp_file, "-y"]
    try:
        result_subprocess = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                           timeout=60)

        # Check if there were any errors
        if result_subprocess.returncode != 0:
            print(f"FFmpeg error extracting segment {start:.2f}-{end:.2f}: {result_subprocess.stderr}")
            return start, end, "[ERROR: Failed extraction]"

        if not os.path.exists(temp_file):
            print(f"Error: Failed to extract segment {start:.2f}-{end:.2f}")
            return start, end, "[ERROR: Failed extraction]"

        # Transcribe
        result = whisper_model.transcribe(temp_file, temperature=0.0, beam_size=1, language=language)
        os.remove(temp_file)
        return start, end, result["text"]

    except subprocess.TimeoutExpired:
        print(f"FFmpeg timeout expired while processing segment {start:.2f}-{end:.2f}")
        return start, end, "[ERROR: Timeout]"

    except Exception as e:
        print(f"Error processing segment {start:.2f}-{end:.2f}: {e}")
        return start, end, "[ERROR: General failure]"


def format_transcription(args):
    """Formats a transcription entry."""
    (start, end, speaker), (_, _, text) = args
    return f"[{speaker}] {start:.2f} - {end:.2f}: {text}"


def process_file(file, input_folder, output_folder, model_size, language):
    """Processes a single file: extracts audio, applies diarization, and transcribes."""
    print(f"Processing file: {file}")

    mp4_file = os.path.join(input_folder, file)
    audio_file = os.path.join(output_folder, f"{file}.wav")
    diarization_cache_file = os.path.join(output_folder, f"{file}_diarization.pkl")

    # Extract audio
    extracted_audio = extract_audio(mp4_file, audio_file)
    if not extracted_audio:
        return

    # Check if diarization results exist (cached)
    speaker_segments = load_diarization_results(diarization_cache_file)

    if not speaker_segments:
        # Apply speaker diarization if no cached result is found
        speaker_segments = apply_diarization(audio_file)
        if not speaker_segments:
            print(f"Skipping transcription for {file}: No speakers detected.")
            return

        # Save diarization results for future use
        save_diarization_results(speaker_segments, diarization_cache_file)

    print(f"Speaker Segments for {file}: {len(speaker_segments)} segments found.")

    # Transcribe segments
    with ThreadPoolExecutor(max_workers=min(cpu_count(), 4)) as executor:
        futures = {
            executor.submit(transcribe_segment, (audio_file, start, end, model_size, language)): (start, end)
            for start, end, _ in speaker_segments
        }

        transcriptions = []
        for future in as_completed(futures):
            try:
                transcriptions.append(future.result())  # Collect results safely
            except Exception as e:
                start, end = futures[future]
                print(f"Error transcribing segment {start:.2f}-{end:.2f}: {e}")
                transcriptions.append((start, end, "[ERROR: Transcription failed]"))

    # Format output (using ThreadPoolExecutor for efficiency)
    with ThreadPoolExecutor(max_workers=min(cpu_count(), 4)) as executor:
        full_transcript = list(executor.map(format_transcription, zip(speaker_segments, transcriptions)))

    transcript_path = os.path.join(output_folder, file.replace(".mp4", "_diarized_transcript_" + model_size + ".txt"))

    # Save transcript
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_transcript))

    print(f"Transcript saved: {transcript_path}")


def main():
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_size', type=str, default="small", help="Whisper model size")
    parser.add_argument('--language', type=str, default="el", help="Language code for transcription")
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

    num_workers = min(cpu_count(), len(files))
    with Pool(processes=num_workers) as pool:
        pool.starmap(
            process_file,
            [(file, args.input_folder, args.output_folder, args.model_size, args.language) for file in files]
        )

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()

import os
import argparse
import subprocess
import whisper
import time
from multiprocessing import Pool
from functools import partial


# Function to extract audio from an MP4 file
def extract_audio(mp4_file, output_audio):
    """Extracts audio from an MP4 file as WAV format."""
    print(f"Extracting audio from {mp4_file}...")
    command = [
        "ffmpeg", "-i", mp4_file,
        "-ac", "1", "-ar", "16000", "-vn",
        output_audio
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Audio extracted: {output_audio}")


# Function to get audio duration
def get_audio_duration(input_audio):
    """Extracts duration from an audio file using FFmpeg."""
    command = ["ffmpeg", "-i", input_audio, "-f", "null", "-"]
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)

    duration_str = None
    for line in result.stderr.splitlines():
        if "Duration:" in line:
            duration_str = line.split("Duration:")[1].split(",")[0].strip()
            break

    if not duration_str:
        return 0

    hours, minutes, seconds = map(float, duration_str.split(":"))
    return int(hours * 3600 + minutes * 60 + seconds)


# Function to split audio into smaller chunks
def split_audio(input_audio, output_folder, chunk_length_sec=600):
    """Splits the audio file into smaller chunks."""
    os.makedirs(output_folder, exist_ok=True)
    total_seconds = get_audio_duration(input_audio)

    chunks = []
    for start_sec in range(0, total_seconds, chunk_length_sec):
        chunk_filename = os.path.join(output_folder, f"chunk_{start_sec}.wav")
        command = [
            "ffmpeg", "-i", input_audio, "-ss", str(start_sec), "-t", str(chunk_length_sec),
            "-ac", "1", "-ar", "16000", "-vn", chunk_filename
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        chunks.append(chunk_filename)

    return chunks


# Function to transcribe audio
def transcribe_audio(audio_file, model_size, language):
    """Transcribes an audio file using OpenAI Whisper."""
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_file, temperature=0.0, beam_size=1, language=language)
    return result["text"]


# Wrapper function for transcription
def transcribe_audio_wrapper(chunk, model_size, language):
    print(f"Transcribing chunk : {chunk}")
    return transcribe_audio(chunk, model_size, language)


# Main function
def main():
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_size', type=str, default="small", help="Whisper model size")
    parser.add_argument('--language', type=str, default="el", help="Language code for transcription")
    parser.add_argument('--input_folder', type=str, default="/app/input", help="Folder for MP4 files")
    parser.add_argument('--output_folder', type=str, default="/app/output", help="Folder for transcripts")

    args = parser.parse_args()
    print(f"Using Whisper Model  : {args.model_size}")

    os.makedirs(args.output_folder, exist_ok=True)

    for file in os.listdir(args.input_folder):
        if file.endswith(".mp4"):
            mp4_file = os.path.join(args.input_folder, file)
            audio_file = os.path.join(args.output_folder, "temp_audio.wav")

            # Extract audio
            extract_audio(mp4_file, audio_file)

            # Split audio into chunks
            chunks = split_audio(audio_file, os.path.join(args.output_folder, "chunks"))
            print(f"Extracted chunks : {chunks}")

            # Create a partial function with the required additional arguments
            transcribe_partial = partial(transcribe_audio_wrapper, model_size=args.model_size, language=args.language)

            # Use multiprocessing to speed up transcription
            print(f"Use multiprocessing to speed up transcription")
            with Pool() as pool:
                transcripts = pool.map(transcribe_partial, chunks)

            full_transcript = "\n".join(transcripts)
            print(f"Full Transcript: {full_transcript}")

            # Save transcript
            transcript_path = os.path.join(args.output_folder, file.replace(".mp4", "_transcript_" + args.model_size + ".txt"))
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(f"Transcription:\n{full_transcript}")

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()

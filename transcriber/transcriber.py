import os
import argparse
import subprocess
import tkinter as tk
from multiprocessing import Pool
from tkinter import filedialog
from tkinter import ttk
import whisper
import time
from multiprocessing import Pool, cpu_count


def extract_audio(mp4_file, output_audio, progress_var):
    """Extracts audio from an MP4 file as WAV format."""
    print(f"Extracting audio from {mp4_file}...")
    command = [
        "ffmpeg", "-i", mp4_file,
        "-ac", "1", "-ar", "16000",  # Mono channel, 16kHz for better transcription
        "-vn",  # Remove video
        output_audio
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Audio extracted: {output_audio}")


def split_audio(input_audio, output_folder, chunk_length_sec, progress_var):
    """Splits the audio file into smaller chunks using ffmpeg."""
    print(f"Splitting audio into chunks...")
    os.makedirs(output_folder, exist_ok=True)

    # Get audio file duration
    command = [
        "ffmpeg", "-i", input_audio, "-f", "null", "-"
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the ffmpeg stderr to help debug the output
    print("ffmpeg stderr output:")
    print(result.stderr)

    # Extract duration from stderr
    duration_str = None
    for line in result.stderr.splitlines():
        if "Duration:" in line:
            duration_str = line.split("Duration:")[1].split(",")[0].strip()
            break

    if not duration_str:
        print("Error: Could not find audio duration in ffmpeg output.")
        return []

    try:
        hours, minutes, seconds = map(float, duration_str.split(":"))
        total_seconds = int(hours * 3600 + minutes * 60 + seconds)
    except ValueError:
        print(f"Error: Failed to parse duration '{duration_str}'.")
        return []

    print(f"Audio duration: {total_seconds} seconds")

    # Split the audio into chunks
    chunks = []
    total_chunks = total_seconds // chunk_length_sec + (1 if total_seconds % chunk_length_sec != 0 else 0)
    for start_sec in range(0, total_seconds, chunk_length_sec):
        chunk_filename = os.path.join(output_folder, f"chunk_{start_sec}.wav")
        command = [
            "ffmpeg", "-i", input_audio,
            "-ss", str(start_sec), "-t", str(chunk_length_sec), "-ac", "1",
            "-ar", "16000",  # Mono channel, 16kHz for better transcription
            "-vn",  # Remove video
            chunk_filename
        ]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        chunks.append(chunk_filename)
        progress_var.set(25 + (50 * len(chunks)) // total_chunks)  # Update progress bar

    return chunks

def select_file():
    """Opens a file dialog to select the MP4 file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an MP4 file",
        filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*"))
    )
    return file_path


def transcribe_audio_chunk(chunk, model_size, language="el"):
    """Transcribes a single chunk of audio using OpenAI Whisper with the specified language."""
    try:
        print(f"Loading Whisper model: {model_size} for chunk {chunk}...")
        model = whisper.load_model(model_size)
        print(f"Transcribing {chunk} with Whisper in {language}...")
        result = model.transcribe(chunk, temperature=0.0, beam_size=1, language=language)  # Specify language
        return result["text"]
    except Exception as e:
        print(f"Error transcribing {chunk}: {str(e)}")
        return ""

def main():
    start_time = time.time()  # Record the start time
    # Set up argparse to get model_size and language from command-line arguments
    parser = argparse.ArgumentParser(description="Transcribe audio using OpenAI Whisper.")
    parser.add_argument('--model_size', type=str, default="small", help="Whisper model size (e.g., 'small', 'medium', 'large')")
    parser.add_argument('--language', type=str, default="el", help="Language code for transcription (e.g., 'el' for Greek)")

    args = parser.parse_args()

    mp4_file = select_file()  # Open the file dialog to select the file
    if not mp4_file:
        print("No file selected. Exiting...")
        return

    if not os.path.exists(mp4_file):
        print(f"Error: File '{mp4_file}' not found!")
        return

    audio_file = os.path.abspath("temp_audio.wav")
    temp_folder = os.path.abspath("audio_chunks")

    root = tk.Tk()
    root.title("Processing...")
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(padx=20, pady=20)

    try:
        extract_audio(mp4_file, audio_file, progress_var)

        if not os.path.exists(audio_file):
            print(f"Error: Audio file '{audio_file}' was not created.")
            return

        chunks = split_audio(audio_file, temp_folder, chunk_length_sec=600, progress_var=progress_var)

        full_transcript = ""
        num_processes = min(cpu_count(), len(chunks))  # Use CPU count but no more than the number of chunks
        with Pool(processes=num_processes) as pool:
            # Each chunk is processed in parallel with its transcription
            transcripts = pool.starmap(transcribe_audio_chunk,
                                       [(chunk, args.model_size, args.language) for chunk in chunks])

        # Combine the results and delete the chunks
        for i, transcript in enumerate(transcripts):
            full_transcript += transcript + "\n\n"
            os.remove(chunks[i])  # Remove chunk after processing
            progress_var.set(75 + (25 * (i + 1)) // len(chunks))  # Update progress bar

        print("\n=== Full Transcription ===\n")
        print(full_transcript)

        output_txt = os.path.splitext(mp4_file)[0] + "_transcript_"+ args.model_size+".txt"
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(full_transcript)
        print(f"\nTranscription saved to {output_txt}")

    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
        if os.path.exists(temp_folder):
            os.rmdir(temp_folder)

        progress_var.set(100)
        root.after(1000, root.quit)
        root.mainloop()

    # Calculate and print the total execution time
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the total execution time
    print(f"\nTotal execution time: {execution_time:.2f} seconds")  # Print the execution time

if __name__ == "__main__":
    main()

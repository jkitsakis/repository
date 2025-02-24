import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Correct import for ttk (Progressbar)
import whisper


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


def transcribe_audio(audio_file, model_size="large", progress_var=None):
    """Transcribes an audio file using OpenAI Whisper."""
    print(f"Loading Whisper model: {model_size}...")
    model = whisper.load_model(model_size)
    print("Transcribing with beam search...")
    result = model.transcribe(audio_file, temperature=0.0, beam_size=5)  # Optimal for best accuracy
    if progress_var:
        progress_var.set(75)  # Update progress bar
    return result["text"]


def select_file():
    """Opens a file dialog to select the MP4 file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an MP4 file",
        filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*"))
    )
    return file_path


def main():
    """Main function to handle user input and process the MP4 file."""
    mp4_file = select_file()  # Open the file dialog to select the file
    if not mp4_file:
        print("No file selected. Exiting...")
        return

    if not os.path.exists(mp4_file):
        print(f"Error: File '{mp4_file}' not found!")
        return

    # Setup paths using absolute paths
    audio_file = os.path.abspath("temp_audio.wav")  # Temporary audio file with absolute path
    temp_folder = os.path.abspath("audio_chunks")  # Temporary folder to store chunks

    # Create a Tkinter root window to display the progress bar
    root = tk.Tk()
    root.title("Processing...")
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)  # Corrected Progressbar import
    progress_bar.pack(padx=20, pady=20)

    try:
        # Step 1: Extract audio from the MP4 file
        extract_audio(mp4_file, audio_file, progress_var)

        # Check if the audio file was created successfully
        if not os.path.exists(audio_file):
            print(f"Error: Audio file '{audio_file}' was not created.")
            return

        # Step 2: Split audio into chunks
        chunks = split_audio(audio_file, temp_folder, chunk_length_sec=600, progress_var=progress_var)

        # Step 3: Transcribe each chunk and combine the result
        full_transcript = ""
        total_chunks = len(chunks)
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i + 1}/{total_chunks}: {chunk}")
            transcript = transcribe_audio(chunk, model_size="large", progress_var=progress_var)
            full_transcript += transcript + "\n\n"
            os.remove(chunk)  # Remove chunk after processing
            progress_var.set(75 + (25 * (i + 1)) // total_chunks)  # Update progress bar for transcription

        print("\n=== Full Transcription ===\n")
        print(full_transcript)

        # Save the transcript to a file
        output_txt = os.path.splitext(mp4_file)[0] + "_transcript.txt"
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(full_transcript)
        print(f"\nTranscription saved to {output_txt}")

    finally:
        # Cleanup temporary files
        if os.path.exists(audio_file):
            os.remove(audio_file)
        if os.path.exists(temp_folder):
            os.rmdir(temp_folder)

        # Finish up progress bar
        progress_var.set(100)
        root.after(1000, root.quit)  # Close after a short delay
        root.mainloop()


if __name__ == "__main__":
    main()

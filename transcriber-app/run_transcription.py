import os
import subprocess
from pydub import AudioSegment
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import datetime
import psutil

WHISPER_CPP_PATH = "./whisper.cpp/build/bin/whisper-cli"
AUDIO_DIR = "./audio"
OUTPUT_DIR = "./output"
INPUT_DIR = "./input"

def find_mp4():
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".mp4")]
    if not files:
        print("❗ No MP4 file found in input/ folder!")
        exit(1)
    return [os.path.join(INPUT_DIR, f) for f in files]

def convert_mp4_to_wav(mp4_path):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    basename = os.path.splitext(os.path.basename(mp4_path))[0]
    wav_path = os.path.join(AUDIO_DIR, f"{basename}.wav")
    audio = AudioSegment.from_file(mp4_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(wav_path, format="wav")
    return wav_path

def choose_model():
    models = [f for f in os.listdir("./models") if f.endswith(".bin")]
    if not models:
        print("❗ No Whisper models found in ./models/")
        exit(1)
    print("🧠 Available models:")
    for idx, name in enumerate(models, start=1):
        print(f"{idx}. {name}")
    choice = int(input("Select model [1-{}]: ".format(len(models)))) - 1
    return os.path.join("./models", models[choice])

def choose_language():
    print("\n🌐 Select transcription language:")
    print("1. auto (auto-detect)")
    print("2. en (English)")
    print("3. el (Greek)")
    lang_map = {"1": "auto", "2": "en", "3": "el"}
    lang_input = input("Choose [1-3]: ").strip()
    return lang_map.get(lang_input, "auto")

def transcribe_with_whisper(wav_path, model_path, language_code):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    basename = os.path.splitext(os.path.basename(wav_path))[0]
    output_prefix = os.path.join(OUTPUT_DIR, f"raw_{basename}")
    command = [
        WHISPER_CPP_PATH,
        "-m", model_path,
        "-f", wav_path,
        "-otxt",
        "-of", output_prefix
    ]
    if language_code != "auto":
        command += ["-l", language_code]
    print(f"🔠 Running whisper with model: {os.path.basename(model_path)} and language: {language_code}")
    subprocess.run(command, check=True)
    return output_prefix + ".txt"

def diarize(wav_path):
    wav = preprocess_wav(wav_path)
    encoder = VoiceEncoder()

    # Split into 30-second chunks to reduce RAM load
    window_duration = 30  # seconds
    sample_rate = 16000
    chunk_samples = window_duration * sample_rate

    total_samples = len(wav)
    embeddings = []

    print(f"🔁 Diarizing in {total_samples // chunk_samples + 1} chunks...")

    for start in range(0, total_samples, chunk_samples):
        chunk = wav[start:start + chunk_samples]
        if len(chunk) == 0:
            continue
        try:
            chunk_embeds = encoder.embed_utterance(chunk, return_partials=True, rate=8)
            if isinstance(chunk_embeds, list):
                embeddings.extend(chunk_embeds)
            # ✅ Print RAM after every chunk
            print(f"🧠 RAM used: {psutil.virtual_memory().percent}%")
        except Exception as e:
            print(f"⚠️ Skipping chunk due to error: {e}")

    if len(embeddings) < 2:
        print("⚠️ Not enough valid embeddings for clustering. Assigning Speaker 0 to all.")
        labels = [0] * len(embeddings)
    else:
        from sklearn.cluster import MiniBatchKMeans
        clustering = MiniBatchKMeans(n_clusters=2, batch_size=256, random_state=42)
        embeddings = np.stack([e for e in embeddings if isinstance(e, np.ndarray)])
        labels = clustering.fit_predict(embeddings)

    segment_duration = 0.5
    times = [i * segment_duration for i in range(len(labels))]
    return list(zip(labels, times))


def merge_transcript_with_speakers(transcript_txt, diarization):
    with open(transcript_txt, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    segment_duration = 0.5
    output_lines = []
    for i, line in enumerate(lines):
        segment_time = i * segment_duration
        speaker_label = 0
        for label, time in diarization:
            if time < segment_time:
                speaker_label = label
            else:
                break
        timestamp = str(datetime.timedelta(seconds=int(segment_time)))
        output_lines.append(f"[{timestamp}] Speaker {speaker_label}: {line}")

    base = os.path.splitext(os.path.basename(transcript_txt))[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base}_diarized.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    return output_path

def main():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    mp4_files  = find_mp4()
    model_path = choose_model()
    language_code = choose_language()

    for mp4 in mp4_files:
        print(f"\n🎬 Processing: {mp4}")
        wav = convert_mp4_to_wav(mp4)
        raw_transcript_txt = transcribe_with_whisper(wav, model_path, language_code)
        diarization = diarize(wav)
        merge_transcript_with_speakers(raw_transcript_txt, diarization)
        output_name = os.path.splitext(os.path.basename(mp4))[0] + ".txt"
        print(f"✅ Done: {OUTPUT_DIR}/{output_name}")


if __name__ == "__main__":
    main()

import numpy as np
import tempfile
import os
import scipy.io.wavfile as wav
from faster_whisper import WhisperModel

try:
    import sounddevice as sd
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("⚠️ sounddevice not available. Mic input will be skipped.")

model = WhisperModel("base", compute_type="float32")

def record_audio(duration=6, fs=16000):
    if not SOUND_AVAILABLE:
        print("⚠️ Skipping audio recording - sounddevice not available.")
        return create_dummy_audio(fs)

    try:
        print("🎙️ Recording...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        _, path = tempfile.mkstemp(suffix=".wav")
        wav.write(path, fs, np.int16(recording * 32767))
        print("✅ Audio saved:", path)
        return path
    except Exception as e:
        print(f"❌ Audio capture failed: {e}")
        return create_dummy_audio(fs)

def create_dummy_audio(fs):
    path = os.path.join(tempfile.gettempdir(), "dummy.wav")
    silence = np.zeros((fs * 2,), dtype=np.int16)  # 2 seconds of silence
    wav.write(path, fs, silence)
    print("🔇 Dummy audio file created:", path)
    return path

def transcribe_audio(audio_path):
    segments, _ = model.transcribe(audio_path)
    return " ".join([seg.text for seg in segments])

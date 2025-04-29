
# config.py
OPENAI_API_KEY = None
DEFAULT_LANGUAGE = None
MODEL_FOLDER = None
SOUNDS_FOLDER = None

AVAILABLE_LANGUAGES = ["English", "Greek"]

LANGUAGE_MODEL_MAP = {
    "English": "vosk-model-small-en-us-0.15",
    "Greek": "vosk-model-el-gr-0.7"
}

START_SOUND_FILE = "start.wav"
STOP_SOUND_FILE = "stop.wav"
SESSION_LOG_FILE = "session_log.txt"

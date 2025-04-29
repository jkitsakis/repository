
# start_assistant.py
import argparse
import config
from tutor_assistant_gui import TutorAssistantApp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--apikey', type=str, required=True)
    parser.add_argument('--defaultlang', type=str, default="English")
    parser.add_argument('--modelfolder', type=str, default="model")
    parser.add_argument('--soundsfolder', type=str, default="sounds")
    args = parser.parse_args()

    config.OPENAI_API_KEY = args.apikey
    config.DEFAULT_LANGUAGE = args.defaultlang
    config.MODEL_FOLDER = args.modelfolder
    config.SOUNDS_FOLDER = args.soundsfolder

    TutorAssistantApp().run()

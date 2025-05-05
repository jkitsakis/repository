
# assistant_engine.py
import openai
import vosk
import datetime
import json
import os
import config
import re

class AssistantEngine:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
        self.model = None
        self.language_choice = config.DEFAULT_LANGUAGE
        self.question_counter = 0

    def load_vosk_model(self):
        model_subpath = config.LANGUAGE_MODEL_MAP.get(self.language_choice)
        model_path = os.path.join(config.MODEL_FOLDER, model_subpath)
        if not model_path or not os.path.exists(model_path):
            raise Exception(f"Vosk model for {self.language_choice} not found at {model_path}")
        self.model = vosk.Model(model_path)

    def recognize_audio(self, recorded_audio):
        if not self.model:
            raise Exception("Vosk model not loaded.")
        recognizer = vosk.KaldiRecognizer(self.model, 16000)
        recognizer.AcceptWaveform(recorded_audio)
        result = recognizer.Result()
        text = json.loads(result).get("text", "")
        return text.strip()



    def refine_question(self, raw_text):
        try:
            # Mask protected terms (case-insensitive)
            protected_map = {}
            masked_text = raw_text
            for i, term in enumerate(config.PROTECTED_TERMS):
                pattern = re.compile(re.escape(term), re.IGNORECASE)
                if pattern.search(masked_text):
                    key = f"<TERM{i}>"
                    protected_map[key] = term
                    masked_text = pattern.sub(key, masked_text)

            refine_prompt = (
                "Please clean and rephrase into a clear, short question in "
                + ("Greek." if self.language_choice == "Greek" else "English.")
                + " Important: Do NOT translate any technical or scientific terms. "
                + "Return a short question, preserving placeholders like <TERM0>."
            )

            client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": refine_prompt},
                    {"role": "user", "content": masked_text}
                ]
            )
            refined = response.choices[0].message.content.strip()

            # Restore protected terms
            for key, term in protected_map.items():
                refined = refined.replace(key, term)

            return refined
        except Exception as e:
            print(f"Error refining question: {e}")
            return raw_text


    def ask_ai(self, question):
        try:
            system_prompt = f"You are a {config.ROLE}. Always reply in " + ("Greek." if self.language_choice == "Greek" else "English. Return a short question suitable for {config.ROLE}")
            client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            return answer
        except Exception as e:
            return f"Error asking AI: {e}"

    def log_session(self, question, answer):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(config.SESSION_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\n")
            f.write(f"Q: {question}\n")
            f.write(f"A: {answer}\n")
            f.write("\n" + "-"*50 + "\n")

    def next_question_number(self):
        self.question_counter += 1
        return self.question_counter

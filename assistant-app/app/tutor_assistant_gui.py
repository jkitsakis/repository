import datetime
import os
import tkinter as tk
from tkinter import scrolledtext, ttk
import sounddevice as sd
import pygame
import config
from assistant_engine import AssistantEngine
import threading

class TutorAssistantApp:
    def __init__(self):
        pygame.mixer.init()
        self.engine = AssistantEngine()
        self.window = tk.Tk()
        self.window.title("Tutor Assistant (Auto Device Selection)")
        self.window.geometry("950x800")
        self.recording = False
        self.recorded_audio = b""
        self.selected_device_id, self.device_name = self.find_best_input_device()
        self.stream = None
        self.build_gui()

    def find_best_input_device(self):
        devices = sd.query_devices()
        for idx, dev in enumerate(devices):
            name = dev['name'].lower()
            if dev['max_input_channels'] > 0:
                if any(keyword in name for keyword in ["stereo mix", "cable output", "loopback"]):
                    return idx, dev['name']
        return None, None

    def build_gui(self):
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12), height=12, width=80)
        self.text_area.pack(expand=True, fill='both', pady=10)

        if self.device_name:
            device_message = f"🎧 Using device: {self.device_name}"
        else:
            device_message = "⚠️ No suitable device found."

        self.status_label = tk.Label(self.window, text=device_message, font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.language_var = tk.StringVar(value=config.DEFAULT_LANGUAGE)
        self.language_dropdown = ttk.Combobox(self.window, textvariable=self.language_var, values=config.AVAILABLE_LANGUAGES, font=("Arial", 12))
        self.language_dropdown.pack(pady=5)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        start_button = tk.Button(button_frame, text="▶️ Start Recording", font=("Arial", 16), bg="lightgreen", command=self.start_recording)
        start_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(button_frame, text="⏹ Stop Recording", font=("Arial", 16), bg="salmon", command=self.stop_recording)
        stop_button.pack(side=tk.LEFT, padx=5)

        manual_label = tk.Label(self.window, text="Or type a question manually:", font=("Arial", 14))
        manual_label.pack(pady=5)

        self.manual_entry = tk.Entry(self.window, font=("Arial", 14), width=60)
        self.manual_entry.pack(pady=5)

        submit_button = tk.Button(self.window, text="🧠 Submit Typed Question", font=("Arial", 14), bg="lightblue", command=self.submit_typed_question)
        submit_button.pack(pady=5)

    def start_recording(self):
        try:
            if self.selected_device_id is None:
                raise Exception("No suitable recording device found.")
            sound_path = os.path.join(config.SOUNDS_FOLDER, config.START_SOUND_FILE)
            pygame.mixer.Sound(sound_path).play()
            self.engine.language_choice = self.language_var.get()
            self.engine.load_vosk_model()
            self.recording = True
            self.recorded_audio = b""
            self.stream = sd.RawInputStream(device=self.selected_device_id, samplerate=16000, blocksize=8000, dtype='int16',
                                            channels=1, callback=self.callback)
            self.stream.start()
            self.status_label.config(text="🎤 Recording...")
        except Exception as e:
            self.status_label.config(text=f"Error starting recording: {e}")

    def stop_recording(self):
        try:
            sound_path = os.path.join(config.SOUNDS_FOLDER, config.STOP_SOUND_FILE)
            pygame.mixer.Sound(sound_path).play()
            self.recording = False
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.stream = None
            text = self.engine.recognize_audio(self.recorded_audio)
            if text:
                self.process_question(text)
            else:
                self.status_label.config(text="⚠️ No speech detected.")
        except Exception as e:
            self.status_label.config(text=f"Error stopping recording: {e}")

    def submit_typed_question(self):
        typed = self.manual_entry.get()
        if typed.strip():
            self.process_question(typed.strip())
        else:
            self.status_label.config(text="⚠️ Please type a question first.")

    def process_question(self, text):
        self.status_label.config(text="🛠 Refining...")
        def refine_and_ask():
            refined = self.engine.refine_question(text)
            answer = self.engine.ask_ai(refined)
            q_num = self.engine.next_question_number()
            self.update_gui(q_num, refined, answer)
            self.engine.log_session(refined, answer)
        threading.Thread(target=refine_and_ask, daemon=True).start()

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.recorded_audio += bytes(indata)

    def update_gui(self, q_num, question, answer):
        self.text_area.insert(tk.END, f"\n\n💬 Q{q_num}: {question}\n\n🤖 Answer: {answer}\n")
        self.text_area.see(tk.END)
        self.log_to_file(question, answer)

    def log_to_file(question, answer):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("session_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\n")
            f.write(f"Q: {question}\n")
            f.write(f"A: {answer}\n")
            f.write("\n" + "-" * 50 + "\n")

    def run(self):
        self.window.mainloop()

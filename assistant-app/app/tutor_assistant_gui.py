import datetime
import os
import tkinter as tk
from tkinter import scrolledtext, ttk
import sounddevice as sd
import pygame
import config
from assistant_engine import AssistantEngine
import threading

def label_device(name, direction="input"):
    lower = name.lower()
    if "vb-audio virtual" in lower or "vb-audio cable" in lower:
        if "output" in lower:
            return "🔈 System Audio (VB-Cable)"
        if "input" in lower:
            return "🎧 VB-Cable Input"
    if "stereo mix" in lower:
        return "🔈 Stereo Mix (System Loopback)"
    if "voicemeeter" in lower:
        if "out" in lower:
            return f"🎚 VoiceMeeter Out"
        if "in" in lower:
            return f"🎚 VoiceMeeter In"
        return f"🎚 VoiceMeeter"
    if "microphone" in lower:
        return "🎤 Microphone"
    if "array" in lower:
        return "🎤 Internal Mic"
    if "headset" in lower:
        return "🎧 Headset"
    if "realtek" in lower:
        return "🎧 Realtek Output" if direction == "output" else "🎤 Realtek Mic"
    if "dock" in lower:
        return "🧩 Dock Audio"
    if "display audio" in lower or "hdmi" in lower:
        return "🖥️ HDMI Audio"
    if "mapper" in lower or "primary" in lower:
        return "🌀 Windows Default"
    return name.strip()

class TutorAssistantApp:
    def __init__(self):
        pygame.mixer.init()
        self.engine = AssistantEngine()
        self.window = tk.Tk()
        self.window.title("Tutor Assistant (Filtered Devices)")
        self.window.geometry("950x850")
        self.recording = False
        self.recorded_audio = b""
        self.selected_input_id = None
        self.selected_output_id = None
        self.stream = None
        self.build_gui()

    def build_gui(self):
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=2)
        self.window.rowconfigure(8, weight=1)

        self.input_map = {}
        self.output_map = {}
        input_seen = set()
        output_seen = set()
        input_list = []
        output_list = []

        default_input_index, default_output_index = sd.default.device

        for idx, dev in enumerate(sd.query_devices()):
            base_name = dev['name']
            label = f"{label_device(base_name)}  [{idx}]"

            if dev['max_input_channels'] > 0 and base_name not in input_seen:
                marker = ">" if idx == default_input_index else " "
                print(f"Input Devices: {marker} {label}")
                input_list.append(f"{marker} {label}")
                self.input_map[f"{marker} {label}"] = idx
                input_seen.add(base_name)
                # print(f"Input Devices: {input_seen}")

            if dev['max_output_channels'] > 0 and base_name not in output_seen:
                marker = ">" if idx == default_output_index else " "
                print(f"Output Devices: {marker} {label}")
                output_list.append(f"{marker} {label}")
                self.output_map[f"{marker} {label}"] = idx
                output_seen.add(base_name)
                # print(f"Output Devices: {output_seen}")


        # Input Device
        tk.Label(self.window, text="Select Input Device:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10)
        self.input_choice = tk.StringVar(value=input_list[0] if input_list else "")
        self.input_dropdown = ttk.Combobox(self.window, values=input_list, textvariable=self.input_choice, font=("Arial", 12))
        self.input_dropdown.grid(row=1, column=0, padx=150, sticky="ew")

        # Output Device
        tk.Label(self.window, text="Select Output Device:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10)
        self.output_choice = tk.StringVar(value=output_list[0] if output_list else "")
        self.output_dropdown = ttk.Combobox(self.window, values=output_list, textvariable=self.output_choice, font=("Arial", 12))
        self.output_dropdown.grid(row=2, column=0, padx=150, sticky="ew")

        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12), height=4)
        self.text_area.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.status_label = tk.Label(self.window, text="Select devices and start recording.", font=("Arial", 12))
        self.status_label.grid(row=3, column=0, pady=5, sticky="ew")

        self.language_var = tk.StringVar(value=config.DEFAULT_LANGUAGE)
        self.language_dropdown = ttk.Combobox(self.window, textvariable=self.language_var, values=config.AVAILABLE_LANGUAGES, font=("Arial", 12))
        self.language_dropdown.grid(row=4, column=0, pady=5, padx=10, sticky="ew")

        button_frame = tk.Frame(self.window)
        button_frame.grid(row=5, column=0, pady=10)

        start_button = tk.Button(button_frame, text="▶️ Start Recording", font=("Arial", 16), bg="lightgreen", command=self.start_recording)
        start_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(button_frame, text="⏹ Stop Recording", font=("Arial", 16), bg="salmon", command=self.stop_recording)
        stop_button.pack(side=tk.LEFT, padx=5)

        manual_label = tk.Label(self.window, text="Or type a question manually:", font=("Arial", 14))
        manual_label.grid(row=6, column=0, pady=5, sticky="w")

        self.manual_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12), height=4)
        self.manual_text.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")

        submit_button = tk.Button(self.window, text="🧠 Submit Typed Question", font=("Arial", 14), bg="lightblue", command=self.submit_typed_question)
        submit_button.grid(row=8, column=0, pady=10, sticky="e")

    def start_recording(self):
        try:
            in_label = self.input_choice.get()
            out_label = self.output_choice.get()
            self.selected_input_id = self.input_map.get(in_label)
            self.selected_output_id = self.output_map.get(out_label)

            if self.selected_input_id is None or self.selected_output_id is None:
                raise Exception("Invalid input or output device selected.")

            sd.default.device = (self.selected_input_id, self.selected_output_id)

            sound_path = os.path.join(config.SOUNDS_FOLDER, config.START_SOUND_FILE)
            pygame.mixer.Sound(sound_path).play()
            self.engine.language_choice = self.language_var.get()
            self.engine.load_vosk_model()
            self.recording = True
            self.recorded_audio = b""
            self.stream = sd.RawInputStream(device=self.selected_input_id, samplerate=16000, blocksize=8000, dtype='int16',
                                            channels=1, callback=self.callback)
            self.stream.start()
            self.status_label.config(text=f"🎤 Recording from: {in_label}")
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
                self.status_label.config(text=f"🎤 Ready to Record from: {self.input_choice.get()}")
            else:
                self.status_label.config(text="⚠️ No speech detected.")
        except Exception as e:
            self.status_label.config(text=f"Error stopping recording: {e}")

    def submit_typed_question(self):
        typed = self.manual_text.get("1.0", tk.END).strip()
        if typed:
            self.process_question(typed)
        else:
            self.status_label.config(text="⚠️ Please type a question first.")

    def process_question(self, text):
        print(f"Refining Raw Text : {text}")
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

    def log_to_file(self, question, answer):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("session_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\n")
            f.write(f"Q: {question}\n")
            f.write(f"A: {answer}\n")
            f.write("\n" + "-" * 50 + "\n")

    def run(self):
        self.window.mainloop()
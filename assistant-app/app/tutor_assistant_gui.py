
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
        self.window.title("Tutor Assistant")
        self.window.geometry("950x650")
        self.recording = False
        self.recorded_audio = b""
        self.stream = None
        self.selected_input_id = None
        self.selected_output_id = None
        self.build_gui()
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)  # Make the text_area row scalable

    def build_gui(self):
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 10), height=20)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.text_area.tag_configure("paragraph", spacing3=8, lmargin1=4, lmargin2=4)
        self.text_area.tag_configure("bold", font=("Arial", 12, "bold"))

        self.status_label = tk.Label(self.window, text="Select devices and model, then start recording.",
                                     font=("Arial", 12))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Label(self.window, text="Language/Model:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10)
        self.language_var = tk.StringVar(value=config.DEFAULT_LANGUAGE)
        self.language_dropdown = ttk.Combobox(self.window, textvariable=self.language_var,
                                              values=config.AVAILABLE_LANGUAGES, font=("Arial", 12))
        self.language_dropdown.grid(row=2, column=0, padx=150, sticky="ew")

        self.input_map = {}
        self.output_map = {}
        input_list = []
        output_list = []
        input_seen = set()
        output_seen = set()
        default_input_index, default_output_index = sd.default.device

        for idx, dev in enumerate(sd.query_devices()):
            base_name = dev['name']
            label = f"{label_device(base_name)} [{idx}]"
            if dev['max_input_channels'] > 0 and base_name not in input_seen:
                marker = ">" if idx == default_input_index else " "
                input_list.append(f"{marker} {label}")
                self.input_map[f"{marker} {label}"] = idx
                input_seen.add(base_name)
            if dev['max_output_channels'] > 0 and base_name not in output_seen:
                marker = ">" if idx == default_output_index else " "
                output_list.append(f"{marker} {label}")
                self.output_map[f"{marker} {label}"] = idx
                output_seen.add(base_name)

        tk.Label(self.window, text="Input Device:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10)
        self.input_choice = tk.StringVar(value=input_list[0] if input_list else "")
        self.input_dropdown = ttk.Combobox(self.window, values=input_list, textvariable=self.input_choice,
                                           font=("Arial", 12))
        self.input_dropdown.grid(row=3, column=0, padx=150, sticky="ew")

        tk.Label(self.window, text="Output Device:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=10)
        self.output_choice = tk.StringVar(value=output_list[0] if output_list else "")
        self.output_dropdown = ttk.Combobox(self.window, values=output_list, textvariable=self.output_choice,
                                            font=("Arial", 12))
        self.output_dropdown.grid(row=4, column=0, padx=150, sticky="ew")

        button_frame = tk.Frame(self.window)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        self.toggle_button = tk.Button(button_frame, text="▶️ Start Recording", font=("Arial", 16), bg="lightgreen",
                                       command=self.toggle_recording)
        self.toggle_button.pack(side=tk.LEFT, padx=5)

        self.manual_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12), height=4)
        self.manual_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.manual_text.bind("<Return>", lambda e: (self.submit_typed_question(), "break"))

        submit_button = tk.Button(self.window, text="🧠 Submit Typed Question", font=("Arial", 14), bg="lightblue",
                                  command=self.submit_typed_question)
        submit_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="e")

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
            self.toggle_button.config(text="⏸ Pause", bg="orange")
        else:
            self.pause_recording()
            self.toggle_button.config(text="▶️ Resume", bg="lightgreen")

    def start_recording(self):
        try:
            self.text_area.delete("1.0", tk.END)
            self.manual_text.delete("1.0", tk.END)
            self.engine.language_choice = self.language_var.get()
            in_label = self.input_choice.get()
            out_label = self.output_choice.get()
            self.selected_input_id = self.input_map.get(in_label)
            self.selected_output_id = self.output_map.get(out_label)
            sd.default.device = (self.selected_input_id, self.selected_output_id)

            self.recording = True
            if self.stream is None:
                self.stream = sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                                                channels=1, callback=self.callback)
                self.stream.start()
            else:
                self.stream.start()
            self.status_label.config(text=f"🎤 Recording from: {in_label} with model: {self.engine.language_choice}")
        except Exception as e:
            self.status_label.config(text=f"Error starting recording: {e}")

    def pause_recording(self):
        self.recording = False
        if self.stream:
            self.stream.stop()
        self.status_label.config(text="⏸ Paused. Resume when ready.")
        if self.recorded_audio:
            try:
                text = self.engine.recognize_audio(self.recorded_audio)
                print(f"Raw Question : {text}")
                if text:
                    self.process_question(text)
            except Exception as e:
                self.status_label.config(text=f"Recognition error: {e}")
        self.recorded_audio = b""

    def submit_typed_question(self):
        self.text_area.delete("1.0", tk.END)
        typed = self.manual_text.get("1.0", tk.END).strip()
        if typed:
            self.process_question(typed)
        else:
            self.status_label.config(text="⚠️ Please type a question first.")

    def process_question(self, text):
        self.status_label.config(text="🛠 Refining...")

        def refine_and_ask():
            refined = text
            # self.engine.refine_question(text)
            # print(f"Refined Question : {refined}")
            answer = self.engine.ask_ai(refined)
            q_num = self.engine.next_question_number()
            self.update_gui(q_num, refined, answer)
            self.engine.log_session(refined, answer)
            self.status_label.config(text="Answered...")

        threading.Thread(target=refine_and_ask, daemon=True).start()

    def callback(self, indata, frames, time, status):
        if self.recording:
            self.recorded_audio += bytes(indata)

    def update_gui(self, q_num, question, answer):
        KEY_TERMS = ["KNN", "confusion matrix", "gradient descent", "SVM", "regression",
                     "accuracy", "precision", "recall", "f1 score", "log loss", "AUC",
                     "overfitting", "underfitting", "neural network", "epoch", "loss function",
                     "PCA", "ROC", "decision tree"]

        self.text_area.insert(tk.END, "", "paragraph")
        self.text_area.insert(tk.END, f"💬 Q{q_num}: ", ("bold", "paragraph"))
        self.text_area.insert(tk.END, question + "\n", "paragraph")
        start_index = self.text_area.index(tk.END)
        self.text_area.insert(tk.END, f"🤖 Answer: ", ("bold", "paragraph"))
        self.text_area.insert(tk.END, answer + "\n", "paragraph")

        # self.manual_text.insert(tk.END, question + "\n", "paragraph")

        for term in KEY_TERMS:
            idx = self.text_area.search(term, start_index, tk.END, nocase=True)
            while idx:
                end_idx = f"{idx}+{len(term)}c"
                self.text_area.tag_add("bold", idx, end_idx)
                idx = self.text_area.search(term, end_idx, tk.END, nocase=True)


        self.log_to_file(question, answer)

    def log_to_file(self, question, answer):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("session_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n[{timestamp}]\nQ: {question}\nA: {answer}\n" + "-" * 50 + "\n")

    def run(self):
        self.window.mainloop()

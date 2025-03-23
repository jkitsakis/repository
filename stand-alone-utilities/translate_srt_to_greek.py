import os
import re
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# === CONFIG ===
# input_srt_path = "el-cuento-de-las-comadrejas-2019-hdrip-doktor.srt"
# output_srt_path = "el-cuento-de-las-comadrejas-2019-hdrip-doktor_translated_gr.srt"

# ====== GUI: Select Video File ======
def select_subtitle_file():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a subtitle file",
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv")]
    )
    return Path(file_path) if file_path else None


def translate_subtitle(subtitle_path):
    # === STEP 1: Load the SRT file ===
    with open(subtitle_path, "r", encoding="utf-8") as f:
        srt_content = f.read()

    # === STEP 2: Parse SRT Blocks ===
    blocks = re.findall(r"(\d+)\n([\d:,]+ --> [\d:,]+)\n(.+?)(?=\n\n|\Z)", srt_content, re.DOTALL)

    # === STEP 3: Translate each block's text ===
    translator = GoogleTranslator(source='auto', target='el')
    translated_blocks = []

    for index, timecode, text in blocks:
        lines = text.strip().split('\n')
        translated_lines = []
        for line in lines:
            try:
                translated_line = translator.translate(line.strip())
            except Exception:
                translated_line = "[Translation Error]"
            translated_lines.append(translated_line)
        translated_text = '\n'.join(translated_lines)
        block = f"{index}\n{timecode}\n{translated_text}\n"
        translated_blocks.append(block)

    # === STEP 4: Write new SRT file ===
    output_path = subtitle_path.with_suffix('.el.srt')
    with open(subtitle_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(translated_blocks))

    print(f"✅ Translation complete! File saved as: {subtitle_path}")


# ====== Main Application Entry ======
def main():
    subtitle_path = select_subtitle_file()
    if not subtitle_path:
        print("❌ No file selected.")
        return

    print(f"subtitle Path: {subtitle_path}")
    # Set working directory to video location
    os.chdir(subtitle_path.parent)


    translate_subtitle(subtitle_path)


if __name__ == "__main__":
    main()
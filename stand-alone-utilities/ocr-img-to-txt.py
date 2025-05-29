import time
from PIL import ImageGrab
import pyperclip
import easyocr
import numpy as np
import importlib.resources as resources
import os
from hashlib import md5

def image_to_hash(image):
    return md5(np.array(image).tobytes()).hexdigest()

def extract_text_from_clipboard_image(previous_hash=None):
    try:
        image = ImageGrab.grabclipboard()
        if image is None:
            return None, previous_hash

        image_hash = image_to_hash(image)
        if image_hash == previous_hash:
            return None, previous_hash

        image_np = np.array(image)

        # Check supported languages
        lang_dir = resources.files('easyocr.character')
        langs = [f.name.replace('_char.txt', '') for f in lang_dir.iterdir() if f.name.endswith('_char.txt')]
        supported_langs = ['en']
        # if 'gre' in langs or 'el' in langs:
        #     supported_langs.append('el')

        reader = easyocr.Reader(supported_langs)
        result = reader.readtext(image_np)
        extracted_text = " ".join([text[1] for text in result])

        print("📝 Extracted text:", extracted_text)
        pyperclip.copy(extracted_text)
        print("✅ Text copied to clipboard.")
        return extracted_text, image_hash

    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None, previous_hash

if __name__ == "__main__":
    print("📋 Waiting for new clipboard images... (Press Ctrl+C to stop)\n")
    last_hash = None
    while True:
        text, last_hash = extract_text_from_clipboard_image(previous_hash=last_hash)
        if text:
            print("🔁 Waiting for the next new image...\n")
        time.sleep(1)  # Check every 1 second

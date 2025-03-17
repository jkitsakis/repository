import pytesseract
from PIL import ImageGrab
import pyperclip
import easyocr
import numpy as np


# Ensure pytesseract points to the tesseract executable if not in PATH
# Example for Windows: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_clipboard_image():
    # Load image from clipboard
    try:
        # Capture the image from clipboard
        image = ImageGrab.grabclipboard()

        if image is not None:
            # Convert PIL image to numpy array
            image_np = np.array(image)

            # Extract text using easyocr
            reader = easyocr.Reader(['en'])  # 'en' for English language

            # Read text from the image
            result = reader.readtext(image_np)

            # Extract and print text
            extracted_text = " ".join([text[1] for text in result])
            print("Extracted text:", extracted_text)

            # Copy text to clipboard
            pyperclip.copy(extracted_text)
            print("Extracted text is copied to clipboard.")
            return extracted_text
        else:
            print("No image found in clipboard.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    extracted_text = extract_text_from_clipboard_image()

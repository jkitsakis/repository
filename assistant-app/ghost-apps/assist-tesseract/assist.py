import numpy as np
import pyautogui
from PIL import Image
import pytesseract
from openai import OpenAI
import sys
import datetime
from plyer import notification
from pynput import mouse
import threading
from send_email import EmailSender

# Your OpenAI API Key
api_key = ''
client = OpenAI(api_key=api_key)

prompt= (f"You are an expert in Microsoft Azure AI Fundamentals (AI-900) certification exam and Azure Machine Learning Studio. "
         f"I will provide you with a screenshot containing  multiple-choice question. "
         f"- Identify the **question and possible answers options** to choose from, related to Microsoft Azure AI Fundamentals (AI-900). "
         f"- Please respond **only the correct answer option(s)**, nothing else. Do not include any explanations or extra text."
         f"- If the question asks to match items, please respond with the matched pairs. Only provide the matches, no explanations"
         f"- Please answer the following question **USING ONLY** the content from these study resource links and their sublinks:"
         f"-- https://learn.microsoft.com/training/paths/get-started-with-artificial-intelligence-on-azure/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/training/paths/create-no-code-predictive-models-azure-machine-learning/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/training/paths/explore-computer-vision-microsoft-azure/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/training/paths/explore-natural-language-processing/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/training/paths/explore-fundamentals-of-decision-support/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/training/paths/explore-fundamentals-of-knowledge-mining/?WT_mc_id=academic-88268-abartolo"         
         f"-- https://learn.microsoft.com/azure/machine-learning/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/cognitive-services/computer-vision/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/architecture/data-guide/technology-choices/natural-language-processing?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/cognitive-services/speech-service/speech-translation?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/cognitive-services/luis/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/cognitive-services/speech-service/index-speech-to-text?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/cognitive-services/anomaly-detector/?WT_mc_id=academic-88268-abartolo"
         f"-- https://learn.microsoft.com/azure/bot-service/?WT_mc_id=academic-88268-abartolo&view=azure-bot-service-4.0"
         )

def log(text):
    with open("assist.log", "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {text}\n")



def process_screenshot():
    log("processing screenshot...")
    try:
        # Take screenshot (returns PIL Image)
        screenshot = pyautogui.screenshot()

        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(screenshot, config=custom_config)

        if text.strip() == "":
            log("No text detected in screenshot!")
            print("No text detected in screenshot!")
            return

        # pattern = r"Next .\|(.+)"  # Text after Next | Button
        # match = re.search(pattern, text, re.DOTALL)
        # if match:
        #     question = match.group(1).strip()
        # else:

        #     question = text

        question = text
        print(f"Question :\n{question}")
        log(f"Question :\n{question}")
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ],
            temperature=0,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response.choices[0].message.content.strip()
        print(answer)
        log(f"Answer:\n{answer}\n{'-' * 40}")
        EmailSender.send_email("AI-900 Question", f"Question: \n {question}" + f"\n \n Answer: \n {answer}")
    except Exception as e:
        log(f"Error in process_screenshot: {e}")
        print(f"Error in process_screenshot: {e}")


def on_click(x, y, button, pressed):
    if pressed and (button == mouse.Button.middle or button == mouse.Button.right):
        print(f"Mouse  button pressed at ({x}, {y})")
        threading.Thread(target=process_screenshot, daemon=True).start()

def main():
    log("Ready!!! Listening for mouse wheel scroll...")
    notification.notify(
        title="Assistant",
        message="App is running",
        timeout=5
    )

    listener = mouse.Listener(on_click=on_click)
    listener.start()

    try:
        listener.join()
    except KeyboardInterrupt:
        print("Exiting...")
        log("TutorAssistant exiting...")
        listener.stop()
        sys.exit(0)


if __name__ == "__main__":
    main()


from flask import Flask, request, jsonify, render_template
import subprocess
import requests
import time

app = Flask(__name__)

OLLAMA_ENDPOINT = "http://ollama:11434/api/generate"
OLLAMA_MODEL = "llama3"

def wait_for_ollama(timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            res = requests.get(OLLAMA_ENDPOINT.replace("/api/generate", "/"))
            if res.status_code == 200:
                print("✅ Ollama is up!")
                return True
        except requests.exceptions.RequestException:
            pass
        print("⏳ Waiting for Ollama to be available...")
        time.sleep(1)
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    if not wait_for_ollama():
        return jsonify({"error": "Ollama service not available"}), 503

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": question,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to communicate with Ollama", "details": str(e)}), 500

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files.get('audio')
    if not audio:
        return jsonify({"error": "No audio uploaded"}), 400

    audio.save("temp.wav")
    result = subprocess.run(["whisper", "temp.wav", "--model", "base", "--language", "en", "--output_format", "txt"],
                            capture_output=True, text=True)
    if result.returncode != 0:
        return jsonify({"error": "Transcription failed"}), 500

    with open("temp.txt", "r") as f:
        transcript = f.read()
    return jsonify({"transcript": transcript})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

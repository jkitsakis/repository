import logging
from flask import Flask, render_template, request, jsonify
import os, requests, psutil

app = Flask(__name__)

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
log = logging.getLogger(__name__)

# --- Environment ---
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
WHISPER_URL = os.getenv("WHISPER_URL", "http://localhost:6000")

# --- Supported models ---
MODELS = {
    "codellama": "CodeLLaMA",
    "mistral": "Mistral",
    "llama2": "LLaMA2",
    "gemma": "Gemma"
}

# --- Auto model selection ---
def pick_model(question):
    q = question.lower()
    if any(k in q for k in ["java", "spring", "oracle", "code", "api", "controller"]):
        return "codellama"
    elif any(k in q for k in ["logic", "reason", "why", "compare"]):
        return "mistral"
    elif any(k in q for k in ["ethics", "human", "philosophy"]):
        return "llama2"
    return "mistral"

# --- Call model ---
def query_model(prompt, model):
    log.info(f">> Calling model: {model}")
    response = requests.post(f"{OLLAMA_URL}/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    data = response.json()
    output = data.get("response", "").strip()

    if not output:
        log.warning("⚠️ Empty response from model")
        output = "[No response generated. Check your prompt or model.]"

    return output


# --- Home page ---
@app.route("/")
def home():
    return render_template("index.html", models=MODELS)

# --- Handle text input form ---
@app.route("/text_question", methods=["POST"])
def text_question():
    question = request.form.get("question", "").strip()
    model = request.form.get("model", "auto").strip()

    log.info(f">> Text question received: {question}")
    if model == "auto":
        model = pick_model(question)
        log.info(f">> Auto-selected model: {model}")

    prompt = f"""You are a senior backend engineer with deep knowledge of Java, Spring, and Oracle DB.

Question:
{question}

Answer:
"""
    try:
        log.info(f">> Prompt: {prompt}")
        answer = query_model(prompt, model)
    except Exception as e:
        log.error("❌ Error during model query", exc_info=True)
        answer = f"❌ Error: {str(e)}"

    return render_template("index.html", question=question, answer=answer, model=model, models=MODELS)

# --- Handle audio input form ---
@app.route("/audio_question", methods=["POST"])
def audio_question():
    audio = request.files['audio']
    log.info(">> Audio question received. Sending to Whisper service...")

    whisper_response = requests.post(f"{WHISPER_URL}/transcribe", files={"audio": audio})
    question = whisper_response.json().get("text", "")
    model = pick_model(question)

    log.info(f">> Transcribed question: {question}")
    log.info(f">> Auto-selected model: {model}")

    prompt = f"""You are a senior backend engineer with deep knowledge of Java, Spring, and Oracle DB.

Question:
{question}

Answer:
"""
    try:
        answer = query_model(prompt, model)
    except Exception as e:
        log.error("❌ Error during model query from audio", exc_info=True)
        answer = f"❌ Error: {str(e)}"

    return render_template("index.html", question=question, answer=answer, model=model, models=MODELS)

# --- System resource info ---
@app.route("/system_status")
def system_status():
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    })

# --- Run app ---
if __name__ == "__main__":
    log.info("✅ Flask running at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, jsonify
from whisper_utils import record_audio, transcribe_audio
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/record_question", methods=["POST"])
def record_question():
    audio_path = record_audio(duration=6)
    question = transcribe_audio(audio_path)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Answer as a Java/Spring/Oracle expert:\n{question}"}]
    )
    answer = response.choices[0].message.content.strip()
    return jsonify({"question": question, "answer": answer})

@app.route("/text_question", methods=["POST"])
def text_question():
    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided."}), 400

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Answer as a Java/Spring/Oracle expert:\n{question}"}]
    )
    answer = response.choices[0].message.content.strip()
    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    print("✅ Starting Flask server on http://0.0.0.0:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)

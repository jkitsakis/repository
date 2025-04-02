from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import tempfile

app = Flask(__name__)
model = WhisperModel("base", compute_type="float32")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files['audio']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio.read())
        tmp_path = tmp.name
    segments, _ = model.transcribe(tmp_path)
    text = " ".join([seg.text for seg in segments])
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)

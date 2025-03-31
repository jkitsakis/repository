from flask import Flask, request, send_file, jsonify
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="🚀 Pandoc API is running!")

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify(error="No file uploaded"), 400

    file = request.files['file']
    input_fmt = request.form.get('from', 'markdown')
    output_fmt = request.form.get('to', 'docx')
    math_option = request.form.get('math', '--mathjax')

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, file.filename)
        output_path = os.path.join(tmpdir, f"output.{output_fmt}")
        file.save(input_path)

        cmd = [
            "pandoc", input_path,
            "-f", input_fmt,
            "-t", output_fmt,
            "-o", output_path
        ]

        if output_fmt == "pdf":
            cmd += ["--pdf-engine=xelatex"]
        elif math_option:
            cmd.append(math_option)

        try:
            subprocess.run(cmd, check=True)
            return send_file(output_path, as_attachment=True)
        except subprocess.CalledProcessError as e:
            return jsonify(error=f"Pandoc failed: {e}"), 500


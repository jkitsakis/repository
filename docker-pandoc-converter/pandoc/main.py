from flask import Flask, request, send_file, jsonify
import subprocess
import tempfile
import os
import logging as log

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="🚀 Pandoc API is running!")

@app.route('/convert', methods=['POST'])
def convert():
    log.info(f'---Converting ...')
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
        elif input_fmt == "csv" and output_fmt == "markdown":
            log.info(f'---Converting {input_fmt} to {output_fmt}')
            math_option = ''
            cmd.append(math_option)
            csv_to_markdown(input_path, output_path)
            return send_file(output_path, as_attachment=True)
        elif math_option:
            cmd.append(math_option)

        #for all cases except csv -> md
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            return jsonify(error=f"Pandoc failed: {e}"), 500

        return send_file(output_path, as_attachment=True)

import csv

def csv_to_markdown(csv_file_path: str, markdown_file_path: str):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [[clean_cell(cell) for cell in row] for row in reader]


    if not rows:
        print("The CSV file is empty.")
        return

    # Determine max width per column
    num_cols = len(rows[0])
    col_widths = [0] * num_cols
    for row in rows:
        for i in range(num_cols):
            if i < len(row):
                col_widths[i] = max(col_widths[i], len(row[i]))

    # Function to format a single row
    def format_row(row):
        return '| ' + ' | '.join(
            row[i].ljust(col_widths[i]) if i < len(row) else ' ' * col_widths[i]
            for i in range(num_cols)
        ) + ' |'

    # Build table
    header = format_row(rows[0])
    separator = '| ' + ' | '.join('-' * col_widths[i] for i in range(num_cols)) + ' |'
    data_rows = [format_row(row) for row in rows[1:]]

    markdown_lines = [header, separator] + data_rows

    # Save to .md file
    with open(markdown_file_path, 'w', encoding='utf-8') as mdfile:
        mdfile.write('\n'.join(markdown_lines))


    print(f"Markdown table saved to: {markdown_file_path}")

def clean_cell(cell):
    return cell.strip().replace('\t', ' ').replace('\n', ' ').replace('\r', '')
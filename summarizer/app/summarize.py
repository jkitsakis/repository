import os
import textwrap
import torch
import math
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from docx import Document
import PyPDF2
import markdown

# ✅ Load a Better Model for General Summarization
MODEL_NAME = "facebook/bart-large-cnn"  # Better readability
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)

# ✅ Directories
IMPORT_FOLDER = "import"
EXPORT_FOLDER = "export"
MAX_INPUT_LENGTH = 1024  # BART model limit
CHUNK_SIZE = 900  # Below max limit

os.makedirs(EXPORT_FOLDER, exist_ok=True)


# ✅ Read PDF files
def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])


# ✅ Read DOCX files
def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


# ✅ Preprocess Text to Remove Garbage Characters
def clean_text(text):
    text = text.replace("\n", " ")  # Remove newlines
    text = text.replace("<n>", " ")  # Fix weird symbols
    text = " ".join(text.split())  # Normalize spaces
    return text


# ✅ Chunk text efficiently
def chunk_text(text, chunk_size=CHUNK_SIZE):
    return textwrap.wrap(text, width=chunk_size, break_long_words=False, replace_whitespace=False)


# ✅ Summarize with Improved Settings
def summarize_chunk(chunk):
    inputs = tokenizer(chunk, return_tensors="pt", max_length=MAX_INPUT_LENGTH, truncation=True).to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_length=700,
            min_length=250,
            num_beams=6,
            temperature=0.5,
            repetition_penalty=2.0,
            length_penalty=1.0,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)


# ✅ Improved Summarization Pipeline
def summarize_text(text):
    text = clean_text(text)  # Pre-cleaning step
    chunks = chunk_text(text)
    summaries = []

    batch_size = 3  # Adjust for performance
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]

        inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=MAX_INPUT_LENGTH).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=700,
                min_length=250,
                num_beams=6,
                temperature=0.5,
                repetition_penalty=2.0,
                length_penalty=1.0,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        summaries.extend([tokenizer.decode(output, skip_special_tokens=True) for output in outputs])

    return " ".join(summaries)


# ✅ Better Topic Extraction (NER)
def extract_topics(text):
    ner = pipeline("ner")
    topics = ner(text)
    filtered_topics = list(set([t["word"].strip("##") for t in topics if len(t["word"]) > 3]))  # Remove junk
    return ", ".join(filtered_topics) if filtered_topics else "No topics detected"


# ✅ Main Processing
def main():
    files = [file for file in os.listdir(IMPORT_FOLDER) if file.endswith(".docx") or file.endswith(".pdf")]

    print(f"📂 Found files: {files}")

    for filename in files:
        file_path = os.path.join(IMPORT_FOLDER, filename)

        print(f"📖 Reading {filename} ...")
        text = read_pdf(file_path) if filename.endswith(".pdf") else read_docx(file_path)

        print(f"✍️ Summarizing {filename} ...")
        if text.strip():
            summary = summarize_text(text)
            topics = extract_topics(text)

            txt_path = os.path.join(EXPORT_FOLDER, f"{filename}.summary.txt")
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(f"📌 Topics: {topics}\n\n{summary}")

            print(f"✅ Summary saved: {txt_path}")
        else:
            print(f"⚠️ No readable text in: {filename}")

    print("🎉 Done processing all files!")


if __name__ == "__main__":
    main()

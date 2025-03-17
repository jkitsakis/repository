import os
import textwrap
import torch
import multiprocessing
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from docx import Document
import PyPDF2
import markdown

# ✅ Load Model and Tokenizer Directly
MODEL_NAME = "google/bigbird-pegasus-large-arxiv"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device).eval()

# Use torch.compile() for speedup (PyTorch 2.0+)
if torch.__version__ >= "2.0":
    model = torch.compile(model)

# Directories
IMPORT_FOLDER = "import"
EXPORT_FOLDER = "export"
MAX_INPUT_LENGTH = 4096  # BigBird-Pegasus max tokens
CHUNK_SIZE = 3500  # Slightly lower than max

os.makedirs(EXPORT_FOLDER, exist_ok=True)


# Read PDF files
def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])


# Read DOCX files
def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


# Chunk long text
def chunk_text(text, chunk_size=CHUNK_SIZE):
    return textwrap.wrap(text, width=chunk_size, break_long_words=False, replace_whitespace=False)


# **Summarize a single chunk**
def summarize_chunk(chunk):
    inputs = tokenizer(chunk, return_tensors="pt", max_length=MAX_INPUT_LENGTH, truncation=True).to(device)

    with torch.no_grad():
        output = model.generate(**inputs, max_length=200, min_length=50, do_sample=False)

    return tokenizer.decode(output[0], skip_special_tokens=True)


# **Parallelized Summarization**
def summarize_text(text):
    chunks = chunk_text(text)

    # CPU Parallel Processing (for CPU users)
    if device == "cpu":
        with multiprocessing.Pool(processes=min(len(chunks), os.cpu_count())) as pool:
            summaries = pool.map(summarize_chunk, chunks)
    else:
        # GPU Optimized Processing (batch inference)
        summaries = []
        batch_size = 4  # Adjust based on GPU memory
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True,
                               max_length=MAX_INPUT_LENGTH).to(device)

            with torch.no_grad():
                outputs = model.generate(**inputs, max_length=200, min_length=50, do_sample=False)

            summaries.extend([tokenizer.decode(output, skip_special_tokens=True) for output in outputs])

    return "\n".join(summaries)

def main():
    files = [file for file in os.listdir(IMPORT_FOLDER) if file.endswith(".docx") or file.endswith(".pdf")]

    print(f"📂 Found files: {files}")  # Debugging step

    if not files:
        print("⚠️ No files found in the input folder. Ensure .docx or .pdf files exist in 'import/'.")
        return

    for filename in files:
        file_path = os.path.join(IMPORT_FOLDER, filename)
        print(f"🔍 Checking: {file_path}")  # Debugging step

        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue

        print(f"Processing {filename} ...")

        if filename.endswith(".pdf"):
            text = read_pdf(file_path)
        elif filename.endswith(".docx"):
            text = read_docx(file_path)
        else:
            print(f"Skipping unsupported file: {filename}")
            continue

        print(f"Summarizing {filename} ...")
        if text.strip():
            summary = summarize_text(text)

            # Save TXT file
            txt_path = os.path.join(EXPORT_FOLDER, f"{filename}.summary.txt")
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(summary)

            # Save MD file
            md_path = os.path.join(EXPORT_FOLDER, f"{filename}.summary.md")
            with open(md_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown.markdown(summary))

            print(f"✅ Summarized: {filename} → {txt_path}, {md_path}")
        else:
            print(f"⚠️ No readable text in: {filename}")

    print("🎉 Done processing all files in the import folder!")


if __name__ == "__main__":
    main()
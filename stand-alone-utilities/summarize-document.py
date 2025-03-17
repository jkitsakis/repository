import os
from docx import Document
from PyPDF2 import PdfReader
import win32com.client as win32
import tkinter as tk
from tkinter import filedialog

# Function to read .docx file
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Function to read .pdf file
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        full_text = []
        for page in reader.pages:
            full_text.append(page.extract_text())
        return '\n'.join(full_text)

# Function to read .doc file (using Microsoft Word)
def read_doc(file_path):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(file_path)
    full_text = doc.Content.Text
    doc.Close()
    word.Quit()
    return full_text

from transformers import pipeline
import math

# Function to split text into chunks of specified max length
def split_text_into_chunks(text, max_length=1024):
    words = text.split()
    chunks = []
    chunk = []
    length = 0

    for word in words:
        length += len(word) + 1  # +1 for space between words
        if length > max_length:
            chunks.append(" ".join(chunk))
            chunk = [word]
            length = len(word) + 1
        else:
            chunk.append(word)

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

# Function to summarize text
def summarize_text(text):
    model_name = "facebook/bart-large-cnn"  # Specify the summarization model
    summarizer = pipeline("summarization", model=model_name)

    # Split text into chunks to avoid exceeding token limit
    chunks = split_text_into_chunks(text, max_length=1024)

    # Summarize each chunk
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Combine export into one final summary
    return " ".join(summaries)



# Function to open file dialog and select document
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[("Word Documents", "*.docx"), ("PDF Files", "*.pdf"), ("Word 97-2003 Documents", "*.doc")]
    )
    return file_path

# Main function to handle document input and export summary
def main():
    # Open file dialog to select a document
    file_path = select_file()
    if file_path:
        # Summarize the selected document
        summary = summarize_document(file_path)
        print("Summary:\n", summary)
    else:
        print("No file selected.")

# Function to summarize document based on file type
def summarize_document(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    # Read the document based on extension
    if file_extension == '.docx':
        text = read_docx(file_path)
    elif file_extension == '.pdf':
        text = read_pdf(file_path)
    elif file_extension == '.doc':
        text = read_doc(file_path)
    else:
        return "Unsupported file format."

    # Generate summary
    summary = summarize_text(text)

    return summary

# Entry point to run the script
if __name__ == "__main__":
    main()

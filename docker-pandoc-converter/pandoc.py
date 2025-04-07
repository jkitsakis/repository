import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import requests
import os

API_URL = "http://localhost:5000/convert"

OPERATIONS = {
    "Markdown → Word (.docx)": ("markdown", "docx"),
    "Markdown → PDF": ("markdown", "pdf"),
    "Markdown → LaTeX": ("markdown", "latex"),
    "Markdown → HTML": ("markdown", "html"),
    "DOCX → PDF": ("docx", "pdf"),
    "LaTeX → PDF": ("latex", "pdf"),
    "HTML → Word (.docx)": ("html", "docx"),
    "EPUB → PDF": ("epub", "pdf"),
    "CSV → Markdown": ("csv", "markdown")
}

def convert_file():
    filepath = file_path.get()
    if not os.path.exists(filepath):
        messagebox.showerror("Error", "File not found.")
        return

    from_fmt, to_fmt = OPERATIONS[operation_var.get()]
    math_option = math_var.get()

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            files = {'file': (os.path.basename(filepath), f)}
            data = {
                'from': from_fmt,
                'to': to_fmt,
                'math': math_option
            }
            response = requests.post(API_URL, files=files, data=data)

        if response.status_code == 200:
            out_filename = os.path.splitext(filepath)[0] + f".{to_fmt}"
            with open(out_filename, 'wb') as out_file:
                out_file.write(response.content)
            messagebox.showinfo("Success", f"✅ Converted to: {out_filename}")
        else:
            messagebox.showerror("Conversion Failed", response.json().get('error', 'Unknown error'))

    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    selected = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if selected:
        file_path.set(selected)

# UI Setup
root = tk.Tk()
root.title("Pandoc Converter GUI")

file_path = tk.StringVar()
operation_var = tk.StringVar(value=list(OPERATIONS.keys())[0])
math_var = tk.StringVar(value="--mathjax")

tk.Label(root, text="Input File:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=file_path, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

tk.Label(root, text="Operation:").grid(row=1, column=0, sticky="e")
ttk.Combobox(root, textvariable=operation_var, values=list(OPERATIONS.keys()), width=45).grid(row=1, column=1, sticky="w")

tk.Label(root, text="Math Engine:").grid(row=2, column=0, sticky="e")
ttk.Combobox(root, textvariable=math_var, values=["--mathjax", "--mathml", ""]).grid(row=2, column=1, sticky="w")

tk.Button(root, text="Convert", command=convert_file, bg="#4CAF50", fg="white").grid(row=3, column=1, pady=10)

root.mainloop()

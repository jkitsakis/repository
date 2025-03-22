import os
import time
import tkinter as tk
from tkinter import filedialog


def get_creation_date(filepath):
    try:
        # On Windows, this gives the creation date
        timestamp = os.path.getctime(filepath)
    except AttributeError:
        # On Unix-like systems, fallback to last modification time
        timestamp = os.path.getmtime(filepath)
    return time.strftime("%Y-%m-%d", time.localtime(timestamp))


def rename_files_in_folder(folder_path, base_name="file", start_index=1, padding=3):
    files = sorted(os.listdir(folder_path))
    index = start_index

    for filename in files:
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1]
            creation_date = get_creation_date(old_path)
            new_name = f"{base_name}_{creation_date}_{str(index).zfill(padding)}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
            index += 1


def select_folder_and_rename():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_selected = filedialog.askdirectory(title="Select Folder to Rename Files")

    if folder_selected:
        base_name = input("Enter base name for files (e.g., 'image'): ").strip()
        start_index = int(input("Enter starting number (e.g., 1): ").strip())
        padding = int(input("Enter number padding (e.g., 3 for 001): ").strip())
        rename_files_in_folder(folder_selected, base_name, start_index, padding)
    else:
        print("No folder selected.")


if __name__ == "__main__":
    select_folder_and_rename()

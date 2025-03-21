import os
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from subliminal import download_best_subtitles, save_subtitles, region
from subliminal.video import Video
from babelfish import Language

# ====== OpenSubtitles.com API CONFIG ======
OPENSUBTITLES_API_KEY = 'Yf9MrNUAFePUaDBYribuyN08ZmI3dayp'
OPENSUBTITLES_USERNAME = 'jokit73@yahoo.com'
OPENSUBTITLES_PASSWORD = 'opensubtitlesJokit73'

# ====== GUI: Select Video File ======
def select_video_file():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a video file",
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv")]
    )
    return Path(file_path) if file_path else None

# ====== Ask User: Which Method to Use ======
def choose_method():
    return messagebox.askyesno(
        "Subtitle Method",
        "Use Subliminal (OpenSubtitles.org)?\n\nYes = Subliminal (.org XML-RPC)\nNo = OpenSubtitles.com API v1"
    )

# ====== Method 1: Subliminal (.org XML-RPC) ======
def download_with_subliminal(video_path):
    print(f"[Subliminal / OpenSubtitles.org] Downloading Greek subtitles for {video_path.name}...")
    region.configure('dogpile.cache.memory')

    video = Video.fromname(video_path.name)
    video.name = video_path.name  # Match actual filename for better results

    subtitles = download_best_subtitles([video], {Language('ell')})

    if subtitles.get(video):
        save_subtitles(video, subtitles[video])
        print("✅ Greek subtitle downloaded using Subliminal (.org).")
    else:
        print("❌ No Greek subtitle found via Subliminal.")

# ====== Method 2: OpenSubtitles.com REST API v1 ======
def get_opensubtitles_token():
    url = "https://api.opensubtitles.com/api/v1/login"
    headers = {"Api-Key": OPENSUBTITLES_API_KEY}
    data = {"username": OPENSUBTITLES_USERNAME, "password": OPENSUBTITLES_PASSWORD}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['token']

def search_opensubtitles(token, query):
    url = "https://api.opensubtitles.com/api/v1/subtitles"
    headers = {
        "Authorization": f"Bearer {token}",
        "Api-Key": OPENSUBTITLES_API_KEY
    }
    params = {
        "languages": "ell",
        "query": query,
        "order_by": "download_count",
        "order_direction": "desc"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['data']

def download_opensubtitles(token, file_id, output_path):
    url = "https://api.opensubtitles.com/api/v1/download"
    headers = {
        "Authorization": f"Bearer {token}",
        "Api-Key": OPENSUBTITLES_API_KEY
    }
    response = requests.post(url, headers=headers, json={"file_id": file_id})
    response.raise_for_status()
    download_url = response.json()['link']

    subtitle_response = requests.get(download_url)
    subtitle_response.raise_for_status()

    with open(output_path, 'wb') as f:
        f.write(subtitle_response.content)

    print(f"✅ Greek subtitle saved to {output_path.name} using OpenSubtitles.com API.")

def download_with_opensubtitles_api(video_path):
    print(f"[OpenSubtitles.com API v1] Downloading Greek subtitles for {video_path.name}...")
    try:
        token = get_opensubtitles_token()
        results = search_opensubtitles(token, video_path.stem)
        if not results:
            print("❌ No Greek subtitles found on OpenSubtitles.com.")
            return

        best_file = results[0]['attributes']['files'][0]
        output_path = video_path.with_suffix('.srt')
        download_opensubtitles(token, best_file['file_id'], output_path)

    except requests.HTTPError as e:
        print(f"❌ OpenSubtitles.com API error: {e}")

# ====== Main Application Entry ======
def main():
    video_path = select_video_file()
    if not video_path:
        print("❌ No file selected.")
        return

    # Set working directory to video location
    os.chdir(video_path.parent)

    # Ask user which backend to use
    if choose_method():
        download_with_subliminal(video_path)
    else:
        download_with_opensubtitles_api(video_path)

if __name__ == "__main__":
    main()

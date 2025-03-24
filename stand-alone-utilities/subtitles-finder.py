import os

import chardet
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from subliminal import download_best_subtitles, save_subtitles, region
from babelfish import Language
from guessit import guessit
from subliminal.video import Episode, Movie

# ====== OpenSubtitles.com API CONFIG ======
OPENSUBTITLES_API_KEY = 'Yf9MrNUAFePUaDBYribuyN08ZmI3dayp'
OPENSUBTITLES_USERNAME = 'jokit'
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

    guess = guessit(video_path.name)
    print("🔍 Parsed metadata:", guess)

    try:
        if guess.get("type") == "episode":
            if 'episode' not in guess:
                print("⚠️ Cannot fetch subtitles: no episode number in filename.")
                return
            video = Episode.fromguess(video_path.name, guess)
        elif guess.get("type") == "movie":
            video = Movie.fromguess(video_path.name, guess)
        else:
            print("❌ Could not determine if the video is a movie or episode.")
            return

        subtitles = download_best_subtitles(
            [video],
            {Language('ell')},
            providers=['opensubtitles', 'addic7ed', 'podnapisi', 'tvsubtitles']
        )

        if subtitles.get(video):
            subtitle_list = subtitles[video]
            save_subtitles(video, subtitle_list)

            # Log which provider was used
            for subtitle in subtitle_list:
                provider = getattr(subtitle, 'provider_name', 'unknown')
                print(f"✅ Subtitle provided by: {provider}  | Language: {subtitle.language}")

            # Force UTF-8 conversion
            # Find .el.srt and rename it to match the video filename
            original_sub_path = video_path.with_name(video_path.stem + '.el.srt')
            final_sub_path = video_path.with_suffix('.srt')

            if original_sub_path.exists():
                os.rename(original_sub_path, final_sub_path)
                print(f"📝 Renamed subtitle to match video: {final_sub_path.name}")
                convert_subtitle_to_utf8(final_sub_path)
            else:
                print("⚠️ Expected .el.srt file not found. Subtitle may not have been saved.")

        else:
            print("No Greek subtitle found via any provider.")
            return

    except ValueError as ve:
        print(f"❌ Subliminal error: {ve}")



# ====== Method 2: OpenSubtitles.com REST API v1 ======
def get_opensubtitles_token():
    url = "https://api.opensubtitles.com/api/v1/login"
    headers = {"Api-Key": OPENSUBTITLES_API_KEY}
    data = {"username": OPENSUBTITLES_USERNAME, "password": OPENSUBTITLES_PASSWORD}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['token']

def search_opensubtitles(token, query, language):
    url = "https://api.opensubtitles.com/api/v1/subtitles"
    headers = {
        "Authorization": f"Bearer {token}",
        "Api-Key": OPENSUBTITLES_API_KEY
    }
    params = {
        "languages": language,
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

    # Detect encoding
    detected = chardet.detect(subtitle_response.content)
    text = subtitle_response.content.decode(detected['encoding'], errors='replace')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"✅ Greek subtitle saved to {output_path.name} using OpenSubtitles.com API.")

def download_with_opensubtitles_api(video_path, language):
    print(f"[OpenSubtitles.com API v1] Downloading Greek subtitles for {video_path.name}...")
    try:
        token = get_opensubtitles_token()
        results = search_opensubtitles(token, video_path.stem, language)

        if not results:
            print(f"No subtitles found on OpenSubtitles.com for {language}")
            return

        best_file = results[0]['attributes']['files'][0]
        suffix = '.srt' if language=='el' else f'{language}.srt'
        output_path = video_path.with_suffix(suffix)
        download_opensubtitles(token, best_file['file_id'], output_path)
        return True

    except requests.HTTPError as e:
        print(f"OpenSubtitles.com API error: {e}")


def convert_subtitle_to_utf8(subtitle_path):
    try:
        with open(subtitle_path, 'rb') as f:
            raw_data = f.read()

        # Try to decode as best as possible
        try:
            text = raw_data.decode('utf-8')
        except UnicodeDecodeError:
            text = raw_data.decode('iso-8859-7')  # Greek fallback

        with open(subtitle_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"📝 Converted subtitle to UTF-8: {subtitle_path.name}")

    except Exception as e:
        print(f"⚠️ Could not convert {subtitle_path.name} to UTF-8: {e}")


# ====== Main Application Entry ======
def main():
    video_path = select_video_file()
    if not video_path:
        print("❌ No file selected.")
        return

    print(f"Video Path: {video_path}")
    # Set working directory to video location
    os.chdir(video_path.parent)

    if not download_with_opensubtitles_api(video_path, 'el'):
        if not download_with_subliminal(video_path):
           download_with_opensubtitles_api(video_path, 'en')


if __name__ == "__main__":
    main()

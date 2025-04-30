
# 🎬 Transcriber App Setup Guide

This app lets you:
- Select MP4 videos
- Transcribe audio using whisper.cpp (CPU-optimized)
- Perform speaker diarization with resemblyzer
- Export transcripts with speaker labels

---

## 📦 Folder Structure

```
transcriber-app/
├── run_transcription.py
├── run.sh
├── setup.sh
├── requirements.txt
├── audio/
├── output/
├── models/
├── input/
├── whisper.cpp/ (clone and build separately)
```

---

# 🐧 Kubuntu / Linux Native Setup

## 1. Install System Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg build-essential git cmake
```

## 2. Clone and Build whisper.cpp
```bash
cd ~/workspace/transcriber-app
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make
cd ..
```

## 3. Download and Quantize Whisper Model
```bash
./setup.sh
```

## 4. Launch Interactive Menu
```bash
./run.sh
```
You can:
- Create and activate .venv
- Install Python requirements
- Run the transcriber
- Reset the venv

---

# 🪟 Windows WSL (Ubuntu) Setup

Copy folder WSL->Winodws : 
cd ~/workspace/transcriber-app
rsync -av --exclude='.venv' --exclude='whisper.cpp' --exclude='input' --exclude='audio' ./ /mnt/c/Workspace/My-Applications/GitHub/repository/transcriber-app/


## 1. Avoid /mnt/c/ folders
WSL cannot properly chmod files inside Windows-mounted drives.
**Move the project to a Linux-native folder**:

```wsl ubntu bash
cd ~
mkdir -p workspace
cp -r /mnt/c/Workspace/My-Applications/GitHub/repository/transcriber-app workspace/
cd workspace/transcriber-app/whisper.cpp

```
## 1.1 install python env
```
sudo apt update
sudo apt install python3-venv build-essential python3-dev python3-tk ffmpeg cmake
```

## 2. Make Scripts Executable
```bash
chmod +x setup.sh run.sh
```

## 3. Build whisper.cpp
```bash
cd whisper.cpp
make
cd ..
```

## 4. Download and Quantize Model
```bash
./setup.sh
```

## 5. Launch the Transcriber Menu
```bash
./run.sh
```

---

# ⚙️ Menu Options Explained

| Option | Action                                  |
|:-------|:----------------------------------------|
| `1`    | Run the transcriber app (select MP4)     |
| `2`    | Install Python requirements             |
| `3`    | Create and activate Python `.venv`       |
| `4`    | Reset the Python `.venv` completely      |
| `5`    | Exit the menu                           |

---

# 📂 Output Location

- Transcribed text: `output/transcript.txt`
- WAV converted audio: `audio/audio.wav`
- Speaker-diarized transcript with timestamps

---

# 🧠 Tips
- Always activate `.venv` before running manually:
  ```bash
  source .venv/bin/activate
  ```
- Make sure `ffmpeg` is installed properly.
- Run all commands inside Linux-native WSL folders, not `/mnt/c/`.

---

# 📢 Important Changes (whisper.cpp 2025)
- The executable is now `whisper-cli` (not `main`)
- Binaries are located in `whisper.cpp/build/bin/`

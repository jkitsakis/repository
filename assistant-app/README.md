
# 🎤 Tutor Assistant - Full Setup Guide

---

## 1. Overview
This application provides live speech recognition (via Vosk) and smart AI responses (via OpenAI).  
It can run on **Windows**, **Ubuntu Linux**, or **WSL Ubuntu** (Windows Subsystem for Linux).

---

## 2. Windows Setup

### 2.1 Install Python
- Download and install Python 3.10+ from https://www.python.org/downloads/
- During install: ✅ Check "Add Python to PATH"

### 2.2 Create Virtual Environment
Open Command Prompt (CMD) in your project folder:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 2.3 Install Libraries
```bash
pip install vosk openai sounddevice pygame
```

### 2.4 Install Audio Tools
- **VB-Cable** (Virtual Audio Cable): https://vb-audio.com/Cable/
- **VoiceMeeter** (Optional, more advanced audio control): https://vb-audio.com/Voicemeeter/

### 2.5 Configure Audio
- Enable **Stereo Mix** from Windows Sound settings if available.
- If Stereo Mix is not available:
  - Install **VB-Cable** and set it as the default Input/Output.
- In **VoiceMeeter** (if installed): Route microphone and app audio properly to VB-Cable Input.

---

## 3. Ubuntu Setup (Native Linux)

### 3.1 Install Python and Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 3.2 Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.3 Install Required Python Libraries
```bash
pip install vosk openai sounddevice pygame
```

### 3.4 Install Audio Tools
```bash
sudo apt install pavucontrol pulseaudio
```

### 3.5 Configure Audio
- Open `pavucontrol`
- Under the **Recording** tab, select "Monitor of Output" or "Loopback" device as the recording source.

---

## 4. WSL Ubuntu Setup (Windows Subsystem for Linux)

### 4.1 Install Python inside WSL
Same commands as Ubuntu above.

### 4.2 Install an X Server for GUI
- Install **VcXsrv** (free) from https://sourceforge.net/projects/vcxsrv/
- Run `XLaunch` -> allow public connections -> no window manager.
- In WSL Terminal:

```bash
export DISPLAY=:0
```

✅ This allows Tkinter windows (GUI) to appear.

### 4.3 Setup Audio in WSL (Optional, Advanced)
- Install PulseAudio on Windows separately.
- Setup TCP forwarding manually.
- **Warning**: Native microphone access from WSL is complex and not fully reliable.

---

## 5. Running the Application

### 5.1 Windows
- Double-click `start_assistant.bat`
or run manually:
```bash
python start_assistant.py --apikey="your-openai-key" --defaultlang="Greek" --modelfolder="model"
```

### 5.2 Ubuntu / WSL
Make the script executable:

```bash
chmod +x start_assistant.sh
```

Then run:

```bash
./start_assistant.sh
```

---

## 6. Important Notes

- Models for Vosk should be placed inside a `/model/` folder.
- Make sure you have:
  - `vosk-model-small-en-us-0.15`
  - `vosk-model-el-gr-0.7`
- Start sounds (`start.wav` and `stop.wav`) should be placed inside a `/sounds/` folder if your project uses sounds.

---

## 7. Troubleshooting

| Problem | Solution |
|:--------|:---------|
| No input device detected | Check Stereo Mix or VB-Cable input device |
| Tkinter window not showing in WSL | Use `VcXsrv`, set `export DISPLAY=:0` |
| Mic not working in WSL | Configure PulseAudio TCP server (advanced) |
| Python packages missing | Activate `.venv` and install requirements again |
| Permission denied (Linux) | Run `chmod +x start_assistant.sh` first |

---

# 🎯 You are now ready to use the Tutor Assistant!

Enjoy learning with AI! 🚀

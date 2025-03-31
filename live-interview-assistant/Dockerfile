FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (including PortAudio)
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    libavdevice-dev \
    libavfilter-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY app/ /app/
RUN pip install --upgrade pip
RUN pip install flask openai faster-whisper pydub sounddevice scipy numpy

EXPOSE 5000

CMD ["python", "main.py"]

FROM python:3.11

WORKDIR /app

# Install ffmpeg and dependencies
RUN apt-get update
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    libsndfile1 \
    libportaudio2 \
    libavcodec-extra \
    python3-dev \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*
COPY app/requirements.txt .
COPY app/transcriber.py .

RUN pip install --upgrade pip setuptools wheel
RUN pip install git+https://github.com/openai/whisper.git@517a43ecd132a2089d85f4ebc044728a71d49f6e

RUN pip install --no-cache-dir -r requirements.txt





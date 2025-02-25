FROM python:latest

WORKDIR /app

# Install ffmpeg and dependencies
RUN apt-get update && apt-get install -y  build-essential ffmpeg  libsndfile1 && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
COPY app/transcriber.py .
	
# Expose a volume for MP4 input and output folder
# VOLUME ["/app/input", "/app/output"]

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the script
# CMD ["python", "transcriber.py"]

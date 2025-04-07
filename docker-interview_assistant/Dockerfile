
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install git+https://github.com/openai/whisper.git

VOLUME ["/app/whisper_models"]

ENV WHISPER_MODELS_DIR=/app/whisper_models

EXPOSE 5000

CMD ["python", "app.py"]

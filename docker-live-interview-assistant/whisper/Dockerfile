FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y ffmpeg && \
    pip install flask faster-whisper

EXPOSE 6000

CMD ["python", "transcriber.py"]

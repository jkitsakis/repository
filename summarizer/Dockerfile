# Use Python 3.11 slim as the base image
FROM python:3.11

# Install system dependencies required for PyPDF2 and python-docx
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    torch transformers \
    python-docx \
    PyPDF2 \
    markdown

# Copy the Python script to the container
COPY app/summarize.py /app/summarize.py

# Create necessary folders
RUN mkdir -p /app/import /app/export

# Set the entrypoint
# ENTRYPOINT ["python", "/app/summarize.py"]

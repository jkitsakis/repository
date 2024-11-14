# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python script to the container
COPY planner-available.py /app/

# Install dependencies
RUN pip install --no-cache-dir requests

# Set the command to run the Python script
CMD ["python", "planner-available.py"]

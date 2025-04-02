FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask requests psutil

EXPOSE 5000

CMD ["python", "main.py"]

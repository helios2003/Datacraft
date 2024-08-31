FROM python:3.11-slim

WORKDIR /app
RUN pip install fastapi uvicorn

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]


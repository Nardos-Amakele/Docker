FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY model.py .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

RUN python model.py

EXPOSE 5000

CMD ["python", "app.py"]

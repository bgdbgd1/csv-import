FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY models.py .
COPY processors/ ./processors/
COPY import_csv.py .

ENTRYPOINT ["python", "import_csv.py"]
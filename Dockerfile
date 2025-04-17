FROM python:3.10-slim

WORKDIR /app

# Minimal dependencies to avoid bloat
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m spacy download en_core_web_sm

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

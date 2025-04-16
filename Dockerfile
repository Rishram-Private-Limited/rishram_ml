FROM python:3.10-alpine

WORKDIR /app

# Install system dependencies only if needed (e.g., for psycopg2)
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cleanup build dependencies if not needed at runtime
RUN apk del gcc musl-dev linux-headers

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]  # Reduce workers

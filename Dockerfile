FROM python:3.10-alpine

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    g++ \
    make \
    openblas-dev \
    lapack-dev \
    libstdc++

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Remove build tools (keep OpenBLAS)
RUN apk del build-base g++ make

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

FROM python:3.10-alpine

WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    g++ \
    make \
    openblas-dev \
    libstdc++

# Install Python dependencies with optimized build
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --no-build-isolation numpy==1.26.4 scipy==1.13.0 && \
    pip install --no-cache-dir -r requirements.txt

# Clean build dependencies (keep openblas for runtime)
RUN apk del build-base g++ make

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

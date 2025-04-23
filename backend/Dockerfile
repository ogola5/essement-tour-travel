FROM python:3.11-slim

WORKDIR /app

# Install system dependencies first (some Python packages need them)
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/app ./app

EXPOSE 8000

# Explicitly use the full path to uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0-0-0", "--port", "8000"]
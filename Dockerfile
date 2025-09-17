# Use official Python runtime
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements (even if empty)
COPY requirements.txt .

# Install dependencies (none for now)
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the alarm script
CMD ["python", "simple.py"]

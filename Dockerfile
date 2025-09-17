FROM python:3.10-slim

WORKDIR /app

# Copy your code
COPY app.py .
COPY requirements.txt .

# Install Flask
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

# To build and run the Docker container, use the following commands:


# Build the image
#docker build -t numbertowrord .

# Run interactively
# docker run -it numbertoword

# docker tag numbertoword ahilashoba/numbertoword:latest
# docker push ahilashoba/numbertoword:latest


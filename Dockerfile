# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your application to the container
COPY . /app

# Command to run your application
CMD ["python", "main.py"]

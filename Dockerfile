# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Install build tools and Python dev headers required for uWSGI
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for caching optimization
COPY requirements.txt ./

# Install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Create a non-root user and ensure the directory is accessible
RUN addgroup --system django && adduser --system --group django && \
    chown -R django:django /code

# Switch to the non-root user
USER django

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
COPY ./app /code
COPY uwsgi.ini /conf/uwsgi.ini
COPY mime.types /etc/mime.types

# Expose Django's default port
EXPOSE 8000

# Run uWSGI with the appropriate configuration
CMD ["uwsgi", "--ini", "/conf/uwsgi.ini"]
# Use official Python image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Copy only requirements first for caching optimization
COPY requirements.txt ./

# Install dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose Django's default port
EXPOSE 8000

# Run Django development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
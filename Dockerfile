# Use the official Python 3.9 image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including app.py, templates folder, and the model file) to the container
COPY . /app/

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable to prevent Flask from running in debug mode in production
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "app.py"]

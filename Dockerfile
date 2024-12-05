# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files
COPY app.py requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port for Flask
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]

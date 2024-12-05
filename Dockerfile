# Use a lightweight base image for Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files (app.py and requirements.txt)
COPY app.py requirements.txt /app/

# Install Python dependencies (from requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (Cloud Run default port)
EXPOSE 8080

# Set the environment variable for the port to be used by Flask
ENV PORT 8080

# Run the Flask app when the container starts
CMD ["python", "app.py"]

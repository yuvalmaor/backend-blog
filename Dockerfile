# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements (if any) and the app to the working directory
COPY app.py /app/

# Install Flask (and any other dependencies, if needed)
RUN pip install --no-cache-dir flask

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY login.py .

# Run the script when the container launches
# We use -u to force the stdout/stderr streams to be unbuffered
CMD ["python", "-u", "login.py"]
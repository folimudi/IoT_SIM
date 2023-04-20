# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY /src /app

# Install any needed packages specified in requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "server.py"]

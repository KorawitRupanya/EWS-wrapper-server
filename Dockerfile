# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the host to the container's /app directory
COPY requirements.txt requirements.txt

# Install the Python dependencies listed in the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy the entire content of the current directory from the host to the /app directory in the container
COPY . .

# Set the environment variable FLASK_APP to specify the application factory for Flask
ENV FLASK_APP app:create_app

# Expose port 5000 to the outside world (default Flask port)
EXPOSE 5000

# Define the default command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

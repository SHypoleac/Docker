# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY hello_clock.py /app/hello_clock.py

# Switch to root user to install dependencies and set permissions
USER root

# Install pendulum
RUN pip install pendulum

# Set permissions for the script to be executable by the nobody user
RUN chmod 755 /app/hello_clock.py

# Switch back to the nobody user
USER nobody

# Run hello_clock.py when the container launches
CMD ["python", "hello_clock.py"]
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY JsonCompare.py /app/JsonCompare.py

# Switch to root user to install dependencies and set permissions
USER root

# Install pendulum
RUN pip install pendulum

# Set permissions for the script to be executable by the nobody user
RUN chmod 755 /app/JsonCompare.py

# Switch back to the nobody user
USER nobody

# Run JsonCompare.py when the container launches
CMD ["python", "JsonCompare.py"]
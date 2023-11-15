#!/bin/bash

echo "Running local checks..."

# Run pylint
echo "Running pylint..."
docker run --rm pingurl:latest pylint /backend

# Run pylint and fail if the score is under 9.0
echo "Running pylint with threshold..."
docker run --rm pingurl:latest pylint --fail-under=9.0 /backend

# Check the exit status of the pylint command
pylintStatus=$?

if [ $pylintStatus -ne 0 ]; then
    echo "Error: Pylint score is below the threshold of 9.0"
    exit 1
fi

# Build Docker image locally
echo "Building Docker image..."
docker build --no-cache -t pingurl:latest .

# Run the application and check if it starts successfully
echo "Running the application..."
docker run --rm -d -p 5001:5001 --name localpingapp pingurl:latest

# Sleep for a moment to allow the application to start
sleep 5

# Check if the application container is running
if [ "$(docker inspect -f '{{.State.Running}}' localpingapp)" != "true" ]; then
    echo "Error: The application failed to start."
    exit 1
fi
docker stop localpingapp
docker rm localpingapp

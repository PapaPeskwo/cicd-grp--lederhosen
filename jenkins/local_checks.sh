#!/bin/bash

echo "Running local checks..."

# Build Docker image locally
echo "Building Docker image..."
docker build --no-cache -t pingurl:latest .

# Run pylint
echo "Running pylint..."
docker run --rm pingurl:latest pylint /backend

# Run pylint and fail if the score is under 8.0
echo "Running pylint with threshold..."
docker run --rm pingurl:latest pylint --fail-under=8.0 /backend

# Check the exit status of the pylint command
pylintStatus=$?

if [ $pylintStatus -ne 0 ]; then
    echo "Error: Pylint score is below the threshold of 8.0"
    exit 1
fi

# Run pytest
echo "Running pytest..."
docker run --rm pingurl:latest pytest /backend

# Check the exit status of the pytest command
pytestStatus=$?

if [ $pytestStatus -ne 0 ]; then
    echo "Error: Pytest failed. Check the test results."
    exit 1
fi

# Run the application and check if it starts successfully
echo "Running the application..."
docker run --rm -d -p 5000:5000 --name pingapp pingurl:latest

# Sleep for a moment to allow the application to start
sleep 5

# Check if the application container is running
if [ "$(docker inspect -f '{{.State.Running}}' pingapp)" != "true" ]; then
    echo "Error: The application failed to start."
    exit 1
fi
docker stop pingapp
docker rm pingapp

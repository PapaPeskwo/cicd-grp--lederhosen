#!/bin/bash

echo "Running local checks..."

# Example: Run pylint
docker run --rm pingurl:latest pylint /backend

# Example: Build Docker image locally
docker build --no-cache -t pingurl:latest .


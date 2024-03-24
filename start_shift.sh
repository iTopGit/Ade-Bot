#!/bin/bash

# Check if pip is installed
echo "Checking pip..."
if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Installing pip..."
    sudo apt update
    sudo apt install python3-pip -y
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install pip."
        exit 1
    fi
    echo "pip installed successfully."
fi

# Check if requirements.txt file exists
echo "Checking requirements..."

if [ ! -f "Ade Project/requirements.txt" ]; then
    echo "Error: requirements.txt file not found."
    exit 1
fi

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -q -U -r "Ade Project/requirements.txt"

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies."
    exit 1
fi

# Run main.py
echo "Starting Shift..."
python3 "Ade Project/src/bot.py"

# Check if main.py execution was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to execute bot.py."
    exit 1
fi

echo "Shift started successfully."
exit 0

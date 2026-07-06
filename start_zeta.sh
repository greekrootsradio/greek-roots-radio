#!/bin/bash

echo "Starting Zeta..."

# Find PID safely
PID=$(lsof -ti :5050)

if [ ! -z "$PID" ]; then
    echo "Stopping existing process on port 5050: $PID"
    kill -9 $PID
    sleep 1
else
    echo "No existing process found on port 5050"
fi

cd ~/cyprus

python3 main.py

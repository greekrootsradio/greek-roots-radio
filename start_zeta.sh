#!/bin/bash

# ==========================================
# ZETA Autonomous AI Launcher
# ==========================================

cd "$(dirname "$0")"

LOG_FILE="cyprus.log"
ERROR_LOG="cyprus_error.log"
PID_FILE="zeta.pid"


echo "$(date) Starting ZETA" >> "$LOG_FILE"


# ------------------------------------------
# Prevent duplicate ZETA instances
# ------------------------------------------

if [ -f "$PID_FILE" ]; then

    PID=$(cat "$PID_FILE")

    if ps -p "$PID" > /dev/null 2>&1; then
        echo "ZETA already running PID $PID"
        exit 0
    else
        rm "$PID_FILE"
    fi

fi


# ------------------------------------------
# Start ZETA
# ------------------------------------------

nohup python3 main.py >> "$LOG_FILE" 2>> "$ERROR_LOG" &


PID=$!

echo "$PID" > "$PID_FILE"


echo "ZETA running in background"
echo "PID: $PID"
echo "Log: $LOG_FILE"

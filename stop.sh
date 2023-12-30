#!/bin/bash

PROCESS_CMD="python3 main.py --instance Down-Detector"
PROCESS_ID=$(pgrep -f "$PROCESS_CMD")

if [ -n "$PROCESS_ID" ]; then
    echo "Found $PROCESS_CMD with PID: $PROCESS_ID"
    sleep 1
    echo "Terminating process $PROCESS_ID"
    kill "$PROCESS_ID"
else
   echo "Unable to find $PROCESS_CMD, please ensure the applicaiton is running"
fi

#!/bin/bash

LOG_FOLDER="$PWD/logs"
LOG_FILE="$PWD/logs/log.log"
CONFIG_FILE="$PWD/config.cfg"

echo "Starting Down-Detector"
sleep 2

if [ -e "$LOG_FOLDER" ];then
    echo "$LOG_FOLDER was found"
else
    echo "Unable to find $LOGFOLDER, creating one now.."
    mkdir "$LOG_FOLDER"
fi

sleep 1

if [ -e "$LOG_FILE" ];then
    echo "$LOG_FILE was found"
else
    echo "Unable to find log file, creating one now.."
    touch "$LOG_FILE"
fi

sleep 1

if [ -e "$CONFIG_FILE" ];then
    echo "Config.cfg was found"
    sleep 1
    echo "Starting Down-Detector"
    echo "Check nohup.out or ./logs/log.log to ensure application is running properly"
    nohup python3 main.py --instance "Down-Detector" &
else
    echo "Unable to find config.cfg"
    echo "Please either clone the depo again or navigate to https://github.com/lilrebel17/down-detector and copy the config.cfg"
    echo "Exiting application start..."
    exit 1
fi

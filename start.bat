@echo off
echo "Starting Down Detector"
timeout 2

if exist ./logs (
    echo "Couldnt find ./logs"
) else (
    echo "Creating log folder.."
    mkdir "./logs"
)

timeout 1

if exist ./logs/log.log (
    echo "log.log was found"
) else (
    echo .> "./logs/log.log"
)

timeout 1

if exist config.cfg ( 
    echo "config.cfg was found"
) else (
    echo "Unable to find config.cfg" 
    echo "Please either clone the depo again or navigate to https://github.com/lilrebel17/down-detector and copy the config.cfg"
    exit
    )

echo "All checks ran successfully, please see ./logs/log.log for information. Do not close the window or the program will exit"
timeout 5
start python main.py
pause
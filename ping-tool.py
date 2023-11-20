import os
import time
import sendEmail
import logger
import configparser

config = configparser.RawConfigParser()
config_path = './config.cfg'
config.read(config_path)

LOCATION_NAME = config.get('Location','LOCATION_NAME')
LOCATION_IP = config.get('Location','LOCATION_IP')

def check_internet_connectivity():
    response = os.system('ping -c 4 google.com')
    if response == 0:
        logger.info('[PASS] INTERNET CONNECTIVITY DETECTED RESPONSE RECEIVED FROM - Google.com')
        return True
    else:
        logger.error('[FAIL] NO INTERNET CONNECTIVITY NO RESPONSE FROM - Google.com')
        return False

while True:
    internet_check = check_internet_connectivity()

    if internet_check is True:
        response = os.system(f"ping -c 4 {LOCATION_IP}")
        # We check to see if response == 0. It should be if we get a single reponses from the IP
        if response == 0:
            logger.info(f"[SUCCESS] RESPONSE RECEIEVED FROM - {LOCATION_NAME}")
        else:
        # IF we dont get a response from the IP. We update the log
            logger.error(f"[FAIL] NO RESPONSE FROM - {LOCATION_NAME}")
            # We open the log file
            with open('./logs/log.log',"r") as log:
                #We split the lines to see how many their are in the file
                lines = log.read().splitlines()
                #Finally, we take that number of lines and -1 due to it counting the empty space at the end.
                last_line = lines[-1]
            # We email the log to ourselves so we know that the IP is unreachable.
            sendEmail.send_email(last_line)
        # Then this waits 30 seconds and loops again.
        time.sleep(30.0)
    else:
        logger.info("Retrying in 60 seconds.")
        time.sleep(60)
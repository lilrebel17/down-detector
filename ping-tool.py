import os
import time
import sendEmail
import logger
import configparser

# Reading the config file
config = configparser.RawConfigParser()
config_path = './config_DEV.cfg'
config.read(config_path)
# Grabbing the Config Variables we need for this script
LOCATION_NAME = config.get('Location','LOCATION_NAME')
LOCATION_IP = config.get('Location','LOCATION_IP')

# Function to check for internet connectivity.
def check_internet_connectivity():
    #We just ping google. If it responds, we are connected to the internet.
    response = os.system('ping google.com')
    #response will = 0 if we get at least 1 packet back
    if response == 0:
        logger.success('Internet Connectivity Check - response received from google.com')
        return True
    else:
        logger.fail('Internet Connectivity Check - no response from google.com')
        return False

while True:
    #We run a connectivity check to see if we can talk to the internet
    internet_check = check_internet_connectivity()

    #IF our function returns true
    if internet_check is True:
        response = os.system(f"ping {LOCATION_IP}")
        # We check to see if response == 0. It should be if we get a single reponses from the IP
        if response == 0:
            logger.success(f"SITE CONNECTIVITY CHECK - RESPONSE RECEIEVED FROM - {LOCATION_NAME}")
        else:
        # IF we dont get a response from the IP. We update the log
            logger.fail(f"SITE CONNECTIVITY CHECK - NO RESPONSE FROM - {LOCATION_NAME}")
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
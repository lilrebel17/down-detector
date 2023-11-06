import os
import time
import sendEmail
import logger


print("Please input an IP address to monitor")
ip = input()
print("Please input a name for the site you wish to monitor")
location_name = input()
running = True

def check_internet_connectivity():
    response = os.system('ping google.com')
    if response == 0:
        logger.info('[PASS] INTERNET CONNECTIVITY DETECTED RESPONSE RECEIVED FROM - Google.com')
        return True
    else:
        logger.error('[FAIL] NO INTERNET CONNECTIVITY NO RESPONSE FROM - Google.com')

while running == True:
    internet_check = check_internet_connectivity()

    if internet_check is True:
        response = os.system(f"ping {ip}")
        # We check to see if response == 0. It should be if we get a single reponses from the IP
        if response == 0:
            logger.info(f"[SUCCESS] RESPONSE RECEIEVED FROM - {location_name}")
        else:
        # IF we dont get a response from the IP. We update the log
            logger.error(f"[FAIL] NO RESPONSE FROM - {location_name}")
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
import os
import time
import sendEmail
import logger

ip = "YOUR IP HERE"

while True:
    response = os.system("ping " + ip)
    # We check to see if response == 0. It should be if we get a single reponses from the IP
    if response == 0:
        logger.info("RESPONSE RECEIVED")
    else:
    # IF we dont get a response from the IP. We update the log
        logger.error("NO RESPONSE")
        # We open the log file
        with open('./log.log',"r") as log:
            #We split the lines to see how many their are in the file
            lines = log.read().splitlines()
            #Finally, we take that number of lines and -1 due to it counting the empty space at the end.
            last_line = lines[-1]
        # We email the log to ourselves so we know that the IP is unreachable.
        sendEmail.send_email(last_line)
    # Then this waits 30 seconds and loops again.
    time.sleep(30.0)

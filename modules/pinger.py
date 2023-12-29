import os
import time
from modules.logger import logger

# Pinger is used to ping remote sites

class Pinger():

    #site can be a hostname or ip
    #Hostname Example: google.com
    #IP Example: 192.168.1.1
    def ping_site(self,site):
        device_os = os.getenv("os")
        successes = 0
        for i in range(4):
            if device_os == "Windows_NT":
                response = os.system(f'ping -n 1 {site}')
            else:
                response = os.system(f'ping -c 1 {site}')
            if response == 0:
                successes += 1
            time.sleep(1)
        if successes > 0  and successes < 4:
            logger.warning(f'Server has Limited Connectivity - received {successes} packets from {site}')
        elif successes == 4:
            logger.success(f'Server has Full Connectivity - Received {successes} packets from {site}')
        else:
            logger.fail(f'Server has NO Connectivity - Receive {successes} packets from {site}')
        return successes
            




        

pinger = Pinger()
import time
from modules.logger import logger
from modules.configer import configuration
from modules.pinger import pinger
from modules.emailer import send_email


if __name__ == "__main__":
    while True:
        server_has_internet = pinger.check_internet_connectivity()
        if server_has_internet == True:
            logger.success('Server has internet - Received a response from google.com')
            site_is_online = pinger.ping_site(configuration.location_ip)
            if site_is_online == True:
                logger.success(f'Site is online - Received a response from {configuration.location_name}')
            else:
                logger.fail(f'Site is offline - Did not receive a response from {configuration.location_name}')
                log_message = str(logger.get_last_log())
                send_email(log_message)
            logger.info('Trying again in 30 seconds..')
            time.sleep(30)
        else:
            logger.fail('Server is offline - Did not receive a packet from google.com')
            logger.info('Trying again in 60 seconds..')
            time.sleep(60)
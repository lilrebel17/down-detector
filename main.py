import time
from modules.logger import logger
from modules.configer import configuration
from modules.pinger import pinger
from modules.emailer import send_email


if __name__ == "__main__":
    while True:
        internet_connection_check = pinger.ping_site('google.com')
        internet_connection_message = str(logger.get_last_log())

        if internet_connection_check == 0:
            logger.info('Trying again in 60 seconds')
            time.sleep(60)
        else:
            if internet_connection_check == 4:
                site_connection_check = pinger.ping_site(configuration.location_ip)
                site_connection_message = str(logger.get_last_log())

                if site_connection_check != 4:
                    send_email(f'{internet_connection_message}\n\n{site_connection_message}')
            logger.info('Trying Again in 30 seconds')
            time.sleep(30)
import time
import datetime
from modules.logger import logger
from modules.configer import configuration
from modules.pinger import pinger
from modules.emailer import send_email


if __name__ == "__main__":
    while True:
        #We check to see if the date in the config file is the same as the current date.
        if configuration.date != datetime.date.today().strftime('%m-%d-%y'):
            try:
                #If it ISNT, we rotate the log. Meant to rotate every 24 hours.
                logger.rotate_log()
            except Exception as e:
                #If there is an error rotating logs. We log it and send an email letting the admin know.
                logger.error(e)
                send_email(e)
            else:
                #If the log rotates successfully, we set the config's date to the current date
                #and wait 5 seconds to restart the loop
                configuration.set_date()
                time.sleep(5)
        else:
            #We ping google to see if we get a response.
            internet_connection_check = pinger.ping_site('google.com')
            #We then store the last line of the log file
            last_log = logger.get_last_log()
            internet_connection_message = str(last_log)
            #If we get no response from the internet it will return 0
            if internet_connection_check == 0:
                logger.info('Trying again in 60 seconds')
                time.sleep(60)
            else:
                #If we get 4 which is no packets dropping.
                if internet_connection_check == 4:
                    #Ping the site and log it.
                    site_connection_check = pinger.ping_site(configuration.location_ip)
                    site_connection_message = str(logger.get_last_log())
                    #If we get anything less than all packets back.
                    if site_connection_check != 4:
                        #Email the admin
                        send_email(f'{internet_connection_message}\n\n{site_connection_message}')
                logger.info('Trying Again in 30 seconds')
                time.sleep(30)
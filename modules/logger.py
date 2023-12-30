import logging
import os
import datetime
import shutil
import time
from modules.configer import configuration
# Logger will handle anything dealing with the log file
# This includes updating & reading the log file.

class Logger():
    def __init__(self) -> None:
        self.format = '[%(asctime)s] - %(message)s'
        self.log_path = './logs/log.log'
        logging.basicConfig(level=logging.INFO,format=self.format,datefmt='%m/%d/%Y %I:%M:%S %p',filename=self.log_path,encoding='utf-8')
        logging.basicConfig(level=logging.ERROR,format=self.format,datefmt='%m/%d/%Y %I:%M:%S %p',filename=self.log_path,encoding='utf-8')


    def info(self,message):
        logging.info(f'[INFO]: {message.upper()}')

    def success(self,message):
        logging.info(f'[PASS]: {message.upper()}')

    def error(self,message):
        logging.warning(f'[ERROR]: {message.upper()}')

    def warning(self,message):
        logging.warning(f'[WARNING]: {message.upper()}')

    def fail(self,message):
        logging.error(f'[FAIL]: {message.upper()}')

    #Used as the email body when the site is unreachable.
    def get_last_log(self):
        try:
            with open(self.log_path,"r") as log:
                #We split the lines to see how many their are in the file
                lines = log.read().splitlines()
                #Finally, we take that number of lines and -1 due to it counting the empty space at the end.
                last_line = lines[-1]
                log.close()
                return last_line
        except IndexError as error:
            error_string = str(error)
            self.error(error_string)
            return False

    #This is meant to rotate the log file every 24 hours a common naming schema
    #Log file Naming Schema:
    #log_month-day-year.log
    def rotate_log(self):
        #Get the paths for the log folder and what will be yesterdays log
        log_folder = os.path.dirname('./logs/log.log')
        yesterday_log = f'log_{configuration.date}.log'

        try:
            #Then we copy everything from the current log file to yesterdays log
            shutil.copyfile(self.log_path,f'{log_folder}/{yesterday_log}')
        except Exception as e:
            self.error(e)
        else:
            #If the file copies to yesterdays log. We erase the current log.log.
            current_log = open(self.log_path,'+r')
            current_log.truncate(0)
            current_log.close()

logger = Logger()
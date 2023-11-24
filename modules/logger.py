import logging

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
        with open(self.log_path,"r") as log:
            #We split the lines to see how many their are in the file
            lines = log.read().splitlines()
            #Finally, we take that number of lines and -1 due to it counting the empty space at the end.
            last_line = lines[-1]
            return last_line


logger = Logger()
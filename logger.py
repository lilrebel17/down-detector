import logging
from logging.handlers import TimedRotatingFileHandler

LOG_PATH = './logs/log.log'
FORMAT = '[%(asctime)s] - %(levelname)s: %(message)s'

handler = TimedRotatingFileHandler(LOG_PATH,when='midnight',backupCount=30)

logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p',filename=LOG_PATH,encoding='utf-8')
logging.basicConfig(level=logging.ERROR,format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p',filename=LOG_PATH,encoding='utf-8')

def info(message):
    logging.info(f'[INFO]: {message.upper()}')

def success(message):
    logging.info(f'[PASS]: {message.upper()}')

def error(message):
    logging.error(f'[ERROR]: {message.upper()}')

def fail(message):
    logging.error(f'[FAIL]: {message.upper()}')
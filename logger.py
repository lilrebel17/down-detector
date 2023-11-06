import logging

FORMAT = '[%(asctime)s] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p',filename='./logs/log.log',encoding='utf-8')
logging.basicConfig(level=logging.ERROR,format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p',filename='./logs/log.log',encoding='utf-8')

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)
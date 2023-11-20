import smtplib
import logger
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Setup & read the config file
config = configparser.RawConfigParser()
config_path = './config.cfg'
config.read(config_path)

# Getting the Email creds for both the sender & receipent
SENDER_EMAIL = config.get('Email_Credentials','FROM_ADDRESS')
SENDER_PASSWORD = config.get('Email_Credentials','FROM_PASSWORD')
RECEPIENT_EMAIL = config.get('Email_Credentials','TO_ADDRESS')

#Getting the Email Server Information
HOSTNAME = config.get('Email_Server',"HOSTNAME")
PORT = config.get('Email_Server',"PORT")

#Getting the Subject Line
SUBJECT = config.get('Email_Information','SUBJECT')

# Setting up the Email Message fields.
MESSAGE = MIMEMultipart()
MESSAGE['From'] = SENDER_EMAIL
MESSAGE['To'] = RECEPIENT_EMAIL
MESSAGE['Subject'] = SUBJECT

def send_email(message):
    # We attach a message to actually send to the user
    MESSAGE.attach(MIMEText(message))
    try: 
        # This gives us an SMTP SSL instance to work with on the hostname & default SSL port
        SMTP_SERVER = smtplib.SMTP_SSL(HOSTNAME,PORT)
        # We login with the password we input at the beginning
        SMTP_SERVER.login(SENDER_EMAIL,SENDER_PASSWORD)
        # The message cant be MIMEMultiType so we conver it to a string
        MESSAGE_STRING = MESSAGE.as_string()
        # Then we send the email out to the recepient email
        SMTP_SERVER.sendmail(SENDER_EMAIL,RECEPIENT_EMAIL,MESSAGE_STRING)
        logger.info(f'[SUCCESS] Email was sent out to {RECEPIENT_EMAIL}')
        # Finally we close the connection to the server
        SMTP_SERVER.quit()
    except Exception as e:
        logger.error(f'[FAIL] {e}')
        print(f"Error: {e}")
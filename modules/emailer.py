import smtplib
from modules.logger import logger
from modules.configer import configuration
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(message):
    MESSAGE = MIMEMultipart()
    MESSAGE['Subject'] = configuration.subject
    # We attach a message to actually send to the user
    MESSAGE.attach(MIMEText(message))
    try: 
        # This gives us an SMTP SSL instance to work with on the hostname & default SSL port
        SMTP_SERVER = smtplib.SMTP_SSL(configuration.hostname,configuration.port)
        # We login with the password we input at the beginning
        SMTP_SERVER.login(configuration.from_address,configuration.from_password)
        # The message cant be MIMEMultiType so we conver it to a string
        MESSAGE_STRING = MESSAGE.as_string()
        # Then we send the email out to the recepient email
        SMTP_SERVER.sendmail(configuration.from_address,configuration.to_address,MESSAGE_STRING)
        logger.success(f'Email was sent out to - {configuration.to_address}')
        # Finally we close the connection to the server
        SMTP_SERVER.quit()
    except Exception as e:
        logger.error(f'{e}')
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define to/from emails
SENDER_EMAIL = "INSERT YOUR EMAIL HERE"
RECEPIENT_EMAIL = 'INSERT RECEPIENT EMAIL HERE'

# SMTP address to send emails
HOSTNAME = "smtp.zoho.com"
PORT = 465

# Setting up the Email Message fields.
MESSAGE = MIMEMultipart()
MESSAGE['From'] = SENDER_EMAIL
MESSAGE['To'] = RECEPIENT_EMAIL
MESSAGE['Subject'] = 'INSERT SUBJECT HERE'

def send_email(message):
    # We attach a message to actually send to the user
    MESSAGE.attach(MIMEText(message))
    try: 
        # This gives us an SMTP SSL instance to work with on the hostname & default SSL port
        SMTP_SERVER = smtplib.SMTP_SSL(HOSTNAME,PORT)
        # We login with the password we input at the beginning
        SMTP_SERVER.login(SENDER_EMAIL,'INSERT YOUR PASSWORD HERE')
        # The message cant be MIMEMultiType so we conver it to a string
        MESSAGE_STRING = MESSAGE.as_string()
        # Then we send the email out to the recepient email
        SMTP_SERVER.sendmail(SENDER_EMAIL,RECEPIENT_EMAIL,MESSAGE_STRING)
        # Finally we close the connection to the server
        SMTP_SERVER.quit()
    except Exception as e:
        print(f"Error: {e}")
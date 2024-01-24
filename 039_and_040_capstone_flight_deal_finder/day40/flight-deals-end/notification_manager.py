from twilio.rest import Client
import smtplib 
import os 

TWILIO_SID = os.environ.get("TWILLIO_ID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILLIO_KEY")
TWILIO_VIRTUAL_NUMBER = "+18508015410"
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_PHONE") 

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, email:str, message:str):
        my_email = "vaporbirdo@gmail.com"
        password = os.environ.get("GMAIL_EMAIL_KEY")
        smtp_domain = "smtp.gmail.com" 
        
        connection = smtplib.SMTP(smtp_domain)
        connection.starttls()
        connection.login(user = my_email, password = password)
        msg_to_send = ("Flight Deal !!!\n\n" + message).encode("utf8")
        connection.sendmail(from_addr = my_email, to_addrs = email, msg = msg_to_send)
        connection.close()


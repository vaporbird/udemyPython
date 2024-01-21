import requests
import os
from twilio.rest import Client

TWILLIO_ID = os.environ.get("TWILLIO_ID")
TWILLIO_KEY = os.environ.get("TWILLIO_KEY")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILLIO_ID, TWILLIO_KEY)

    def send_sms(self, body:str):
        
        message = self.client.messages.create(
  	        from_ = "+18508015410",
  		    body = body,
  		    to = os.environ.get("MY_PHONE")
		)

        print(message.status)

#test = NotificationManager()
#test.send_sms("kole, kole, test")

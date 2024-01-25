import os
from twilio.rest import Client

TWILLIO_ID = os.environ.get("TWILLIO_ID")
TWILLIO_KEY = os.environ.get("TWILLIO_KEY")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILLIO_ID, TWILLIO_KEY)

    def send_sms(self, kiwi_flight_data: dict):
        msg = f'(Low Price Alert! Only {kiwi_flight_data["price"]} euro to fly from {kiwi_flight_data["cityFrom"]}-{kiwi_flight_data["flyFrom"]} to {kiwi_flight_data["cityTo"]}-{kiwi_flight_data["flyTo"]} on {kiwi_flight_data["local_departure"].split("T")[0]}'

        message = self.client.messages.create(
            from_="+18508015410",
            body=msg,
            to=os.environ.get("MY_PHONE")
        )

        print(message.status)

# test = NotificationManager()
# test.send_sms("kole, kole, test")

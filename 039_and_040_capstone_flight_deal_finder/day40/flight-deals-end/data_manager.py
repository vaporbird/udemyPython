from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c6dcc7cea7441693306e3103492711a5/flightDeals/prices"  

SHEETY_USER_ENDPOINT = "https://api.sheety.co/c6dcc7cea7441693306e3103492711a5/flightDeals/users"  

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_user_data(self):
        response = requests.get(url=SHEETY_USER_ENDPOINT)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

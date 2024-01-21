import requests
import os
import datetime as dt

KIWI_KEY = os.environ.get("KIWI_KEY")
KIWI_URL = "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_cheapest_price(self, start:str, end:str, fly_from:str, fly_to:str):
        headers = {
            "apikey" : KIWI_KEY,
        }
            
        prompt = {
            "fly_from" : fly_from,
            "fly_to" : fly_to,
            "date_from" : start,
            "date_to" :  end,
        }
        req = requests.get(url = KIWI_URL, params = prompt, headers = headers)
        req.raise_for_status()
        flights = req.json()["data"]
        try:
            cheapest = flights[0]["price"]
        except IndexError:
            return 0
        else:
            for flight in flights[1:]:
                if (flight["price"] < cheapest):
                    cheapest = flight["price"]  

            return cheapest


test = FlightSearch()
lis = test.get_cheapest_price("22/01/2024","22/01/2024","LIS","PLD")
print(lis)

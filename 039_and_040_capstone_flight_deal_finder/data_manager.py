import requests

SHEETY_URL = "https://api.sheety.co/c6dcc7cea7441693306e3103492711a5/flightDeals/prices"
class DataManager:
    def __init__(self):
        self.data:dict
        self.update_data()
        
    def update_data(self):
        req = requests.get(url = SHEETY_URL)
        try:
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        else:
            self.data = req.json()
            return True

    def get_data(self):
        return self.data
    
    def updade_row_price(self, row_name:str, row_value:int):
        prompt = {
            "price" : {
                "city" : row_name.capitalize(),
                "lowestPrice" : row_value,
            } 
        }
        try:
            req = requests.put(url = SHEETY_URL + "/2", json = prompt)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            SystemExit(err)
        else:
            return True

#test = DataManager()
#test.updade_row_price("paris",54)

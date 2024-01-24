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

    def get_city_iatas(self):
        cities = {}
        for city in self.data["prices"]:
            cities[city["city"]] = city["iataCode"]

        return cities

    def get_flight_min_prices(self):
        cities = {}
        for city in self.data["prices"]:
            cities[city["city"]] = city["lowestPrice"]

        return cities

    def get_row_index_of_a_city(self, city:str):
        counter = 2
        for d in self.data["prices"]:
            if city.lower().strip() == d["city"].lower().strip():
                return counter
            else:
                counter += 1
        raise KeyError("No such city!") 

    
    def updade_row_price(self, city_name:str, flight_price:int):
        city = city_name.capitalize()
        prompt = {
            "price" : {
                "city" : city,
                "lowestPrice" : flight_price,
            } 
        }
        try:
            req = requests.put(url = SHEETY_URL + "/" + str(self.get_row_index_of_a_city(city)), json = prompt)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            SystemExit(err)
        else:
            return True

    def set_iata(self, city:str, iata:str):
        city = city_name.capitalize()
        prompt = {
            "price" : {
                "city" : city(),
                "iataCode" : iata,
            } 
        }
        try:
            req = requests.put(url = SHEETY_URL + "/" + str(self.get_row_index_of_a_city), json = prompt)
            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            SystemExit(err)
        else:
            return True


#test = DataManager()
#asd = test.get_row_index_of_a_city("Berlin")
#print(asd)
#test.set_iata("paris",545)

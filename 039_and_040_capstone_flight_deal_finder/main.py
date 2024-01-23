from  data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime
from dateutil.relativedelta import relativedelta

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

destinations = dm.get_city_iatas()
cheapest_prices = dm.get_flight_min_prices()

now = datetime.datetime.now()
now_plus_six = now + relativedelta(months=+6)

today = now.strftime("%d/%m/%Y")
next_6_m = now_plus_six.strftime("%d/%m/%Y")

for destination in destinations:    
    print (destinations[destination])
    loc = fs.get_cheapest_price(cheapest_prices[destination] , today, next_6_m, "SOF", destinations[destination])
    if (loc):
        #nm.send_sms(loc)
        dm.updade_row_price(destination, loc["price"])

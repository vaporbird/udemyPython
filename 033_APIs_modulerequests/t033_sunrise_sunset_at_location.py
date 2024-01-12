import requests
import datetime as dt

MY_LAT = 42.144920
MY_LONG = 24.750320

parameters = {
	"lat" : MY_LAT,
	"lng": MY_LONG,
	"formatted":0,
	"tzid": "Europe/Sofia"
}

location_request = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
location_request.raise_for_status()

sunrise = location_request.json()["results"]["sunrise"]
sunset = location_request.json()["results"]["sunset"]
now = dt.datetime.now() 

sunrise_h = int(sunrise.split("T")[1].split(":")[0])
sunset_h = int(sunset.split("T")[1].split(":")[0])
now_h = now.hour

if now_h >= sunrise_h and now_h < sunset_h:
	print("It's bright outside")
else:
	print("It's dark outside")
	

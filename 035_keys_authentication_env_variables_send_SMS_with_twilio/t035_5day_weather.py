import requests
from twilio.rest import Client
MY_API_KEY = "6db4be4c4b16e1a1a341d3b0c525e45d"
MY_LAT = 42.144920
MY_LONG = 24.750320

#twilio
account_sid = 'AC105e52fdd6126936d0325df5ed1a8a90'
auth_token = '4a7d90235b560f87be581746e24ac149'
client = Client(account_sid, auth_token)

#openweather
parameters = {
"lat" :  MY_LAT,
"lon" : MY_LONG,
"appid" : MY_API_KEY,
}

weather = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
weather.raise_for_status()
data = weather.json()

for hourly in data["list"][:4]:
	code = hourly["weather"][0]["id"]
	if code < 700:
		message = client.messages.create(
  			from_='+18508015410',
  			body='It\'s going to rain today!',
  			to='<some_phone>'
		)
		print(message.status)
		break




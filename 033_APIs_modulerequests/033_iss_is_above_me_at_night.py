import datetime as dt
import requests
import smtplib
import time

MY_LAT = 42.144920
MY_LONG = 24.750320

def send_email(message, email, smtp_domain):
	my_email = "vaporbirdo@gmail.com"
	password = "pldlvuagdhmuehkk"
	
	connection = smtplib.SMTP(smtp_domain)
	connection.starttls()
	connection.login(user = my_email, password = password)
	msg_to_send = ("Subject:ISS above! \n\n" +  message).encode("utf8")
	connection.sendmail(from_addr = my_email, to_addrs = email, msg = msg_to_send)
	connection.close()


def get_sunrise_and_sunset(lat = MY_LAT, lng = MY_LONG, formatted = 0, tzid = "Europe/Sofia"):
	parameters = {
		"lat" : lng,
		"lng": lat,
		"formatted": formatted,
		"tzid": tzid,
	}
	
	location_request = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
	location_request.raise_for_status()
	
	sunrise = location_request.json()["results"]["sunrise"]
	sunset = location_request.json()["results"]["sunset"]
	
	sunrise_h = int(sunrise.split("T")[1].split(":")[0])
	sunset_h = int(sunset.split("T")[1].split(":")[0])
	
	return {"sunrise" : sunrise_h, "sunset" : sunset_h}

def is_it_night(sunrise = 6, sunset = 17):
	now = dt.datetime.now()
	hour = now.hour
	return (hour <= sunrise) or (hour > sunset)
	
def is_iss_above_me(my_lat = MY_LAT, my_long = MY_LONG):
	position_request = requests.get(url = "http://api.open-notify.org/iss-now.json")
	position_request.raise_for_status()

	current_lat = float(position_request.json()["iss_position"]["latitude"])
	current_long = float(position_request.json()["iss_position"]["longitude"])

	return (current_lat >= my_lat - 5 and current_lat <= my_lat + 5) and (current_long >= my_long - 5 and current_long <= my_long + 5)

day_diapazon = get_sunrise_and_sunset()
while True:
	if not is_it_night(day_diapazon["sunrise"], day_diapazon["sunset"]) and is_iss_above_me():
		send_msg = f"ISS is above you right now"
		smtp_domain = "smtp.gmail.com"
		send_email(send_msg, "vaporbirdo@gmail.com", smtp_domain)
		time.sleep(60*60)
	else:
		time.sleep(60)

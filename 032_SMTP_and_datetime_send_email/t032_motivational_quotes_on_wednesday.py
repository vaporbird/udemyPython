import datetime as dt
import smtplib as smtp
import random as rand

import smtplib

def send_email(message):
	my_email = "vaporbirdo@gmail.com"
	password = "pldlvuagdhmuehkk"
	
	connection = smtplib.SMTP("smtp.gmail.com")
	connection.starttls()
	connection.login(user = my_email, password = password)
	msg_to_send = ("Subject:This is a test message\n\n" + message).encode("utf8")
	connection.sendmail(from_addr = my_email, to_addrs = "vaporbirdo@yahoo.com", msg = msg_to_send)
	connection.close()

def random_quote():
	with open("./quotes.txt", "r") as qfile:
		quotes = qfile.readlines()
		return rand.choice(quotes)

today = dt.datetime.now()
weekday_today = today.weekday()

if weekday_today == 2:
	quote = random_quote()
	send_email(quote)
	

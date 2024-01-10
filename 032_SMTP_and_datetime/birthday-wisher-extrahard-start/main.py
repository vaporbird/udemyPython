##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random as rand
import smtplib as smtp
import pandas as pd
import smtplib 

def send_email(message, email, smtp_domain):
	my_email = "vaporbirdo@gmail.com"
	password = "pldlvuagdhmuehkk"
	
	connection = smtplib.SMTP(smtp_domain)
	connection.starttls()
	connection.login(user = my_email, password = password)
	msg_to_send = ("Subject:Happy B-Day AutoGen Message Cuz You're not special, sukk it\n\n" + message).encode("utf8")
	connection.sendmail(from_addr = my_email, to_addrs = email, msg = msg_to_send)
	connection.close()

def gen_bdays_today_list():
	today = dt.datetime.now()
	day = today.day
	month = today.month
	with open("./birthdays.csv") as birthdays:
		df = pd.read_csv(birthdays)
		bday_dict = df.to_dict(orient = "records")
		bday_persons = [] 
		for person in bday_dict:
			if person["day"] == day and person["month"] == month:
				bday_persons.append(person)
	return bday_persons

bdays = gen_bdays_today_list()
if len(bdays) > 0:
	for bday in bdays:
		rand_msg_index = rand.randint(1,3)
		with open(f"./letter_templates/letter_{rand_msg_index}.txt", "r") as msg:
			send_msg = msg.read()
			send_msg = send_msg.replace("[NAME]", bday["name"])
			send_msg = send_msg.replace("Angela", "Ivan")
			smtp_domain = "smtp.gmail.com" # This could be a dict, with keys of what is  after @ and values of the smtp domain, but im lazy, so hardcode it 
			send_email(send_msg, bday["email"], smtp_domain)
#print(bdays)




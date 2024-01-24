import requests


SHEETY_URL = "https://api.sheety.co/c6dcc7cea7441693306e3103492711a5/flightDeals/users"

print("Welcome to the Flight club!\n")

while True:
    first_name = input("What is your first name?\n").strip().capitalize()
    if first_name.isalpha():
        break
    print("only letters allowed")

while True:
    last_name = input("What is your last name?\n").strip().capitalize()
    if last_name.isalpha():
        break
    print("only letters allowed")

while True:
    email1 = input("What is your email?\n").strip()
    email2 = input("Type your email again\n").strip()
    if (email1 == email2):
        break
    print("Emails do not match, try again")

sheety_reg_params = {
    "user": {
        "firstName" : first_name,
        "lastName" : last_name,
        "email": email1
    }
}
#add_user_req = requests.post(url = SHEETY_URL, json = sheety_reg_params)
#add_user_req.raise_for_status()

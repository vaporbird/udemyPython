import requests
import datetime
import os

API_KEY = os.environ.get("NUTRI_API_KEY")
API_ID = os.environ.get("NUTRI_API_ID")
CONTENT = "application/json"
EXER_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-Type" : CONTENT,
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
}

body = {
    "query" : ""
}
body["query"] = input("Prompt the activities you did today with their respective timings:\n")

response = requests.post(url = EXER_URL, json = body, headers = headers)
response.raise_for_status()

print(response.text)
exercises = response.json()["exercises"]
#date, time, exercise = name, duration = duration_min, calories = nf_calories

sheety_url = "https://api.sheety.co/c6dcc7cea7441693306e3103492711a5/myWorkouts/workouts"
sheety_headers = {
    "Content-Type" : "application/json",
    "Authorization" :  os.environ.get("SHEETY_KEY"), 
}

time_now = datetime.datetime.now()
date = time_now.strftime("%d/%m/%Y")
time = time_now.strftime("%H:%M:%S")
print(date,time)
row = {"workout":{}}
#questionable_dev_decision:#1 They workout key should be singular(without s) and the datasheet should be named as a multiple(with s). It is documented, but still strange.
#questionable_dev_decision:#2 The column names in the sheet are capitalized, but here you need to prompt the first letter as lowercase. This apparently is true only for the first letter and also if you go through the struggle of lowercasing it, why don't you do it with my input aswell
for exercise in exercises:
    row["workout"]["tiMe"] = time
    row["workout"]["date"] = date
    row["workout"]["exercise"] = exercise["name"] 
    row["workout"]["duration"] = exercise["duration_min"]
    row["workout"]["calories"] = exercise["nf_calories"]

    sheety_req = requests.post(url = sheety_url, json = row, headers = sheety_headers)
    sheety_req.raise_for_status()

import requests
import datetime
import json
import smtplib
import html

parameters_av = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "outputsize" : "compact",
    "apikey" :"",
}

data = requests.get("https://www.alphavantage.co/query", params = parameters_av).json()

#if exceeding their API daily limits use old data, else save data
if len(data) == 1:
    with open("./data.json") as file:
        data = json.load(file)
else:
    with open("./data.json","w") as file:
        file.write((data).encode("utf-8"))

#using last week's data because today is not generated yet, also last four days are missing for some reason
today = str((datetime.datetime.now() - datetime.timedelta(7)).date())
yesterday = str((datetime.datetime.now() - datetime.timedelta(8)).date())

open_today = float(data["Time Series (Daily)"][today]["1. open"])
open_yesterday = float(data["Time Series (Daily)"][yesterday]["1. open"])

if abs(1 - open_today/open_yesterday) > 0.0001:
    parameters_na = {
        "q" : "Tesla Inc",
        "from" : today,
        "sortBy" : "popularity",
        "apiKey" : "",
    }


    news = requests.get("https://newsapi.org/v2/everything", params = parameters_na).json()
    top3art = {art["title"]:art["description"] for art in news["articles"][0:2]}

    #send email
    message = ""
    for art in top3art:
        message += html.unescape(f"=== {art} ===\n {top3art[art]} \n\n")
    message = message.encode("utf-8")
    my_email = "vaporbirdo@gmail.com"
    password = "pldlvuagdhmuehkk"
    
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(from_addr = my_email, to_addrs = "vaporbirdo@yahoo.com", msg = f"Subject:Stocks Action, change of {(1 - open_today/open_yesterday)*100}%\n\n{message}")
    connection.close()
    

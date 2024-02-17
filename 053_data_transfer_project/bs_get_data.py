import requests
from bs4 import BeautifulSoup as bs
import re

WEBSITE = "https://appbrewery.github.io/Zillow-Clone/"


class Scraper:
    def __init__(self):
        website = requests.get(WEBSITE).text
        soup = bs(website, "html.parser")
        self.offers = []
        data = soup.select('.List-c11n-8-84-3-photo-cards > li')

        for d in data:
            #  get only the numberic values of the text in the price
            price = d.select(".PropertyCardWrapper__StyledPriceLine")[0].text.split(" ")[0]
            price = re.sub("\D", "", price)
            address = d.select("address")[0]
            address = address.text.strip()
            link = d.select("a")[0]["href"]
            self.offers.append({"address": address, "price": price, "link": link})

    def get_data(self):
        return self.offers

#  test = Scraper().get_data()

from bs4 import BeautifulSoup
import requests
from send_mail import SendMail

PRODUCT_URL = "https://www.amazon.com/dp/B08PQ2KWHS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
ITEM_NAME = "Instant cooker"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(PRODUCT_URL)
html = response.text

bs = BeautifulSoup(html, parser="lxml.parser", features="lxml")
# look at this abomination below
price_whole = bs.select("div.a-section span.a-price span[aria-hidden='true'] span.a-price-whole")[0].text
price_fraction = bs.select("div.a-section span.a-price span[aria-hidden='true'] span.a-price-fraction")[0].text
price = float(price_whole + price_fraction)


if (price < 120):
    SendMail.send_email("amazon item:"+ITEM_NAME, f"Has dropped in price to {price}")

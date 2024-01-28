import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
top100 = response.text

soup = BeautifulSoup(top100, parser="html.parser", features="lxml")
entries = soup.select("h3")

with open("./movies_list.txt", "w") as file:
    file.write("")

with open("./movies_list.txt", "a") as file:
    for entry in reversed(entries):
        file.write(entry.text + "\n")

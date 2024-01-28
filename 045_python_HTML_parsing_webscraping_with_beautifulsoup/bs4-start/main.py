from bs4 import BeautifulSoup

with open("./website.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")  # 2nd arg is the pareser

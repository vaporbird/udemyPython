import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
hacker_news = response.text
soup = BeautifulSoup(hacker_news, parser="html.parser", features="lxml")
articles = soup.select(selector=".titleline > a")
scores = soup.select(selector=".subtext")

index = 0
top_article_score = 0
for i in range(len(articles)):
    if not (scores[i].select(".subline .score")):  # Because some posts have no scores
        continue
    score = int(scores[i].select(".subline .score")[0].getText().split(" ")[0])
    if top_article_score < score:
        top_article_score = score
        index = i
top_article_title = articles[index].getText()
top_article_link = articles[index].get("href")

print(f"-- TOP ARTICLE --\ntitle : {top_article_title}\nscore : {top_article_score}\nlink : {top_article_link}")

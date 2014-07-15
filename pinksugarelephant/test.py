import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://slownews.kr/").read()

soup = BeautifulSoup(htmltext, from_encoding = "utf-8")

authors = []

for tag in soup.select(".recent_news_title"):
	authors.append(tag.get_text())

for author in authors:
	print author


import urllib.request
import http.cookiejar
import requests
import re
import sys
from bs4 import BeautifulSoup


head = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

url = "https://bdwm.net/v2/"

def crawler():
	r = requests.get(url + "hot-topic.php", headers=head)
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "html.parser")
	titles = []
	authors = []
	boards = []
	links = []

	for div in soup.find_all("div"):
		t = div.get("class")
		if t == ["title", "l", "limit"]:
			titles.append(div.get_text())
		elif t == ["board", "l", "limit"]:
			boards.append(div.get_text())
		elif t == ["name", "limit"]:
			authors.append(div.get_text())

	for link in soup.find_all('a'):
		t = link.get("href")
		if t != None and re.search(r'threadid=\d+$', t) != None:
			links.append(url + t)

	return titles, boards, authors, links
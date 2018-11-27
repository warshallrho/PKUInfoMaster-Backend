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

url = "http://www.pku-hall.com/pwxx.aspx"

def crawler():
	r = requests.get(url, headers=head)
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "html.parser")
	dates = []
	times = []
	places = []
	titles = []
	prices = []
	statuses = []

	cnt = 0
	for td in soup.find_all("td"):
		t = td.get_text().strip()
		if cnt == 0:
			dates.append(t)
		elif cnt == 2:
			times.append(t)
		elif cnt == 3:
			places.append(t)
		elif cnt == 4:
			titles.append(t)
		elif cnt == 5:
			prices.append(t)
		elif cnt == 6:
			statuses.append(t)
		cnt = (cnt + 1) % 7

	return dates, times, places, titles, prices, statuses
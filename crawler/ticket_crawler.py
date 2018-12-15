import urllib.request
import http.cookiejar
import requests
import re
import sys
from bs4 import BeautifulSoup
import time


head = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

url = "http://www.pku-hall.com"

def crawler():
	r = requests.get(url + "/pwxx.aspx", headers=head)
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "html.parser")
	dates = []
	times = []
	places = []
	titles = []
	prices = []
	statuses = []
	startdates = []
	links = []

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
			link = url + re.findall("<img src=\"(.*?)\"", str(td))[0]
			links.append(link)
			
			id = int(re.findall("MM_over\((.*?)\)", str(td))[0])
			para = {"id": id}
			r = requests.get(url + "/qbhd-nr.aspx", headers=head, params=para)
			t = re.findall("开票时间：(.*?)月(.*?)日", r.text)[0]
			date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
			year = int(date[0: 4])
			startdate = "{0}-{1}-{2}".format(year, t[0].zfill(2), t[1].zfill(2))
			if startdate > dates[-1]:
				year = year - 1
				startdate = "{0}-{1}-{2}".format(year, t[0].zfill(2), t[1].zfill(2))
			startdates.append(startdate)

		elif cnt == 5:
			prices.append(t)
		elif cnt == 6:
			statuses.append(t)
		cnt = (cnt + 1) % 7

	return dates, times, places, titles, prices, statuses, startdates, links
import urllib.request
import http.cookiejar
import requests
import re
import sys
import time
from bs4 import BeautifulSoup


head = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

url = "http://lecture.pku.edu.cn/index_new.php?page="

titles = []
speakers = []
times = []
places = []

def crawler():
	today = time.strftime('%Y.%m.%d',time.localtime(time.time()))
	for i in range(1000):
		f = False
		r = requests.get(url + str(i+1), headers=head)
		r.encoding = "utf-8"
		soup = BeautifulSoup(r.text, "html.parser")
		for div in soup.find_all("div"):
			if div.get("class") == ["infortext"]:
				t = str(div).split("<br/>")
				title = re.findall(r"\"_blank\">(.+?)</a>", t[0])[0]
				speaker = re.findall(r"主讲人： (.+?) $", t[1])[0]
				tim = re.findall(r"时    间：(.+?)      ", t[2])[0]
				place = re.findall(r"地点：：(.+?) </div>", t[2])[0]

				day = tim.split(" ")[0].replace("年", ".").replace("月", ".").replace("日", "")
				if day < today:
					f = True
					break
				titles.append(title)
				speakers.append(speaker)
				times.append(tim)
				places.append(place)
		if f:
			break
	return titles, speakers, times, places

crawler()
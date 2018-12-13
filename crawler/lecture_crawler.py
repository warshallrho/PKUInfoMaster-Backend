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

url = "http://resource.pku.edu.cn/index.php?r=lecturepre/view&id="

titles = []
speakers = []
places = []
dates = []
times = []
faculties = []
schools = []
labels = []
pids = []

def crawler():
	for i in range(1, 1000, 2):
		r = requests.get(url+str(i), headers=head)
		r.encoding = "utf-8"
		soup = BeautifulSoup(r.text, "html.parser")
		for sec in soup.find_all("section"):
			if(sec.get("class") == ["pull-left", "lec-content", "bg-white"]):
				title = sec.find("h3").get_text()
				if(title == " "):
					break
				title.strip()
				div = sec.find_all("div", attrs={"class": "brief"})
				speaker = div[0].get_text()
				place = div[1].get_text()
				t = div[2].get_text().split(" ")
				date = t[0]
				time = t[1]
				t = div[7].get_text().split(" / ")
				faculty = t[0]
				school = t[1]
				label = div[8].get_text().strip("\n")

				titles.append(title)
				speakers.append(speaker)
				places.append(place)
				dates.append(date)
				times.append(time)
				faculties.append(faculty)
				schools.append(school)
				labels.append(label)
				pids.append(i)

	return titles, speakers, places, dates, times, faculties, schools, labels, pids
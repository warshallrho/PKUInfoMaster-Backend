import urllib.request
import http.cookiejar
import requests
import re
import sys
from bs4 import BeautifulSoup
from selenium import webdriver


head = {
	"Accept": "application/json, text/plain, */*",
	"Referer": "https://portal.pku.edu.cn/portal2017/",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

url = "https://portal.pku.edu.cn/portal2017/canteen/dat/hotpoints_canteen.dat"

def crawler():
	print("canteen start!")

	r = requests.get(url, headers=head)
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "html.parser")

	print("canteen end!")

	return re.findall(r"\d+", str(soup))
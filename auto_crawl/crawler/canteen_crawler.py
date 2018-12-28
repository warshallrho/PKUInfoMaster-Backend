import urllib.request
import http.cookiejar
import requests
import re
import sys
import json
import random
from bs4 import BeautifulSoup
from selenium import webdriver


head = {
	"Accept": "application/json, text/plain, */*",
	"Referer": "https://portal.pku.edu.cn/portal2017/",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

url = "https://portal.w.pku.edu.cn/portal2017/canteen/dat/hotpoints_canteen.dat"

def login():
	url = "https://iaaa.pku.edu.cn/iaaa/oauthlogin.do"
	redirect = "https://w.pku.edu.cn/users/auth/pkuauth/callback"
	data = {"appid": "webvpn", "userName": "1600012836", "password": "lsh971101", "redirUrl": redirect}
	session = requests.session()
	r = session.post(url, data=data)
	token = json.loads(r.text, strict=False)["token"]
	rand = random.random()
	para = {"rand": rand, "token": token}
	r = session.get(redirect, params=para)
	return session

def crawler():
	print("canteen start!")

	session = login()
	r = session.get(url, headers=head)
	r.encoding = "utf-8"
	soup = BeautifulSoup(r.text, "html.parser")

	print("canteen end!")

	return re.findall(r"\d+", str(soup))

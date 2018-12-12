import urllib.request
import http.cookiejar
import requests
import re
import sys
import time
import json
from bs4 import BeautifulSoup

head = {
	"Host": "www.pkuhelper.com",
	"Accept": "*/*",
	"Accept-Language": "zh-Hans-CN;q=1",
	"Connection": "keep-alive",
	"Accept-Encoding": "gzip, deflate",
	"User-Agent": "PKU Helper/2.3.8 (iPhone; iOS 12.1; Scale/3.00)"
}
url = "http://162.105.205.61/services/pkuhole/api.php"

def crawler(pid):
	para = {"action": "getcomment", "pid": pid, "token": "pnh3dmks5fmo00u0177qplsre44qo4fk"}
	r = requests.get(url, headers=head, params=para)
	data = json.loads(r.text)["data"]
	pids = []
	texts = []
	names = []
	for t in data:
		pids.append(int(t["pid"]))
		texts.append(t["text"])
		names.append(t["name"])
	return pids, texts, names
	
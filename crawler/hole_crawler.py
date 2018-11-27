import urllib.request
import http.cookiejar
import requests
import re
import sys
import time
import json
from bs4 import BeautifulSoup

head = {
	"Host": "www.pkuhelper.com:10301",
	"Accept": "*/*",
	"Accept-Language": "zh-Hans-CN;q=1",
	"Connection": "keep-alive",
	"Accept-Encoding": "gzip, deflate",
	"User-Agent": "PKU Helper/2.3.8 (iPhone; iOS 12.1; Scale/3.00)"
}
url = "http://www.pkuhelper.com/pkuhelper/../services/pkuhole/api.php"
def crawler():
	para = {"action": "getlist", "p": "1"}
	r = requests.get(url, headers=head, params=para)
	data = json.loads(r.text)["data"]
	pids = []
	texts = []
	replys = []
	likenums = []
	for t in data:
		pids.append(int(t["pid"]))
		texts.append(t["text"])
		replys.append(int(t["reply"]))
		likenums.append(int(t["likenum"]))
	return pids, texts, replys, likenums
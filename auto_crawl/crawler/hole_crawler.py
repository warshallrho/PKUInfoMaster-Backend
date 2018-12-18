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
pids = []
texts = []
replys = []
likenums = []
def crawler():
	print("hole start!")

	for i in range(5):
		para = {"action": "getlist", "p": str(i+1)}
		r = requests.get(url, headers=head, params=para)
		data = json.loads(r.text)["data"]
		for t in data:
			if int(t["pid"]) in pids:
				continue
			pids.append(int(t["pid"]))
			texts.append(t["text"])
			replys.append(int(t["reply"]))
			likenums.append(int(t["likenum"]))

	print("hole end!")

	return pids, texts, replys, likenums

if __name__ == "__main__":
	crawler()
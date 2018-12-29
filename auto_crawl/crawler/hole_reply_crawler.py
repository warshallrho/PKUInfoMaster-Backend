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

#树洞回复爬虫，爬取树洞回复号、内容、姓名
def crawler(pid):
	print("hole reply start!")
	cids = []
	texts = []
	names = []

	try:
		para = {"action": "getcomment", "pid": pid, "token": "pnh3dmks5fmo00u0177qplsre44qo4fk"}
		r = requests.get(url, headers=head, params=para)
		data = json.loads(r.text)["data"]
		for t in data:
			cids.append(int(t["cid"]))
			texts.append(t["text"])
			names.append(t["name"])

		print("hole reply end!")

		return cids, texts, names
	except:
		print("HOLE REPLY ERROR!!!!!!")
		return cids, texts, names
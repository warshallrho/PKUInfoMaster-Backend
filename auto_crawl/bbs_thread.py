#coding=gbk
from crawler import bbs_crawler as bbs_crawler
from config import db
from peewee import *
import time


def bbs():
	class bbs(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		class Meta:
			database = db

	titles, boards, authors, links = bbs_crawler.crawler()

	t = bbs.delete()
	t.execute()

	for i in range(100):
		title = titles[i]
		board = boards[i]
		author = authors[i]
		link = links[i]

		t = bbs.insert(id=i+1, title=title, board=board, author=author, link=link)
		t.execute()

	bbs_history(titles, boards, authors, links)

def bbs_history(titles, boards, authors, links):
	class bbs_history(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		date = DateField()
		count = IntegerField()
		class Meta:
			database = db

	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	for i in range(10):
		title = titles[i]
		board = boards[i]
		author = authors[i]
		link = links[i]
		try:
			t = bbs_history.get(bbs_history.link == link, bbs_history.date == date)
			count = t.count + 1
			t = bbs_history.update(count=count).where(bbs_history.link == link, bbs_history.date == date)
			t.execute()

		except bbs_history.DoesNotExist:
			t = bbs_history.insert(title=title, board=board, author=author, link=link, date=date, count=1)
			t.execute()

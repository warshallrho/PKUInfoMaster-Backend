from crawler import hole_reply_crawler as hole_reply_crawler
from crawler import hole_crawler as hole_crawler
from peewee import *
from config import db
import time


def hole():
	class hole(Model):
		id = IntegerField()
		pid = IntegerField()
		text = CharField()
		reply = IntegerField()
		likenum = IntegerField()
		date = DateField()
		key = IntegerField()
		class Meta:
			database = db

	pids, texts, replys, likenums = hole_crawler.crawler()
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	for i in range(len(pids)):
		pid = pids[i]
		text = texts[i]
		reply = replys[i]
		likenum = likenums[i]
		try:
			t = hole.get(hole.pid == pid)
			if t.likenum != likenum or t.reply != reply:
				t = hole.update(likenum=likenum, reply=reply, date=date, key=reply + likenum).where(hole.pid == pid)
				t.execute()
				hole_reply(pid)

		except hole.DoesNotExist:
			t = hole.insert(pid=pid, text=text, reply=reply, likenum=likenum, date=date, key=reply + likenum)
			t.execute()
			hole_reply(pid)

def hole_reply(pid):
	class hole_reply(Model):
		id = IntegerField()
		cid = IntegerField()
		pid = IntegerField()
		text = CharField()
		name = CharField()
		class Meta:
			database = db

	cids, texts, names = hole_reply_crawler.crawler(pid)
	for i in range(len(cids)):
		cid = cids[i]
		text = texts[i]
		name = names[i]
		try:
			t = hole_reply.get(hole_reply.cid == cid)
			# t.execute()

		except hole_reply.DoesNotExist:
			t = hole_reply.insert(cid=cid, pid=pid, text=text, name=name)
			t.execute()

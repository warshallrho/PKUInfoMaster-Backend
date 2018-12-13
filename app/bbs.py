#coding=gbk
from app import app
from peewee import *
import json
import time
from .config import db


# 查询BBS实时热点
def bbs_query(lmt=0):
	class bbs(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		class Meta:
			database = db

	bbs_array = []
	if (lmt == 0):
		results = bbs.select()
	else:
		results = bbs.select().limit(lmt)

	for array in results:
		title, board, author, link = array.title, array.board, array.author, array.link
		dic = {}
		dic["title"] = title
		dic["board"] = board
		dic["author"] = author
		dic["link"] = link
		bbs_array.append(dic)
	return bbs_array

# 查询BBS实时热点的路由
@app.route('/BBS')
def BBS():
	bbs_array = bbs_query()
	bbs_array_json = json.dumps(bbs_array, ensure_ascii=False)
#	with open("bbs_record.json","w", encoding="utf8") as f:
#		f.write(bbs_array_json)
	return bbs_array_json

# 按天查询BBS热点
def bbs_date_query(year=2018, month=12, day=0, lmt=10):
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

	time_day = time.struct_time((year, month, day, 0, 0, 0, 0, 0, 0))
	date = time.strftime('%Y-%m-%d', time_day)

	results = bbs_history.select().where(bbs_history.date == date).order_by(bbs_history.count.desc()).limit(lmt)

	bbs_history_array = []
	for array in results:
		title, board, author, link = array.title, array.board, array.author, array.link
		dic = {}
		dic["title"] = title
		dic["board"] = board
		dic["author"] = author
		dic["link"] = link
		bbs_history_array.append(dic)
	return bbs_history_array

# 查询BBS历史每日热点的路由
@app.route('/BBS/<int:YY>/<int:MM>/<int:DD>')
def BBSYMD(YY, MM, DD):
	bbsYMD_array = bbs_date_query(YY, MM, DD, 10)
	bbs_history_array_json = json.dumps(bbsYMD_array, ensure_ascii=False)
	#with open("bbs_history_record.json","w", encoding="utf8") as f:
	#	f.write(bbs_history_array_json)
	return bbs_history_array_json

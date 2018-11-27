#coding=gbk
from flask import render_template, jsonify
from app import app
from peewee import *
import json
import time

#passwd = input("password: ")
db = MySQLDatabase(host="127.0.0.1", user="root", passwd='1998218wrh', database="pkuinfomaster", charset="utf8", port=3306)

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'WuRuihai'}
	title = 'PKUInfoMaster'
	return render_template('index.html', title=title, user=user)


def bbs_query():
	class bbs(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		class Meta:
			database = db

	bbs_array = []
	results = bbs.select()

	for array in results:
		title, board, author, link = array.title, array.board, array.author, array.link
		dic = {}
		dic["title"] = title
		dic["board"] = board
		dic["author"] = author
		dic["link"] = link
		bbs_array.append(dic)
	return bbs_array

@app.route('/BBS')
def BBS():
	bbs_array = bbs_query()
	bbs_array_json = json.dumps(bbs_array, ensure_ascii=False)
#	with open("bbs_record.json","w", encoding="utf8") as f:
#		f.write(bbs_array_json)
	#return render_template('BBS.html', posts=bbs_array, title='PKUInfoMaster')
	return bbs_array_json


def bbs_date_query(year=2018, month=11, day=0):
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

	results = bbs_history.select().where(bbs_history.date == date).order_by(bbs_history.count.desc()).limit(10)

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

@app.route('/BBS/<int:YY>/<int:MM>/<int:DD>')
def BBSYMD(YY, MM, DD):
	#print(YY, MM, DD)
	bbsYMD_array = bbs_date_query(YY, MM, DD)
	bbs_history_array_json = json.dumps(bbsYMD_array, ensure_ascii=False)
#	with open("bbs_history_record.json","w", encoding="utf8") as f:
#		f.write(bbs_history_array_json)
	return bbs_history_array_json


def ticket_query():
	class ticket(Model):
		id = IntegerField()
		date = DateField()
		time = TimeField()
		place = CharField()
		title = CharField()
		price = CharField()
		status = CharField()
		class Meta:
			database = db

	ticket_array = []
	results = ticket.select()
	for array in results:
		date, time, place, title, price, status = array.date, array.time, array.place, array.title, array.price, array.status
		dic = {}
		dic["date"] = str(date)
		dic["time"] = str(time)
		dic["place"] = place
		dic["title"] = title
		dic["price"] = price
		dic["status"] = status
		ticket_array.append(dic)
	return ticket_array

@app.route('/TICKET')
def TICKET():
	ticket_array = ticket_query()
	ticket_array_json = json.dumps(ticket_array, ensure_ascii=False)
#	with open("ticket_record.json","w", encoding="utf8") as f:
#		f.write(ticket_array_json)
	return ticket_array_json


def canteen_query():
	class canteen(Model):
		id  = IntegerField()
		name = CharField()
		total = IntegerField()
		now = IntegerField()
		class Meta:
			database = db

	canteen_array = []
	results = canteen.select()
	for array in results:
		name, total, now = array.name, array.total, array.now
		dic = {}
		dic["name"] = name
		dic["total"] = total
		dic["now"] = now
		canteen_array.append(dic)
	return canteen_array
	canteen_array = json.dumps(canteen_array, ensure_ascii=False)
#	with open("canteen_record.json","w", encoding="utf8") as f:
#		f.write(canteen_array)

@app.route('/CANTEEN')
def CANTEEN():
	canteen_array = canteen_query()
	canteen_array_json = json.dumps(canteen_array, ensure_ascii=False)
#	with open("canteen_record.json","w", encoding="utf8") as f:
#		f.write(canteen_array_json)
	return canteen_array_json


def lecture_query():
	class lecture(Model):
		id  = IntegerField()
		title = CharField()
		speaker = CharField()
		time = CharField()
		place = CharField()
		class Meta:
			database = db

	lecture_array = []
	results = lecture.select()
	for array in results:
		title, speaker, time, place = array.title, array.speaker, array.time, array.place
		dic = {}
		dic["title"] = title
		dic["speaker"] = speaker
		dic["time"] = time
		dic["place"] = place
		lecture_array.append(dic)
	return lecture_array

@app.route('/LECTURE')
def LECTURE():
	lecture_array = lecture_query()
	lecture_array_json = json.dumps(lecture_array, ensure_ascii=False)
#	with open("lecture_record.json","w", encoding="utf8") as f:
#		f.write(lecture_array_json)
	return lecture_array_json


def hole_query():
	class hole(Model):
		id = IntegerField()
		pid = IntegerField()
		text = CharField()
		reply = IntegerField()
		likenum = IntegerField()
		class Meta:
			database = db

	hole_array = []
	results = hole.select()
	for array in results:
		pid, text, reply, likenum = array.pid, array.text, array.reply, array.likenum
		dic = {}
		dic["pid"] = pid
		dic["text"] = text
		dic["reply"] = reply
		dic["likenum"] = likenum
		hole_array.append(dic)
	return hole_array

@app.route('/HOLE')
def HOLE():
	hole_array = hole_query()
	hole_array_json = json.dumps(hole_array, ensure_ascii=False)
#	hole_array_json = json.dumps(hole_array, ensure_ascii=False)
#	with open("hole_record.json","w", encoding="utf8") as f:
#		f.write(hole_array_json)
	return hole_array_json


def hole_reply_query():
	class hole_reply(Model):
		id = IntegerField()
		pid = IntegerField()
		text = CharField()
		name = CharField()
		class Meta:
			database = db

	hole_reply_array = []
	results = hole_reply.select()
	for array in results:
		pid, text, name = array.pid, array.text, array.name
		dic = {}
		dic["pid"] = pid
		dic["text"] = text
		dic["name"] = name
		hole_reply_array.append(dic)
	hole_reply_array = json.dumps(hole_reply_array, ensure_ascii=False)
	with open("hole_reply_record.json","w", encoding="utf8") as f:
		f.write(hole_reply_array)

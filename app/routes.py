#coding=gbk
from flask import render_template, jsonify
from app import app
from peewee import *
import json
import time

#passwd = input("password: ")
db = MySQLDatabase(host="127.0.0.1", user="root", passwd='1998218wrh', database="pkuinfomaster", charset="utf8", port=3306)

# default
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'WuRuihai'}
	title = 'PKUInfoMaster'
	return render_template('index.html', title=title, user=user)


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
def bbs_date_query(year=2018, month=12, day=0):
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

# 查询BBS历史每日热点的路由
@app.route('/BBS/<int:YY>/<int:MM>/<int:DD>')
def BBSYMD(YY, MM, DD):
	bbsYMD_array = bbs_date_query(YY, MM, DD)
	bbs_history_array_json = json.dumps(bbsYMD_array, ensure_ascii=False)
	with open("bbs_history_record.json","w", encoding="utf8") as f:
		f.write(bbs_history_array_json)
	return bbs_history_array_json


# 查询百讲票务情况
def ticket_query(lmt=0):
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
	if (lmt == 0):
		results = ticket.select()
	else:
		results = ticket.select().limit(lmt)
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

# 查询票务情况的路由
@app.route('/TICKET')
def TICKET():
	ticket_array = ticket_query()
	ticket_array_json = json.dumps(ticket_array, ensure_ascii=False)
#	with open("ticket_record.json","w", encoding="utf8") as f:
#		f.write(ticket_array_json)
	return ticket_array_json


# 按天查询百讲票务
def ticket_date_query(year=2018, month=12, day=0):
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

	import time
	time_day = time.struct_time((year, month, day, 0, 0, 0, 0, 0, 0))
	date = time.strftime('%Y-%m-%d', time_day)

	results = ticket.select().where(ticket.date == date)

	ticket_history_array = []
	for array in results:
		date, time, place, title, price, status = array.date, array.time, array.place, array.title, array.price, array.status
		dic = {}
		dic["date"] = str(date)
		dic["time"] = str(time)
		dic["place"] = place
		dic["title"] = title
		dic["price"] = price
		dic["status"] = status
		ticket_history_array.append(dic)
	return ticket_history_array

# 按日期查询百讲票务的路由
@app.route('/TICKET/<int:YY>/<int:MM>/<int:DD>')
def TICKETYMD(YY, MM, DD):
	ticketYMD_array = ticket_date_query(YY, MM, DD)
	ticket_history_array_json = json.dumps(ticketYMD_array, ensure_ascii=False)
	#with open("ticket_history_record.json","w", encoding="utf8") as f:
	#	f.write(ticket_history_array_json)
	return ticket_history_array_json


# 查询就餐指数
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
	lth = len(canteen_array)
	for i in range(lth - 1):
		for j in range(i + 1, lth):
			ci = canteen_array[i]
			cj = canteen_array[j]
			if (float(ci["now"]) / float(ci["total"]) < float(cj["now"]) / float(cj["total"])):
				ck = ci.copy()
				canteen_array[i] = cj.copy()
				canteen_array[j] = ck
	return canteen_array

# 查询就餐指数的路由
@app.route('/CANTEEN')
def CANTEEN():
	canteen_array = canteen_query()
	canteen_array_json = json.dumps(canteen_array, ensure_ascii=False)
	with open("canteen_record.json","w", encoding="utf8") as f:
		f.write(canteen_array_json)
	return canteen_array_json


# 查询讲座情况
def lecture_query(lmt=0):
	class lecture(Model):
		id = IntegerField()
		title = CharField()
		speaker = CharField()
		place = CharField()
		date = DateField()
		time = TimeField()
		faculty = CharField()
		school = CharField()
		label = CharField()
		class Meta:
			database = db

	lecture_array = []
	if (lmt == 0):
		results = lecture.select().order_by(lecture.date.desc())
	else:
		results = lecture.select().order_by(lecture.date.desc()).limit(lmt)

	today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	for array in results:
		title, speaker, place, date, times, faculty, school, label = array.title, array.speaker, array.place, array.date, array.time, array.faculty, array.school, array.label
		if str(date) < today:
			break
		dic = {}
		dic["title"] = title
		dic["speaker"] = speaker
		dic["place"] = place
		dic["date"] = str(date)
		dic["time"] = str(times)
		dic["faculty"] = faculty
		dic["school"] = school
		dic["label"] = label
		lecture_array.append(dic)
	return lecture_array

# 讲座情况的路由
@app.route('/LECTURE')
def LECTURE():
	lecture_array = lecture_query()
	lecture_array_json = json.dumps(lecture_array, ensure_ascii=False)
	#with open("lecture_record.json","w", encoding="utf8") as f:
	#	f.write(lecture_array_json)
	return lecture_array_json


def hole_query(lmt=0):
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

	hole_array = []
	if (lmt == 0):
		results = hole.select().order_by(hole.key.desc())
	else:
		results = hole.select().order_by(hole.key.desc()).limit(lmt)

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
#	with open("hole_record.json","w", encoding="utf8") as f:
#		f.write(hole_array_json)
	return hole_array_json


# 查询树洞具体情况
def hole_reply_query(pid):
	class hole_reply(Model):
		id = IntegerField()
		cid = IntegerField()
		pid = IntegerField()
		text = CharField()
		name = CharField()
		class Meta:
			database = db

	hole_reply_array = []
	results = hole_reply.select().where(hole_reply.pid == pid)

	for array in results:
		pid, text, name = array.pid, array.text, array.name
		dic = {}
		dic["pid"] = pid
		dic["text"] = text
		dic["name"] = name
		hole_reply_array.append(dic)
	return hole_reply_array

# 查询树洞具体内容的路由
@app.route('/HOLE/<int:PID>')
def HOLE_REPLY(PID):
	hole_reply_array = hole_reply_query(PID)
	hole_reply_array_json = json.dumps(hole_reply_array, ensure_ascii=False)
	#with open("hole_reply_record.json","w", encoding="utf8") as f:
	#	f.write(hole_reply_array_json)
	return hole_reply_array_json


# 查询教室的空闲情况
def classroom_query():
	class classroom(Model):
		id = IntegerField()
		building = CharField(max_length=256)
		room = CharField(max_length=256)
		capacity = IntegerField()
		info = CharField(max_length=256)
		class Meta:
			database = db

	classroom_array = []
	results = classroom.select()
	for array in results:
		building, room, capacity, info = array.building, array.room, array.capacity, array.info
		dic = {}
		dic["building"] = building
		dic["room"] = room
		dic["capacity"] = capacity
		dic["info"] = info
		classroom_array.append(dic)
	return classroom_array

# 查询教室的空闲情况的路由
@app.route('/CLASSROOM')
def CLASSROOM():
	classroom_array = classroom_query()
	classroom_array_json = json.dumps(classroom_array, ensure_ascii=False)
	#with open("classroom_record.json","w", encoding="utf8") as f:
	#	f.write(classroom_array_json)
	return classroom_array_json


def main_query():
	main_array = {}
	lecture_array = lecture_query(3)
	main_array["LECTURE"] = lecture_array
	hole_array = hole_query(3)
	main_array["HOLE"] = hole_array
	bbs_array = bbs_query(3)
	main_array["BBS"] = bbs_array
	ticket_array = ticket_query(3)
	main_array["TICKET"] = ticket_array

	return main_array

@app.route('/MAIN')
def MAINPAGE():
	main_array = main_query()
	main_array_json = json.dumps(main_array, ensure_ascii=False)
	#with open("main_record.json","w", encoding="utf8") as f:
	#	f.write(main_array_json)
	return main_array_json


#coding=gbk
from app import app
from peewee import *
import json
from .config import db


# 查询百讲票务情况
def ticket_query():
	class ticket(Model):
		id = IntegerField()
		date = DateField()
		time = TimeField()
		place = CharField()
		title = CharField()
		price = CharField()
		status = CharField()
		startdate = DateField()
		link = CharField()
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


# 查询百讲票务情况
def ticket_main_date_query(year=2018, month=12, day=0, lmt=0):
	class ticket(Model):
		id = IntegerField()
		date = DateField()
		time = TimeField()
		place = CharField()
		title = CharField()
		price = CharField()
		status = CharField()
		startdate = DateField()
		class Meta:
			database = db

	import time
	time_day = time.struct_time((year, month, day, 0, 0, 0, 0, 0, 0))
	date = time.strftime('%Y-%m-%d', time_day)

	ticket_array = []
	if (lmt == 0):
		results = ticket.select().where(ticket.startdate == date)
	else:
		results = ticket.select().where(ticket.startdate == date).limit(lmt)
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


# 查询票务情况的路由
@app.route('/TICKET')
def TICKET():
	ticket_array = ticket_query()
	ticket_array_json = json.dumps(ticket_array, ensure_ascii=False)
#	with open("ticket_record.json","w", encoding="utf8") as f:
#		f.write(ticket_array_json)
	return ticket_array_json


# 按日期查询百讲票务的路由
@app.route('/TICKET/<int:YY>/<int:MM>/<int:DD>')
def TICKETYMD(YY, MM, DD):
	ticketYMD_array = ticket_date_query(YY, MM, DD)
	ticket_history_array_json = json.dumps(ticketYMD_array, ensure_ascii=False)
	#with open("ticket_history_record.json","w", encoding="utf8") as f:
	#	f.write(ticket_history_array_json)
	return ticket_history_array_json


# 查询TICKET每日新增演出的路由
@app.route('/TICKET/MAIN/<int:YY>/<int:MM>/<int:DD>')
def TICKETMAINYMD(YY, MM, DD):
	ticketYMD_array = ticket_main_date_query(YY, MM, DD, 10)
	ticket_history_array_json = json.dumps(ticketYMD_array, ensure_ascii=False)
	#with open("bbs_history_record.json","w", encoding="utf8") as f:
	#	f.write(bbs_history_array_json)
	return ticket_history_array_json
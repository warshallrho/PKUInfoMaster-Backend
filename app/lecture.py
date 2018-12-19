#coding=gbk
from app import app
from peewee import *
import json
import time
from .config import db


# 查询讲座情况
def lecture_query():
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
		pid = IntegerField()
		class Meta:
			database = db

	lecture_array = []
	results = lecture.select().order_by(lecture.date.desc())

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


# 按天查询百讲票务
def lecture_date_query(year=2018, month=12, day=0, lmt=0):
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
		pid = IntegerField()
		class Meta:
			database = db

	import time
	time_day = time.struct_time((year, month, day, 0, 0, 0, 0, 0, 0))
	date = time.strftime('%Y-%m-%d', time_day)

	if (lmt == 0):
		results = lecture.select().where(lecture.date == date)
	else:
		results = lecture.select().where(lecture.date == date).limit(lmt)

	lecture_history_array = []
	for array in results:
		title, speaker, place, date, times, faculty, school, label = array.title, array.speaker, array.place, array.date, array.time, array.faculty, array.school, array.label
		dic = {}
		dic["title"] = title
		dic["speaker"] = speaker
		dic["place"] = place
		dic["date"] = str(date)
		dic["time"] = str(times)
		dic["faculty"] = faculty
		dic["school"] = school
		dic["label"] = label
		lecture_history_array.append(dic)
	return lecture_history_array


# 讲座情况的路由
@app.route('/LECTURE')
def LECTURE():
	lecture_array = lecture_query()
	lecture_array_json = json.dumps(lecture_array, ensure_ascii=False)
	#with open("lecture_record.json","w", encoding="utf8") as f:
	#	f.write(lecture_array_json)
	return lecture_array_json


# 讲座按日期路由
@app.route('/LECTURE/<int:YY>/<int:MM>/<int:DD>')
def LECTUREYMD(YY, MM, DD):
	lectureYMD_array = lecture_date_query(YY, MM, DD)
	lecture_history_array_json = json.dumps(lectureYMD_array, ensure_ascii=False)
	#with open("lecture_history_record.json","w", encoding="utf8") as f:
	#	f.write(lecture_history_array_json)
	return lecture_history_array_json

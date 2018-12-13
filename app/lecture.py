#coding=gbk
from app import app
from peewee import *
import json
import time
from .config import db


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


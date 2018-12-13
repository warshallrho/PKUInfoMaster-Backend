#coding=gbk
from app import app
from peewee import *
import json
from .config import db

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
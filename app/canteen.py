#coding=gbk
from app import app
from peewee import *
import json
from .config import db


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

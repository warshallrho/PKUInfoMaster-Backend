#coding=gbk
from app import app
from peewee import *
import json
from .config import db


# ��ѯ���ҵĿ������
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
	d = {}
	buildings = ["һ��", "����", "����", "�Ľ�", "���", "��ʷ", "���", "��ѧ", "��ѧ", "����", "����", "��ѧ", "����", "�������"]
	for building in buildings:
		building_array = []
		results = classroom.select().where(classroom.building == building)
		for array in results:
			room, capacity, info = array.room, array.capacity, array.info
			dic = {}
			dic["room"] = room
			dic["capacity"] = capacity
			for i in range(12):
				if info[i] == "0":
					dic["c" + str(i+1)] = ""
				else:
					dic["c" + str(i+1)] = "ռ��"
			building_array.append(dic)
		d[building] = building_array
	classroom_array.append(d)
	return classroom_array


# ��ѯ���ҵĿ��������·��
@app.route('/CLASSROOM')
def CLASSROOM():
	classroom_array = classroom_query()
	classroom_array_json = json.dumps(classroom_array, ensure_ascii=False)
	#with open("classroom_record.json","w", encoding="utf8") as f:
	#	f.write(classroom_array_json)
	return classroom_array_json

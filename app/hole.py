#coding=gbk
from app import app
from peewee import *
import json
import time
from .config import db


# ��ѯ�����������
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


# ��ѯĳһ��������ȵ�
def hole_date_query(year=2018, month=12, day=0, lmt=5):
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

	time_day = time.struct_time((year, month, day, 0, 0, 0, 0, 0, 0))
	date = time.strftime('%Y-%m-%d', time_day)

	hole_array = []
	results = hole.select().where(hole.date == date).order_by(hole.key.desc()).limit(lmt)

	for array in results:
		pid, text, reply, likenum = array.pid, array.text, array.reply, array.likenum
		dic = {}
		dic["pid"] = pid
		dic["text"] = text
		dic["reply"] = reply
		dic["likenum"] = likenum
		hole_array.append(dic)
	return hole_array


def hole_like_query(ST):
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

	s = "%" + ST + "%"
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	results = hole.select().where(hole.date == date, hole.text ** s)
	hole_like_array = []

	for array in results:
		pid, text, reply, likenum = array.pid, array.text, array.reply, array.likenum
		dic = {}
		dic["pid"] = pid
		dic["text"] = text
		dic["reply"] = reply
		dic["likenum"] = likenum
		hole_like_array.append(dic)
	return hole_like_array


# ��ѯ�����ظ�
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


# ��ѯ�������������·��
@app.route('/HOLE')
def HOLE():
	hole_array = hole_query()
	hole_array_json = json.dumps(hole_array, ensure_ascii=False)
#	with open("hole_record.json","w", encoding="utf8") as f:
#		f.write(hole_array_json)
	return hole_array_json


# ��ѯ������ʷÿ���ȵ��·��
@app.route('/HOLE/<int:YY>/<int:MM>/<int:DD>')
def HOLEYMD(YY, MM, DD):
	holeYMD_array = hole_date_query(YY, MM, DD, 10)
	hole_history_array_json = json.dumps(holeYMD_array, ensure_ascii=False)
	#with open("hole_history_record.json","w", encoding="utf8") as f:
	#	f.write(hole_history_array_json)
	return hole_history_array_json


# ��ѯ�����ظ���·��
@app.route('/HOLE/<int:PID>')
def HOLE_REPLY(PID):
	hole_reply_array = hole_reply_query(PID)
	hole_reply_array_json = json.dumps(hole_reply_array, ensure_ascii=False)
	#with open("hole_reply_record.json","w", encoding="utf8") as f:
	#	f.write(hole_reply_array_json)
	return hole_reply_array_json


# ��������·��
@app.route('/HOLE/SEARCH/<string:ST>')
def HOLESEARCH(ST):
	hole_like_array = hole_like_query(ST)
	hole_like_array_json = json.dumps(hole_like_array, ensure_ascii=False)
	#with open("hole_like_record.json","w", encoding="utf8") as f:
	#	f.write(hole_like_array_json)
	return hole_like_array_json
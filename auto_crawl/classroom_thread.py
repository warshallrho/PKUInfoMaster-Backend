from crawler import classroom_crawler as classroom_crawler
from config import db
from peewee import *


def classroom():
	class classroom(Model):
		id = IntegerField()
		building = CharField(max_length=256)
		room = CharField(max_length=256)
		capacity = IntegerField()
		info = CharField(max_length=256)
		class Meta:
			database = db

	buildings, rooms, capacitys, infos = classroom_crawler.crawler()
	t = classroom.delete()
	t.execute()

	for i in range(len(buildings)):
		building = buildings[i]
		room = rooms[i]
		capacity = capacitys[i]
		info = infos[i]

		t = classroom.insert(building=building, room=room, capacity=capacity, info=info)
		t.execute()

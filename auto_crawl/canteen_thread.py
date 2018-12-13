from .crawler import canteen_crawler as canteen_crawler
from ..app.config import db
from peewee import *

def canteen():
	class canteen(Model):
		id  = IntegerField()
		name = CharField()
		total = IntegerField()
		now = IntegerField()
		class Meta:
			database = db

	numbers = canteen_crawler.crawler()
	names = ["畅春园", "农园", "勺园", "佟园", "万柳", "学五", "学一", "燕南美食", "艺园"]
	totals = [458, 1816, 1044, 98, 740, 515, 512, 288, 382]

	try:
		t = canteen.get(canteen.id == 1)
		# t.execute()
		for i in range(9):
			t = canteen.update(now=numbers[i]).where(canteen.id == i+1)
			t.execute()

	except canteen.DoesNotExist:
		for i in range(9):
			name = names[i]
			total = totals[i]
			now = numbers[i]
			t = canteen.insert(name=name, total=total, now=now)
			t.execute()

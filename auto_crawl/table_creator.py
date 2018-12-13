from peewee import *
from ..app.config import db


def create_tables():
	class bbs(Model):
		title = CharField(max_length=256)
		board = CharField(max_length=256)
		author = CharField(max_length=256)
		link = CharField(max_length=256)

		class Meta:
			database = db

	class bbs_history(Model):
		title = CharField(max_length=256)
		board = CharField(max_length=256)
		author = CharField(max_length=256)
		link = CharField(max_length=256)
		date = DateField()
		count = IntegerField()

		class Meta:
			database = db

	class canteen(Model):
		name = CharField(max_length=256)
		total = IntegerField()
		now = IntegerField()

		class Meta:
			database = db

	class lecture(Model):
		title = CharField(max_length=256)
		speaker = CharField(max_length=256)
		place = CharField(max_length=256)
		date = DateField()
		time = TimeField()
		faculty = CharField(max_length=256)
		school = CharField(max_length=256)
		label = CharField(max_length=256)
		pid = IntegerField()

		class Meta:
			database = db

	class ticket(Model):
		date = DateField()
		time = TimeField()
		place = CharField(max_length=256)
		title = CharField(max_length=256)
		price = CharField(max_length=256)
		status = CharField(max_length=256)
		startdate = DateField()

		class Meta:
			database = db

	class hole(Model):
		pid = IntegerField()
		text = TextField()
		reply = IntegerField()
		likenum = IntegerField()
		date = DateField()
		key = IntegerField()

		class Meta:
			database = db

	class hole_reply(Model):
		cid = IntegerField()
		pid = IntegerField()
		text = TextField()
		name = CharField(max_length=256)

		class Meta:
			database = db

	class classroom(Model):
		building = CharField(max_length=256)
		room = CharField(max_length=256)
		capacity = IntegerField()
		info = CharField(max_length=256)

		class Meta:
			database = db

	bbs.create_table()
	bbs_history.create_table()
	canteen.create_table()
	lecture.create_table()
	ticket.create_table()
	hole.create_table()
	hole_reply.create_table()
	classroom.create_table()


def create_table():
	create_tables()

if __name__ == "__main__":
	create_table()

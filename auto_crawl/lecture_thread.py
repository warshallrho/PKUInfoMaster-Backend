from crawler import lecture_crawler as lecture_crawler
from peewee import *
from config import db


def lecture():
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

	titles, speakers, places, dates, times, faculties, schools, labels, pids = lecture_crawler.crawler()

	for i in range(len(titles)):
		title = titles[i]
		speaker = speakers[i]
		place = places[i]
		date = dates[i]
		time = times[i]
		faculty = faculties[i]
		school = schools[i]
		label = labels[i]
		pid = pids[i]

		try:
			t = lecture.get(lecture.pid == pid)

		except lecture.DoesNotExist:
			t = lecture.insert(title=title, speaker=speaker, place=place, date=date, time=time, faculty=faculty, school=school, label=label, pid=pid)
			t.execute()

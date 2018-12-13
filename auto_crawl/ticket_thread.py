from .crawler import ticket_crawler as ticket_crawler
from ..app.config import db
from peewee import *


def ticket():
	class ticket(Model):
		id = IntegerField()
		date = DateField()
		time = TimeField()
		place = CharField()
		title = CharField()
		price = CharField()
		status = CharField()
		startdate = DateField()
		class Meta:
			database = db

	dates, times, places, titles, prices, statuses, startdates = ticket_crawler.crawler()

	t = ticket.delete()
	t.execute()

	for i in range(len(dates)):
		date = dates[i]
		time = times[i]
		place = places[i]
		title = titles[i]
		price = prices[i]
		status = statuses[i]
		startdate = startdates[i]

		t = ticket.insert(date=date, time=time, place=place, title=title, price=price, status=status, startdate=startdate)
		t.execute()

import crawler.bbs_crawler as bbs_crawler
import crawler.canteen_crawler as canteen_crawler
import crawler.lecture_crawler as lecture_crawler
import crawler.ticket_crawler as ticket_crawler
import crawler.hole_crawler as hole_crawler
import crawler.hole_reply_crawler as hole_reply_crawler
import crawler.classroom_crawler as classroom_crawler
import json
import time
import threading
from peewee import *

passwd = input("password: ")
db = MySQLDatabase(host="127.0.0.1", user="root", passwd=passwd, database="pkuinfomaster", charset="utf8mb4", port=3306)

bbs_time = 1800
canteen_time = 1800
lecture_time = 1800
ticket_time = 1800
hole_time = 1800
classroom_time = 1800

bbs_timer = None
canteen_timer = None
lecture_timer = None
ticket_timer = None
hole_timer = None
classroom_timer = None

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

def bbs():
	class bbs(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		class Meta:
			database = db

	titles, boards, authors, links = bbs_crawler.crawler()

	t = bbs.delete()
	t.execute()

	for i in range(100):
		title = titles[i]
		board = boards[i]
		author = authors[i]
		link = links[i]

		t = bbs.insert(id=i+1, title=title, board=board, author=author, link=link)
		t.execute()

	bbs_history(titles, boards, authors, links)

def bbs_history(titles, boards, authors, links):
	class bbs_history(Model):
		id  = IntegerField()
		title = CharField()
		board = CharField()
		author = CharField()
		link = CharField()
		date = DateField()
		count = IntegerField()
		class Meta:
			database = db

	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	for i in range(10):
		title = titles[i]
		board = boards[i]
		author = authors[i]
		link = links[i]
		try:
			t = bbs_history.get(bbs_history.link == link, bbs_history.date == date)
			count = t.count + 1
			t = bbs_history.update(count=count).where(bbs_history.link == link, bbs_history.date == date)
			t.execute()

		except bbs_history.DoesNotExist:
			t = bbs_history.insert(title=title, board=board, author=author, link=link, date=date, count=1)
			t.execute()

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
		for i in range(9):
			t =canteen.update(now=numbers[i]).where(canteen.id == i+1)
			t.execute()

	except canteen.DoesNotExist:
		for i in range(9):
			name = names[i]
			total = totals[i]
			now = numbers[i]
			t = canteen.insert(name=name, total=total, now=now)
			t.execute()

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
		class Meta:
			database = db

	titles, speakers, places, dates, times, faculties, schools, labels = lecture_crawler.crawler()

	t = lecture.delete()
	t.execute()

	for i in range(len(titles)):
		title = titles[i]
		speaker = speakers[i]
		place = places[i]
		date = dates[i]
		time = times[i]
		faculty = faculties[i]
		school = schools[i]
		label = labels[i]

		t = lecture.insert(title=title, speaker=speaker, place=place, date=date, time=time, faculty=faculty, school=school, label=label)
		t.execute()

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

def hole():
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

	pids, texts, replys, likenums = hole_crawler.crawler()
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	for i in range(len(pids)):
		pid = pids[i]
		text = texts[i]
		reply = replys[i]
		likenum = likenums[i]
		try:
			t = hole.get(hole.pid == pid)
			if t.likenum != likenum or t.reply != reply:
				t = hole.update(likenum=likenum, reply=reply, date=date, key=reply + likenum).where(hole.pid == pid)
				t.execute()
				hole_reply(pid)

		except hole.DoesNotExist:
			t = hole.insert(pid=pid, text=text, reply=reply, likenum=likenum, date=date, key=reply + likenum)
			t.execute()
			hole_reply(pid)
			
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

'''def hole_reply_delete():
	class hole_reply(Model):
		id = IntegerField()
		pid = IntegerField()
		text = CharField()
		name = CharField()
		class Meta:
			database = db

	t = hole_reply.delete()
	t.execute()
'''

def hole_reply(pid):
	class hole_reply(Model):
		id = IntegerField()
		cid = IntegerField()
		pid = IntegerField()
		text = CharField()
		name = CharField()
		class Meta:
			database = db

	cids, texts, names = hole_reply_crawler.crawler(pid)

	#print(pid)

	for i in range(len(cids)):
		cid = cids[i]
		text = texts[i]
		name = names[i]
		try:
			t = hole_reply.get(hole_reply.cid == cid)

		except hole_reply.DoesNotExist:
			t = hole_reply.insert(cid=cid, pid=pid, text=text, name=name)
			t.execute()
		
def bbs_func():
	print("bbs")
	bbs()
	global bbs_timer
	bbs_timer = threading.Timer(bbs_time, bbs_func)
	bbs_timer.start()

def canteen_func():
	print("canteen")
	canteen()
	global canteen_timer
	canteen_timer = threading.Timer(canteen_time, canteen_func)
	canteen_timer.start()

def lecture_func():
	print("lecture")
	lecture()
	global lecture_timer
	lecture_timer = threading.Timer(lecture_time, lecture_func)
	lecture_timer.start()

def ticket_func():
	print("ticket")
	ticket()
	global ticket_timer
	ticket_timer = threading.Timer(ticket_time, ticket_func)
	ticket_timer.start()
	
def hole_func():
	print("hole")
	hole()
	global hole_timer
	hole_timer = threading.Timer(hole_time, hole_func)
	hole_timer.start()
	
def classroom_func():
	print("classroom")
	classroom()
	global hole_timer
	classroom_timer = threading.Timer(classroom_time, classroom_func)
	classroom_timer.start()

create_tables()
hole_func()
bbs_func()
canteen_func()
classroom_func()
ticket_func()
lecture_func()



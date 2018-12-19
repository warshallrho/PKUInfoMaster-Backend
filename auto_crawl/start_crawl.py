from bbs_thread import bbs
from classroom_thread import classroom
from ticket_thread import ticket
from hole_thread import hole
from canteen_thread import canteen
from lecture_thread import lecture

import threading


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


def bbs_func():
	print("initial_bbs")
	bbs()
	global bbs_timer
	bbs_timer = threading.Timer(bbs_time, bbs_func)
	bbs_timer.start()


def canteen_func():
	print("initial_canteen")
	canteen()
	global canteen_timer
	canteen_timer = threading.Timer(canteen_time, canteen_func)
	canteen_timer.start()


def lecture_func():
	print("initial_lecture")
	lecture()
	global lecture_timer
	lecture_timer = threading.Timer(lecture_time, lecture_func)
	lecture_timer.start()


def ticket_func():
	print("initial_ticket")
	ticket()
	global ticket_timer
	ticket_timer = threading.Timer(ticket_time, ticket_func)
	ticket_timer.start()


def hole_func():
	print("initial_hole")
	hole()
	global hole_timer
	hole_timer = threading.Timer(hole_time, hole_func)
	hole_timer.start()


def classroom_func():
	print("initial_classroom")
	classroom()
	global classroom_timer
	classroom_timer = threading.Timer(classroom_time, classroom_func)
	classroom_timer.start()


#if __name__ == "__main__":
lecture_func()
bbs_func()
hole_func()
canteen_func()
classroom_func()
ticket_func()

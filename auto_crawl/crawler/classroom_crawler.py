import requests
import json
import random

all_buildings = ["一教", "二教", "三教", "四教", "理教", "文史", "电教", "哲学", "地学", "国关", "政管", "化学", "电子", "电教听力"]

para = {"buildingName": "", "time": "今天"}

#cookies={"JSESSIONID": "F8AE754B35FFBA0BCF43068DE87D6BA4", "UM_distinctid": "1663a9dc24b0-043f5a1930fc8c-8383268-144000-1663a9dc24c7da", "_astraeus_session": "WXFLVkd2N0s5THBQUldzYWpUOU5qZWlTSDh6YVpvQVBhVTBHc0wrWFVBTEMrTzJLTXk4QXllOHJNN2VzZUJ6U3d2TzNLaWgzVUh3TkJuMXhBQzVycklNdU4ybGkzNGlYR045aldCb0JIcjJOdC9PVjZYRFhVT1lmZ21kSWVsZjAzR2QrQkxUZ0lvQlFvenlkM2ZsdWYxVDQ2aTJMTVlneDI4U2pxRmVaVWtSR2J2dTNQcjJWODZtVGt5b2hwZ1Q0NGZZMU9yc05XVVA2Q3VHWERPN1pqc3BDNW0rcGQrb0dLb0dBcWRmakF6YXowQllOOWI0SURtWmFleEQvRHNoSnc2VFAwM01iUG5yZmxzY3EyUVpJVDJQRnQrT0ZUR0lmYzUrdXRZalpMSTNoVDRIUDJ2VjVNQk5JeHo2ZXh1NW80SzNvbHF4ZDFta2pxano3TGhYMVhNZHA0VkNNdHVtM2FIcUtIWXdpMFNlcXBsL2s4V2Q4RFFudGJmLzhDWEhmbGJwS0ZJZy9zNHZFWTN3OVRVMlNZYUJ4RzgrdG5lWGNBTkJMQ1FoSWlyRkk1a215Yi9TU0psVUd1ZlQ5TVduZS0tN0NpdzNVQXdoVFd2enJ3aFJGNGJCUT09--652de24fb5ebcffdd6eafe526733ba00c773030a", "_ga": "GA1.3.1746632523.1524661182"}

cookies = 0

buildings = []
rooms = []
capacitys = []
infos = []

def login():
	url = "https://iaaa.pku.edu.cn/iaaa/oauthlogin.do"
	redirect = "https://w.pku.edu.cn/users/auth/pkuauth/callback"
	data = {"appid": "webvpn", "userName": "1600012836", "password": "lsh971101", "redirUrl": redirect}
	session = requests.session()
	r = session.post(url, data=data)
	token = json.loads(r.text, strict=False)["token"]
	rand = random.random()
	para = {"rand": rand, "token": token}
	r = session.get(redirect, params=para)
	return session

def crawler():
	print("classroom start!")
	session = login()

	for building in all_buildings:
		para["buildingName"] = building
		r = session.get("https://portal.w.pku.edu.cn/portal2017/publicsearch/classroom/retrClassRoomFree.do", params=para)
		array = json.loads(r.text, strict=False)["rows"]
		for room in array:
			buildings.append(building)
			rooms.append(room["room"])
			capacitys.append(int(room["cap"]))
			s = ""
			for i in range(12):
				if room["c" + str(i+1)] == "":
					s = s + "0"
				else:
					s = s + "1"
			infos.append(s)

	print("classroom end!")
	
	return buildings, rooms, capacitys, infos

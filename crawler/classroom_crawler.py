import requests
import json

classrooms = ["一教", "二教", "三教", "四教", "理教", "文史", "电教", "哲学", "地学", "国关", "政管", "化学", "电子", "电教听力"]

para = {"buildingName": "", "time": "今天"}

buildings = []
rooms = []
capacitys = []
infos = []

def crawler():
	for building in classrooms:
		para["buildingName"] = building
		r = requests.get("https://portal.pku.edu.cn/portal2017/publicsearch/classroom/retrClassRoomFree.do", params=para)
		array = json.loads(r.text)["rows"]
		for room in array:
			buildings.append(building)
			rooms.append(room["room"])
			capacitys.append(room["cap"])
			s = ""
			for i in range(12):
				if room["c" + str(i+1)] == "":
					s = s + "0"
				else:
					s = s + "1"
			infos.append(s)
	return buildings, rooms, capacitys, infos
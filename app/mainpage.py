#coding=gbk
from app import app
import json
from pprint import pprint
from .hole import hole_date_query
from .bbs import bbs_date_query
from .ticket import ticket_main_date_query
from .lecture import lecture_date_query


# 推送主页信息
def main_query(YY, MM, DD):
	main_array = {}
	#lecture_array = lecture_query_main(3)
	#main_array["LECTURE"] = lecture_array
	hole_array = hole_date_query(YY, MM, DD, 5)
	main_array["HOLE"] = hole_array
	bbs_array = bbs_date_query(YY, MM, DD, 5)
	main_array["BBS"] = bbs_array
	ticket_array = ticket_main_date_query(YY, MM, DD, 5)
	main_array["TICKET"] = ticket_array
	lecture_array = lecture_date_query(YY, MM, DD, 5)
	main_array["LECTURE"] = lecture_array

	#main_all_json = json.dumps(main_array, ensure_ascii=False)
	#with open("main_all.json","w", encoding="utf8") as f:
	#	f.write(main_all_json)

	# pprint(main_array)

	return main_array

@app.route('/MAIN/<int:YY>/<int:MM>/<int:DD>')
def MAINPAGE(YY, MM, DD):
	main_array = main_query(YY, MM, DD)
	main_array_json = json.dumps(main_array, ensure_ascii=False)
	#with open("main_record.json","w", encoding="utf8") as f:
	#	f.write(main_array_json)
	return main_array_json

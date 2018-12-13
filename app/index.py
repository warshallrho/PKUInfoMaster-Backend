#coding=gbk
from app import app


# index
@app.route('/')
@app.route('/index')
def index():
	return "PKU InfoMaster"

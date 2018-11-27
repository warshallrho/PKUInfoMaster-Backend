#coding=gbk
from flask import Flask

app = Flask(__name__)
#app.config['DEBUG'] = False
#if __name__ == "__main__"
#	app.run(host='0.0.0.0',port=80)

from app import routes

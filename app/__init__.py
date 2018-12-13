#coding=gbk
from flask import Flask

app = Flask(__name__)

from . import index
from . import mainpage
from . import classroom
from . import lecture
from . import hole
from . import canteen
from . import bbs

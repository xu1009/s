# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib,json
from lxml import etree
import connectData
import re
from sae.storage import Bucket,Connection

class Tst1:
	def GET(self):
		session = web.config._session    ##这个session的存储就是将sessionID和session的内容存储到数据库，sae没有直接的权限将数据存储到本地，每次请求会通过cookie传递过来sessionid
		session.count = '2'
		return session.count
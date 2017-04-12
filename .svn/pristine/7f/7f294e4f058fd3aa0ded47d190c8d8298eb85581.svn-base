# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import connectData
import re
class Login:
	def __init__(self):
			self.app_root = os.path.dirname(__file__)
			self.templates_root = os.path.join(self.app_root, 'templates')
			self.render = web.template.render(self.templates_root)
	def GET(self):
		return self.render.login()
	def POST(self):
		data = web.input(inputEmail3=[],inputPassword3=[])
		name = data.inputEmail3
		password = data.inputPassword3
		mes = (connectData.checkName(name[0].encode('utf-8'),password[0].encode('utf-8')))
		if mes == 'error':
			return '不存在该用户'
		if not len(mes):
			return '不存在该用户'
		else:
			if re.findall(r".+u'(.+)'.+",str(mes))[0]==password[0].encode('utf-8'):
				return 'allright'
			else:
				return '密码错误'
			#return mes

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
		#return self.render.login()

		if web.config._session.count == 'false':
			return self.render.login()
		else:
			raise web.redirect('http://1.deveple.applinzi.com/main')  ##重定向问题，请求转发是将当前的请求头信息全部转发到另一个服务，重定向只是简单的重新定位到那个url
	def POST(self):
		data = web.input(inputEmail3=[],inputPassword3=[])
		name = data.inputEmail3
		password = data.inputPassword3
		mes = (connectData.checkName(name[0].encode('utf-8'),password[0].encode('utf-8')))
		if mes == 'error':
			web.config._session.count = 'false'
			return '不存在该用户'
		if not len(mes):
			web.config._session.count = 'false'
			return '不存在该用户'
		else:
			if re.findall(r".+u'(.+)'.+",str(mes))[0]==password[0].encode('utf-8'):
				web.config._session.count = 'true'
				return 'allright'
			else:
				web.config._session.count = 'false'
				return '密码错误'
			#return mes

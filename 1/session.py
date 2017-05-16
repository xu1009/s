# -*- coding: utf-8 -*-
import hashlib
import web
import web.db
import sae.const
import lxml
import time
import os
import urllib2,json
from lxml import etree
import re
class TstSession:
	def __init__(self):
			self.app_root = os.path.dirname(__file__)
			self.templates_root = os.path.join(self.app_root,'templates')
			self.render = web.template.render(self.templates_root)
			self.db = web.database(dbn='mysql',host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT),user=sae.const.MYSQL_USER,passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB)
	def GET(self):
			return 'hello'
			
	
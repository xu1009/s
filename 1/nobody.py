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
class Nothing:
	def __init__(self):
			self.app_root = os.path.dirname(__file__)
			self.templates_root = os.path.join(self.app_root, 'templates')
			self.render = web.template.render(self.templates_root)
	def GET(self):
			return  self.render.oops()
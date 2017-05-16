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
import urllib
from sae.storage import Bucket,Connection 
class TTT:
	def GET(self):
		ip = web.ctx.ip
		return re.search(re.compile("\"ul1.{16}(.*?)</li>"), urllib.urlopen('http://www.ip138.com/ips138.asp?ip='+ip).read()).group(1)     
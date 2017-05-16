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
class TstUrl:
	def GET(self,name):
		if name=='1':    ##存储到tju1数据库
			ip = web.ctx.ip
			add = re.search(re.compile("\"ul1.{16}(.*?)</li>"), urllib.urlopen('http://www.ip138.com/ips138.asp?ip='+ip).read()).group(1).decode("gb2312").encode("utf-8")
			connectData.update_ip1(add)   
			data = web.input(pm25=[],pm10=[],tem=[],dam=[],co2=[],time=[],PM2510=[],PM0325=[])
			connectData.addtju(data.time[0].encode('utf-8'),'1',data.pm25[0].encode('utf-8'),data.pm10[0].encode('utf-8'),data.tem[0].encode('utf-8'),data.dam[0].encode('utf-8'),data.co2[0].encode('utf-8'),data.PM0325[0].encode('utf-8'),data.PM2510[0].encode('utf-8'))
			connectData.addtju(data.time[0].encode('utf-8'),'2',data.pm25[1].encode('utf-8'),data.pm10[1].encode('utf-8'),data.tem[1].encode('utf-8'),data.dam[1].encode('utf-8'),data.co2[1].encode('utf-8'),data.PM0325[1].encode('utf-8'),data.PM2510[1].encode('utf-8'))
			connectData.addtju(data.time[0].encode('utf-8'),'3',data.pm25[2].encode('utf-8'),data.pm10[2].encode('utf-8'),data.tem[2].encode('utf-8'),data.dam[2].encode('utf-8'),data.co2[2].encode('utf-8'),data.PM0325[2].encode('utf-8'),data.PM2510[2].encode('utf-8'))
			connectData.addtju(data.time[0].encode('utf-8'),'4',data.pm25[3].encode('utf-8'),data.pm10[3].encode('utf-8'),data.tem[3].encode('utf-8'),data.dam[3].encode('utf-8'),data.co2[3].encode('utf-8'),data.PM0325[3].encode('utf-8'),data.PM2510[3].encode('utf-8'))
			connectData.addtju(data.time[0].encode('utf-8'),'5',data.pm25[4].encode('utf-8'),data.pm10[4].encode('utf-8'),data.tem[4].encode('utf-8'),data.dam[4].encode('utf-8'),data.co2[4].encode('utf-8'),data.PM0325[4].encode('utf-8'),data.PM2510[4].encode('utf-8'))
			return data
		elif name=='2':
			return 'get 2'
		#return 'name:'+name ##通配符任意访问tju/(\d)的url都会被拦截
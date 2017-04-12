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
class NumOfFou:
	def __init__(self):
			self.app_root = os.path.dirname(__file__)
			self.templates_root = os.path.join(self.app_root, 'templates')
			self.render = web.template.render(self.templates_root)
			self.co2 = []
			self.rh = []
			self.tem = []
			self.pm25 = []
			self.pm10 = []
			self.time = []
			self.co2_f = []
			self.rh_f = []
			self.tem_f = []
			self.pm25_f = []
			self.pm10_f = []
			self.time_f = []
	def GET(self):
		for i in range(1,6):
				i = str(i)
				result_time = list(connectData.get_time(i))
				numOfData = len(result_time)
				result_co2 = list(connectData.get_co2(i))  # list
				result_tem = list(connectData.get_tem(i))
				result_dam = list(connectData.get_dam(i))
				result_pm25 = list(connectData.get_pm25(i))
				result_pm10 = list(connectData.get_pm10(i))
				for i in range(numOfData):
					self.tem.append(re.findall(r".+u'(.+)'.+", str(result_tem[i]))[0].replace('*', '.'))
					self.rh.append(re.findall(r".+u'(.+)'.+", str(result_dam[i]))[0].replace('*', '.').replace('%', ''))
					self.pm10.append(re.findall(r".+u'(.+)'.+", str(result_pm10[i]))[0].replace('*', '.'))
					self.pm25.append(re.findall(r".+u'(.+)'.+", str(result_pm25[i]))[0].replace('*', '.'))
					self.time.append(re.findall(r".+u'(.+)'.+", str(result_time[i]))[0])
					self.co2.append(re.findall(r".+u'(.+)'.+", str(result_co2[i]))[0])
				self.co2_f.append(self.co2)
				self.time_f.append(self.time)
				self.pm10_f.append(self.pm10)
				self.pm25_f.append(self.pm25)
				self.rh_f.append(self.rh)
				self.tem_f.append(self.tem)
				self.co2 = []
				self.tem = []
				self.co2 = []
				self.pm25 = []
				self.pm10 = []
				self.time = []
				self.rh = []
            # self.time.append(re.findall(r".+u'(.+).+'",result[1])[0])
		return self.render.roomOfFou(self.time_f, self.co2_f, self.pm10_f, self.pm25_f, self.rh_f,self.tem_f)	
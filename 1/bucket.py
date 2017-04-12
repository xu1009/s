# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import connectData
from sae.storage import Bucket,Connection
class TstBucket:
	def GET(self):		
		bbk = Connection()        
		buc = bbk.get_bucket('data')
		buc.put_object("roomone.txt","Time  CO2  Tem  RH  PM25  PM10\r\n")
		buc.put_object("roomtwo.txt","Time  CO2  Tem  RH  PM25  PM10\r\n")
		buc.put_object("roomthr.txt","Time  CO2  Tem  RH  PM25  PM10\r\n")
		buc.put_object("roomfou.txt","Time  CO2  Tem  RH  PM25  PM10\r\n")
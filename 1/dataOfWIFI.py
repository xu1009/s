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
class SaveData:      
	def GET(self):
            data = web.input(pm25=[],pm10=[],tem=[],dam=[],co2=[],time=[])
            bbk = Connection()        
            buc = bbk.get_bucket('data')
            orignalData1 = buc.get_object_contents('roomone.txt')
            orignalData2 = buc.get_object_contents('roomtwo.txt')
            orignalData3 = buc.get_object_contents('roomthr.txt')
            orignalData4 = buc.get_object_contents('roomfou.txt')
            newdata1 = orignalData1+data.time[0].encode('utf-8')+'  '+data.co2[0].encode('utf-8')+'  '+data.tem[0].encode('utf-8').replace('*','.')+'  '+data.dam[0].encode('utf-8').replace('*','.')+'  '+data.pm25[0].encode('utf-8').replace('*','.')+'  '+data.pm10[0].encode('utf-8').replace('*','.')+'\r\n'
            newdata2 = orignalData2+data.time[0].encode('utf-8')+'  '+data.co2[1].encode('utf-8')+'  '+data.tem[1].encode('utf-8').replace('*','.')+'  '+data.dam[1].encode('utf-8').replace('*','.')+'  '+data.pm25[1].encode('utf-8').replace('*','.')+'  '+data.pm10[1].encode('utf-8').replace('*','.')+'\r\n'
            newdata3 = orignalData3+data.time[0].encode('utf-8')+'  '+data.co2[2].encode('utf-8')+'  '+data.tem[2].encode('utf-8').replace('*','.')+'  '+data.dam[2].encode('utf-8').replace('*','.')+'  '+data.pm25[2].encode('utf-8').replace('*','.')+'  '+data.pm10[2].encode('utf-8').replace('*','.')+'\r\n'
            newdata4 = orignalData4+data.time[0].encode('utf-8')+'  '+data.co2[3].encode('utf-8')+'  '+data.tem[3].encode('utf-8').replace('*','.')+'  '+data.dam[3].encode('utf-8').replace('*','.')+'  '+data.pm25[3].encode('utf-8').replace('*','.')+'  '+data.pm10[3].encode('utf-8').replace('*','.')+'\r\n'
            buc.put_object("roomone.txt",newdata1)
            buc.put_object("roomtwo.txt",newdata2)
            buc.put_object("roomthr.txt",newdata3)
            buc.put_object("roomfou.txt",newdata4)
            #data = web.input()
            #return (data.pm25+' '+data.pm10+' '+data.tem+' '+data.dam+' '+data.co2)
            #connectData.addfk('123:4','1','22','33','33','ee','ff')
           # connectData.addfk(data.time.encode('utf-8'),'1',data.pm25.encode('utf-8'),data.pm10.encode('utf-8'),data.tem.encode('utf-8'),data.dam.encode('utf-8'),data.co2.encode('utf-8'))
            connectData.addfk(data.time[0].encode('utf-8'),'1',data.pm25[0].encode('utf-8'),data.pm10[0].encode('utf-8'),data.tem[0].encode('utf-8'),data.dam[0].encode('utf-8'),data.co2[0].encode('utf-8'))
            connectData.addfk(data.time[0].encode('utf-8'),'2',data.pm25[1].encode('utf-8'),data.pm10[1].encode('utf-8'),data.tem[1].encode('utf-8'),data.dam[1].encode('utf-8'),data.co2[1].encode('utf-8'))
            connectData.addfk(data.time[0].encode('utf-8'),'3',data.pm25[2].encode('utf-8'),data.pm10[2].encode('utf-8'),data.tem[2].encode('utf-8'),data.dam[2].encode('utf-8'),data.co2[2].encode('utf-8'))
            connectData.addfk(data.time[0].encode('utf-8'),'4',data.pm25[3].encode('utf-8'),data.pm10[3].encode('utf-8'),data.tem[3].encode('utf-8'),data.dam[3].encode('utf-8'),data.co2[3].encode('utf-8'))
            connectData.addfk(data.time[0].encode('utf-8'),'5',data.pm25[4].encode('utf-8'),data.pm10[4].encode('utf-8'),data.tem[4].encode('utf-8'),data.dam[4].encode('utf-8'),data.co2[4].encode('utf-8'))
            
            
            connectData.addfk1(data.time[0].encode('utf-8'),data.pm25[0].encode('utf-8'),data.pm10[0].encode('utf-8'),data.tem[0].encode('utf-8'),data.dam[0].encode('utf-8'),data.co2[0].encode('utf-8'))
            connectData.addfk2(data.time[0].encode('utf-8'),data.pm25[1].encode('utf-8'),data.pm10[1].encode('utf-8'),data.tem[1].encode('utf-8'),data.dam[1].encode('utf-8'),data.co2[1].encode('utf-8'))
            connectData.addfk3(data.time[0].encode('utf-8'),data.pm25[2].encode('utf-8'),data.pm10[2].encode('utf-8'),data.tem[2].encode('utf-8'),data.dam[2].encode('utf-8'),data.co2[2].encode('utf-8'))
            connectData.addfk4(data.time[0].encode('utf-8'),data.pm25[3].encode('utf-8'),data.pm10[3].encode('utf-8'),data.tem[3].encode('utf-8'),data.dam[3].encode('utf-8'),data.co2[3].encode('utf-8'))
            connectData.addfk5(data.time[0].encode('utf-8'),data.pm25[4].encode('utf-8'),data.pm10[4].encode('utf-8'),data.tem[4].encode('utf-8'),data.dam[4].encode('utf-8'),data.co2[4].encode('utf-8'))            
            
            
            
            
            
            
            
            #num = len(str(list(connectData.get_fkcontent())[0]))
            return (str(list(connectData.get_fkcontent())))
         
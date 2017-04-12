# coding: UTF-8
import os
import sae
import web
from weixinInterface import WeixinInterface
from dataOfWIFI import SaveData
from dataOfImg import ImgPrint
from deleteData import DeleteMysql
from mainpage import MainGUI
from nobody import Nothing
from num1 import NumOfOne
from num2 import NumOfTwo
from num3 import NumOfThr
from num4 import NumOfFou
from login import Login
from bucket import TstBucket
from creatmenu import CreatMenu
urls = (
	'/weixin','WeixinInterface',
	'/data','SaveData',
	'/','Login',
	'/delete','DeleteMysql',
    '/Datashow','ImgPrint',
    '/nothing','Nothing',
    '/roomone','NumOfOne',
    '/roomtwo','NumOfTwo',
    '/three','NumOfThr',
    '/four','NumOfFou',
    '/main','MainGUI',
    '/tst','TstBucket',
    '/delstorage','DelStorage',
    '/creat','CreatMenu'
    
)
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

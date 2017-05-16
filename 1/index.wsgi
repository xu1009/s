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
from num5 import NumOfFiv
from login import Login
from bucket import TstBucket
from creatmenu import CreatMenu
from tst import TstUrl
from tju1 import TJUONE
from t import TTT
from validation import Validation
import connectData
from tst1 import Tst1
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
    '/five','NumOfFiv',
    '/main','MainGUI',
    '/tst','TstBucket',
    '/delstorage','DelStorage',
    '/creat','CreatMenu',
    '/tju(\d)','TstUrl',
    '/tjuone(\d)','TJUONE',
    '/ttt','TTT',
    '/val','Validation',
	'/tst1','Tst1',
)
web.config.debug = False
app = web.application(urls, globals())
db = connectData.db
store = web.session.DBStore(db,'sessions')
session = web.session.Session(app, store,initializer={'count':'false'})  
web.config._session = session

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

   
application = sae.create_wsgi_app(app.wsgifunc())

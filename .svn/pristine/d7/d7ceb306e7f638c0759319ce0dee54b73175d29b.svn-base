# -*- coding: utf-8 -*-
import sae
import web
import sae.const
import urllib2
import urllib
import json
class CreatMenu:
    def GET(self):
        appid="wxd7c9865f2e806b6e"
        secret="2950ab66c90425ad2e865cc6f1641845"
        url='https://api.weixin.qq.com/cgi-bin/token?grant_type=''client_credential&appid=%s&secret=%s'% (appid,secret)
        response = urllib2.urlopen(url)
        html = response.read()
        tokeninfo = json.loads(html)
        token=tokeninfo['access_token']
        #return token
        postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "旅行",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
          ]
    } """   
        if isinstance(postJson,unicode):
             postJson = postJson.encode('utf-8')
        url1 = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % token
        #req = urllib2.Request(url1, postJson)
        response = urllib.urlopen(url=url1, data=postJson)
        return response.read()  
    
    
    
    
    
    
    
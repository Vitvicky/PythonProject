#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
from weibopy.auth import OAuthHandler  
from weibopy.api import API  
import ConfigParser  

auth = OAuthHandler('3028524014','660eb5d3feacc40d3bba28e0b9dcc50b') #你的应用的key和secret
auth.setToken('d7cf5c4d17156226a80b2b61a51f97d5','79b483a7a80e2a304ee0e227f5a83dc6')  #你从新浪获得的令牌token和密码tokensecret
api = API(auth)   #得到经过认证和授权的、能访问新浪资源的开发界面
#api.updat_status("Hello World")  #向你的帐号发一个微博，上新浪微博查看：“Hello World”
weibo = api.public_timeline()
for i in weibo:
    print weibo.text
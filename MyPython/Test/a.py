#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
   
from weibo import *  
   
def press_sina_weibo():  
   
    APP_KEY = '3028524014'  
    APP_SECRET = '660eb5d3feacc40d3bba28e0b9dcc50b'  
   
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  
      
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
    print client.get_authorize_url()  
      
    r = client.request_access_token(raw_input("input code:").strip())  
    client.set_access_token(r.access_token, r.expires_in)  
      
    print client.post.statuses__update(status=u'测试一下发送微博')  
      
if __name__ == '__main__':  
   press_sina_weibo()  

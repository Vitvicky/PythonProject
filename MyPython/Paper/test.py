#!/usr/bin/env python  
# -*- coding: utf-8 -*- 
from weibopy.auth import OAuthHandler  
from weibopy.api import API  
     
def get_sina_token():      
    #����Ӧ��ʱ�õ���App Key������  
    App_key = '3028524014'  
    App_secret = '660eb5d3feacc40d3bba28e0b9dcc50b'  
  
    #��Ȩ  
    auth_handler = OAuthHandler(App_key, App_secret)  
    auth_url = auth_handler.get_authorization_url()  
  
    print "Please open this url by your Browser:" + auth_url  
    verifier = raw_input('Please input PIN code get from above url: ').strip()  
      
    #�õ�token������  
    auth_handler.get_access_token(verifier)  
  
if __name__ == '__main__':  
    get_sina_token()  
# -*- coding: utf-8 -*-
'''
Created on 2013-2-5

@author: wzy
'''
import urllib2
import sys
import re
import base64
import time
import json
from urlparse import urlparse 


theurl = 'http://api.t.sina.com.cn/statuses/search.json?\count=%(count)d&\source=%(source_key)d&\q=%(query_string)s&\
needcount=%(needcount)s&\
starttime=%(starttime)d&\
endtime=%(endtime)d&\
filter_ori=%(filter_ori)d\
'
pass_day_length=7#how much day's data we will to search ,default is one week
search_para={
'count':1,
'source_key':3028524014,
'query_string':'iphone4',#搜索的关键字
'needcount':'true',
'starttime':time.time()-3600*24*pass_day_length,
'endtime':time.time(),
'filter_ori':5,
}
theurl=theurl%search_para
#theurl='http://api.t.sina.com.cn/statuses/search.json?source=77221908&q=asdf&needcount=10&starttime=1296028369&endtime=1298620369&filter_ori=5'
print 'theurl:',theurl
#province=
#city=
username = '王卓毅vitvicky'#微博用户名
password = '920115'#微博密码
base64string = base64.encodestring(
                '%s:%s' % (username, password))[:-1]
authheader =  "Basic %s" % base64string
req = urllib2.Request(theurl)
print "authheader:",authheader
req.add_header("Authorization", authheader)
try:
    handle = urllib2.urlopen(req)
except IOError, e:
    # here we shouldn't fail if the username/password is right
    print "It looks like the username or password is wrong."
    sys.exit(1)
thepage = handle.read()
print  "thepage:",thepage
res= json.read(thepage)


print type(res),res
print "====================The result of %d day's data===================="%pass_day_length
total_count = res['total_count_maybe']
result = res['results']
print 'total_count_maybe:',total_count
print 'result len:',len(result)
for row in result:
    text=row['text']
    print row['id']
    print text
    print row
print "====================end===================="
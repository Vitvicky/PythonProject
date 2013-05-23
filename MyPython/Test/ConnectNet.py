'''
Created on 2013-1-22

@author: wzy
'''
import httplib
con=httplib.HTTPConnection("www.baidu.com")
con.request("GET", "/index.html")
r=con.getresponse()
print r.status,r.reason
data=r.read()
print data
r.close()


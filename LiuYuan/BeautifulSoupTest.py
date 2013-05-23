#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
html=urllib.urlopen(r'http://beijing.homelink.com.cn/ershoufang/BJHD85460140.shtml')
text=html.read()
soup=BeautifulSoup(text)
content=soup.find('div',{"class":"xizhi"})
#cotent.findAll('p')
c=content.findAll('p')
def txt_wrap_by(start_str, end, txt):
    start = txt.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = txt.find(end, start)
        if end >= 0:
            return txt[start:end].strip()
c=str(c)
m=txt_wrap_by("<p>","<br />",c)
replace1='<span>/</span>'
m=re.sub(replace1,' ',m)
print m
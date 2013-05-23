#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
html=urllib.urlopen(r'http://beijing.homelink.com.cn/ershoufang/xqcj/BJHD85587502.shtml')
text=html.read()
soup=BeautifulSoup(text)
content=soup.find('td',{"class":"night"})
#pattern=r''
#cotent.findAll('p')
#c=content.findAll('p')

#[p.next_sibling.strip() for p in cotent.findAll('p')]
print content
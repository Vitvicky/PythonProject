#!/usr/bin/python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
html=urllib.urlopen(r'http://www.pjjs.sdu.edu.cn/yywz/submitquery.asp?studentname=201000130085&sub=%B2%E9%D1%AF')
text=html.read()
soup=BeautifulSoup(text)
content=soup.findAll('table')
content=str(content)
replace1='</font></td><td><font color="red" size="2">'
replace2='</font></td></tr><tr><td><font color="black" size="2">'
replace3='<table border="0"><tr><td><font color="black" size="2">'
replace4='</font></td></tr></table>'
m=re.sub(replace1,' ',content)
m1=re.sub(replace2,' ',m)
m2=re.sub(replace3,' ',m1)
m3=re.sub(replace4,' ',m2)
print m3
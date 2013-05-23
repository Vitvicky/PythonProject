#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
#查找单词
pattern='[a-zA-z]+'
word='"Hi,--I am XXX" he said.'
#txt=re.findall(pattern, word)
#print txt

pattern1=r'[.?\-",+]' #前面有\，所以-被转义
#print re.findall(pattern1,word)

def txt_wrap_by(start_str, end, txt):
    start = txt.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = txt.find(end, start)
        if end >= 0:
            return txt[start:end].strip()
        
c='<p>房源信息：2室1厅<span>/</span>东西<span>/</span>66平<span>/</span>中楼层(6层)<span>/</span>精装<span>/</span>2000塔楼<br />'
p=r'<p\.(.+)\.<br$'
m=re.match(p, c)
print m.group(1)
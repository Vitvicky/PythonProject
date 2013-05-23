#!/usr/bin/python
#coding=utf-8
from collections import Counter
import jieba.posseg as p
import jieba

class my_list(list):
    def __init__(self):
        list.__init__(self)
            
    def __str__(self):
        return "[%s]" % ",".join(self)
    
    
#mylist=my_list()
count={}
f=open("wzy-filter.txt")
line=f.readline()
while line:
    mylist=my_list()
    words=p.cut(line)
    for w in words:
     if(w.flag=="n" or w.flag=="ns"):
         #print w.word
         mylist.append(w.word) 
         #print mylist
    #print mylist
    for i in mylist: 
     if(count.has_key(i)):
                count[i]=count[i]+1
     else:
                count.setdefault(i,1)
    for key,value in count.items(): 
            if value>1:
               print key," ",value  
               #count.clear()
    #mylist.remove()
    print "================================="          
    line=f.readline()    
f.close()   
             
             
             
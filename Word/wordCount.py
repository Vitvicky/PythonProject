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
    
    
mylist=my_list()
count={}
#for index in range(1,2):
    #f=open("coments/CN-culture/("+str(index)+").txt")
f=open("wzy/5.txt")
line=f.read()
mylist=my_list()
words=p.cut(line)
for w in words:
        if(w.flag=="n" or w.flag=="ns"):
         mylist.append(w.word) 
for i in mylist: 
             if(count.has_key(i)):
                count[i]=count[i]+1
             else:
                count.setdefault(i,1)
for key,value in count.items(): 
              if value>1:
                 #print index;
                 print key," ",value 
                 #count.clear()
print "=================================" 

         
f.close()   
             
             
             
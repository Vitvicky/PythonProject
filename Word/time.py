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
    
    
count={}
for index in range(1,13):
    f=open("news/IT/"+str(index)+".txt")
    line=f.read()
#while line:
    mylist=my_list()
    words=p.cut(line)
    for w in words:
         #if(w.word=="精度" or w.word=="明朝" or w.word=="编程" or w.word=="美国" or w.word=="设计" or w.word=="软件" or w.word=="梦想" or w.word=="机器学习" or w.word=="数据" or w.word=="微软" or w.word=="管理" or w.word=="网络" or w.word=="程序员" or w.word=="实验室" or w.word=="大学" or w.word=="托福" or w.word=="数据挖掘" or w.word=="金融" or w.word=="商业" or w.word=="经济"):
         if(w.word=="编程" or w.word=="实验室" or w.word==" 程序员 " or w.word=="数据" or w.word=="机器学习 " or w.word=="软件" or w.word=="网络" or w.word=="数据挖掘"):
           mylist.append(w.word) 
    for i in mylist: 
         if(count.has_key(i)):
          count[i]=count[i]+1
         else:
          count.setdefault(i,1)
    for key,value in count.items(): 
        print index
        print key," ",value  
        count.clear()
    print "========================================================="
        #line=f.readline()    
f.close()   

            
             
             
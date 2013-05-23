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
for index in range(1,10):
    f=open("wzyreco/"+str(index)+".txt")
    line=f.read()
#while line:
    mylist=my_list()
    words=p.cut(line)
    for w in words:
        if(w.word=="经济" or w.word=="适用" or w.word=="不会" or w.word=="有钱 " or w.word=="平凡 " or w.word=="肯尼亚" or w.word=="转账" or w.word=="已经" or w.word=="经费" or w.word=="我们" or w.word=="课题  " or w.word=="科学家" or w.word=="科研"or w.word=="美国  "or w.word=="科研开发"or w.word=="研究 "or w.word=="资金"or w.word=="专利"or w.word=="塞浦路斯"or w.word=="管制"or w.word=="资本"or w.word=="这些 "or w.word=="银行  "or w.word=="市场 "or w.word=="股市 "or w.word=="美国  "or w.word=="以及 "or w.word=="上涨 "or w.word=="塞浦路斯" or w.word=="俄罗斯 " or w.word=="央行 " or w.word=="安倍 " or w.word=="通胀" or w.word=="目标"or w.word=="中国 " or w.word=="消费"or w.word=="官方"or w.word=="数据 " or w.word=="香港"):
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

            
             
             
#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pylab as plt
import numpy as np

#x=np.arange(1,5)
#plt.plot(x,x*1.5,x,x*3)
#plt.xlim(1,10)
#plt.ylim(1,10)
#plt.show()


#plt.figure(figsize=(5,5))
#x=[60,20,20]
#lables=['A','B','C']
#explode=[0.1,0.1,0.0]#离心值
#plt.pie(x,labels=lables,explode=explode,autopct='%1.1f%%')
#plt.show()

x=np.random.randn(1000)
y=np.random.randn(1000)
size=50*np.random.randn(1000)
color=np.random.rand(1000)
plt.scatter(x, y,s=size,c=color)#绘制散点图
plt.show()

'''
Created on 2013-1-20

@author: wzy
'''

path="G:/test.txt"
path1="G:/a.txt"
f=open(path,"w")  # Opens file for writing.Creates this file doesn't exist.
f.write("First line 1.\n")
f.writelines("Second line 2")
f.close()

f=open(path1,"r")# Opens file for reading
for i in f:
    print i
    
f.close()


'''
Created on 2013-2-1

@author: wzy
'''
import Image
from random import randint

def randomPalette(length, min, max):  
    return [ randint(min, max) for x in xrange(length)] 

img=Image.open("1.jpg").convert("L")  
l=randomPalette(768, 0, 255) 
img.putpalette(l)  
img.show() 

 
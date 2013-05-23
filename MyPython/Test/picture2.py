'''
Created on 2013-2-1

@author: wzy
'''
import Image
from Image import blend

im1=Image.open("a.jpg")
im2=Image.open("b.jpg")
im3=Image.blend(im1, im2, 0.5)
#im3=Image.composite(im1, im2, 1)
im3.show();
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:27:07 2019

@author: AS
"""
#silly pencil sketch
import numpy as np
import cv2
import matplotlib.pyplot as plt

THRESHOLD=100
 
#choose your file
img=cv2.imread('E:\\happysad\\happy\\hp.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',img)

h=img.shape[0]
w=img.shape[1]



#THRESHOLD=int(input())
 


for i in np.arange(h):
    for j in np.arange(w):
        pix=img.item(i,j)
        if pix>THRESHOLD:
            pix=250
        else:
            pix=20
        pix=1+pix
        img.itemset((i,j),pix)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

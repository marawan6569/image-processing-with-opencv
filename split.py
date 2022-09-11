import cv2
import numpy as np
img = cv2.imread('treka.jpg',1)
b,g,r = cv2.split(img)
cv2.imshow('image',img)
cv2.imshow('r',r)
cv2.imshow('g',g)
cv2.imshow('b',b)
i = cv2.merge((b,g,r))
cv2.imshow('i',i)
cv2.waitKey(0)
print(r)
cv2.destroyAllWindows()
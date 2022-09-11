import cv2
import numpy as np
BLUE = [255,0,0]
img1 = cv2.imread('treka.jpg')
replicate = cv2.copyMakeBorder(img1,20,2,20,20,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_CONSTANT,value=BLUE)
cv2.imshow('replicate',replicate)
cv2.imshow('reflect',reflect)
cv2.imshow('reflect101',reflect101)
cv2.imshow('wrap',wrap)
cv2.imshow('constant',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()
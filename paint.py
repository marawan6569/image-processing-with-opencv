import cv2
import numpy as np 
def noThing():
	pass
drawing = False
ix,iy = -1,-1
img = np.zeros((530,1366,3),np.uint8)
img[:] = 255
cv2.namedWindow('image')

cv2.createTrackbar('prushSize','image',5,100,noThing)
cv2.createTrackbar('R','image',0,255,noThing)
cv2.createTrackbar('G','image',0,255,noThing)
cv2.createTrackbar('B','image',0,255,noThing)
cv2.createTrackbar('clear','image',0,1,noThing)

def draw_circle(event,x,y,flags,param):
	global ix,iy,drawing,mode
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.circle(img,(x,y),s,(b,g,r),-1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.circle(img,(x,y),5,(b,g,r),-1)

cv2.setMouseCallback('image',draw_circle)
while(1):
	global s,r,g,b,c
	s = cv2.getTrackbarPos('prushSize','image')
	r = cv2.getTrackbarPos('R','image')
	g = cv2.getTrackbarPos('G','image')
	b = cv2.getTrackbarPos('B','image')
	c = cv2.getTrackbarPos('clear','image')
	cv2.imshow('image',img)
	if c == 1:
		img[:] = 255

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
	

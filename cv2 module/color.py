import cv2
import numpy as np

def no(x):
	pass

img=np.zeros((700,1500,3),np.uint8)
cv2.namedWindow('color')

cv2.createTrackbar('R','color',0,255,no)
cv2.createTrackbar('G','color',0,255,no)
cv2.createTrackbar('B','color',0,255,no)

#switch='0=off \n 1=on'

#cv2.createTrackbar(switch,'color',0,1,no)

while True:
	cv2.imshow('color',img)
	if cv2.waitKey(1)==13:
		break

	r = cv2.getTrackbarPos('R','color')
	g = cv2.getTrackbarPos('G','color')
	b = cv2.getTrackbarPos('B','color')
	#s = cv2.getTrackbarPos(switch,'color')

	img[:]=[b,g,r]
	#if s==0:
	#	img[:] = 0
	#else:
	#	img[:] = [b,g,r]

cv2.destroyAllWindows()
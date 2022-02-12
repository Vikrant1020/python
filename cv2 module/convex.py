import cv2
import numpy as np

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
	ret, fram=cam.read()
	cv2.imshow('live', fram)

	met, thre = cv2.threshold(fram,70,255,cv2.THRESH_BINARY)
	_,contours,_ = cv2.findContours(thre.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

	hull = [cv2.convexhull(c) for c in contours]

	final=cv2.drawContours(hand,hull,-1,(255,0,0))
	cv2.imshow('final', final)
	cv2.imshow('threshold',thre)
	if cv2.waitKey(1)==13:
		break

cam.release()
cv2.destroyAllWindows()
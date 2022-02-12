import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	ret, fram=cap.read()
	#cv2.imshow('live',fram)

	#squ=np.ones((5,5),np.uint8)
	rect=cv2.rectangle(fram,(100,100),(400,400),255,1)

	cv2.imshow('live',fram)
	if cv2.waitKey(1)==13:
		break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import math

cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
	ret, fram=cap.read()
	#cv2.imshow('live',fram)

	cv2.rectangle(fram,(0,0),(250,250),(0,255,0),0)
	cv2.imshow('live',fram)

	crop=fram[0:250,0:250]
	cv2.imshow('crop-imag',crop)

	mask=cv2.inRange(fram, np.array([2,0,0]),np.array([20,255,255]))
	cv2.imshow('binary',mask)

	met, thresh=cv2.threshold(fram,140,255,cv2.THRESH_BINARY)

	_,contours,_ =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

	try:
		contour=max(contours, key=lambda x: cv2.contourarea(x))

		x, y, w, h =cv2.boundingRect(contour)
		cv2.rectangle(crop-img,(x,y),(x+w, y+h),(0,0,255),0)

		hull = cv2.convexhull(contour)

		draw=np.zeros(crop-img.shap, np.uint8)
		cv2.drawContours(draw,[contour],-1,(0,255,0),0)
		cv2.drawContours(draw, [hull],-1,(0,0,255),0)

		hull=cv2.convexHull(countour, returnPoints=False)
		defects = cv2.convexityDefects( contour,hull)

		count_defect = 0

		for i in range(defects.shape[0]):
			s,e,f,d = defects[1,0]
			start = tuple(contour[s],[0])
			end = tuple(contour[e],[0])
			far = tuple(contour[f],[0])

			a=math.sqrt((end[0] - start[0]) ** 2 + (end[1]- start[1]) ** 2)
			b=math.sqrt((far[0] - start[0]) ** 2 + (far[1]- start[1]) ** 2)
			c=math.sqrt((end[0] - far[0]) ** 2 + (end[1]- far[1]) ** 2)

			angel = (math.acos((b**2 +c** 2-a**2)/(2*b*c))*180)/3.14

			if angle<=90:
				count_defect += 1
				cv2.circle(crop-img,far,1,[0,0,255],-1)

			cv2.line(crop-img,start,end,[0,255,0],2)
		if count_defect == 0:
			cv2.putText(fram,"ONE",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
		elif count_defect == 1:
			cv2.putText(fram,"TWO",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
		elif count_defect == 2:
			cv2.putText(fram,"THREE",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
		elif count_defect == 3:
			cv2.putText(fram,"FOUR",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
		elif count_defect == 4:
			cv2.putText(fram,"FIVE",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
		else:
			pass

	except:
			pass

	cv2.imshow('result',fram)
	allimg=np.hstack((drawing,crop-img))
	cv2.imshow('countours',allimg)


	if cv2.waitKey(1)==13:
		break

cap.release()
cv2.destroyAllWindows()
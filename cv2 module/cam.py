import cv2

cap=cv2.VideoCapture(0)

while True:
	ret, fram=cap.read()
	# thresh hold paramiters	(img name, lower value, upper value,type of thresh hold)
	met, img=cv2.threshold(fram,140,255,cv2.THRESH_BINARY)

	# blur parimeter	(img name, (a metrix ),range)
	img_gaussian= cv2.GaussianBlur(fram,(7,7),0)

	# canny parimeters	 (img name, lower, upper)
	# used for edge finding.
	img_canny=cv2.Canny(fram,140,255)

	# for laplacian image 	(img nmae, conversion type)
	img_lap=cv2.Laplacian(fram, cv2.CV_64F)

	cv2.imshow('lap',img_lap)
	cv2.imshow('gausion',img_gaussian)
	cv2.imshow('canny',img_canny)
	cv2.imshow('live',fram)
	cv2.imshow('binary',img)
	#print(ret)
	#print(fram)
	if cv2.waitKey(1)==13:
		break

cap.release()
cv2.destroyAllWindows()
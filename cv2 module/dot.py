import cv2
import numpy as np

name='click'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(name)

def draw(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),40,(0,255,0),-1)
	if event==cv2.EVENT_RBUTTONDBLCLK:
		cv2.circle(img,(x,y),40,(255,0,0),0)
	if event==cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img,(x,y),40,(0,0,255),0)

cv2.setMouseCallback(name,draw)

while True:
	cv2.imshow(name,img)
	if cv2.waitKey(1)==13:
		break

cv2.destroyAllWindows()
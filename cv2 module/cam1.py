import cv2
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)

if cap.isOpened():
	ret, fram=cap.read()
	cv2.imshow('live',fram)
	
else:
	ret = False

#img=cv2.cvtColor(fram,cv2.COLOR_BGR2RGB)

#cv2.imshow('live-2',img)

plt.imshow(fram)
#plt.nameWindow('pic')
plt.xticks([])
plt.yticks([])
plt.show()

#cap.release()
#cv2.destroyAllWindows()
import cv2
import numpy as np
import random 

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(300,300),(0,0,255),4)
cv2.rectangle(img,(200,200),(400,400),(0,255,0),2)
cv2.circle(img,(100,150),30,(255,255,0),5)
cv2.putText(img,"Open Cv",(150,300),fontFace = cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale  = 1,color = (255,0,0),thickness=1)
cv2.imshow("img",img)
cv2.waitKey(0)
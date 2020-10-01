import cv2 
import numpy as np
import random

img = np.zeros((512,512,3),dtype='float')

cv2.circle(img,(300,300),100,(20,0,11),0)
cv2.imshow("circle",img)
cv2.waitKey(0)
img = img*255
cv2.imwrite('img1.jpg',img)

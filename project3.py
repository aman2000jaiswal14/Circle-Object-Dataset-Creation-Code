import cv2
img = cv2.imread('img1.jpg')
cv2.imshow('img1',img)
print(img[150:250,150:250])
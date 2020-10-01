import cv2
import numpy as np

def addNoise(img,noise):
    img  +=  np.random.randint(-noise,noise,size = (512,512,3))
    return img

radius = 30
center = (100,100)
shape ='circle'
img_name = 'img1.jpg'
color = (0,255,0)
filled = True
thickness = 10
box_corner = (center[0]-radius-thickness//2,center[1]-radius-thickness//2)
box_length = 2*radius+thickness
box_width = 2*radius+thickness
id=0
colName = ['id','img_name','shape','center','radius','color','thickness','filled','box_corner','box_length','box_width']
newdata = [[id,img_name,shape,center,radius,color,thickness,filled,box_corner,box_length,box_width]]

img = np.ones((512,512,3))
img  = addNoise(img,100)
cv2.circle(img,newdata[0][3],newdata[0][4],newdata[0][5],newdata[0][6])

print((box_corner[0]+box_length,box_corner[1]+box_width))
cv2.rectangle(img,box_corner,(box_corner[0]+box_length,box_corner[1]+box_width),(0,0,0),1)
cv2.imshow('img',img)
cv2.waitKey(0)

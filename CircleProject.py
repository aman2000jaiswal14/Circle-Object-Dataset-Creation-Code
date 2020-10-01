import pandas as pd
import numpy as np
import cv2
import random
from tqdm import tqdm

save=False
show=True

img_height,img_width = 512,512

def read_file(filename):
    return pd.read_csv(filename)
    
def addData(newData):
    fileName = 'valueimg1.csv'
    old_df = read_file(fileName)
    colName = ['id','img_name','shape','center','radius','color','thickness','filled','box_corner','box_length','box_width']
    df = pd.DataFrame([newData],columns= colName)
    old_df = pd.concat([old_df,df],axis=0)
    old_df.to_csv(fileName,index=False)

def random_parameter():
    radius = random.randint(0,127)
    center1 = random.randint(radius,img_height-radius)
    center2 = random.randint(radius,img_width-radius)
    thickness = random.randint(-1,10)
    color = random.randint(0,255)/255.,random.randint(0,255)/255.,random.randint(0,255)/255.
    return [(center1,center2),radius,color,thickness]

def get_labels(params):
    center = params[0]
    radius = params[1]
    thickness = params[3]
    box_corner = (center[0]-radius-thickness//2,center[1]-radius-thickness//2)
    box_length = 2*radius + thickness
    box_width = 2*radius + thickness
    return [box_corner,box_length,box_width]


def save_image(id,params,save=True,show=False):
    img = np.ones((img_height,img_width,3))
    center,radius,color,thickness = params[0],params[1],params[2],params[3]
    cv2.circle(img,center,radius,color,thickness)
    if(show):
        cv2.imshow('img{}.jpg'.format(id),img)
        cv2.waitKey(1000)

    img = img*255.
    if(save):
        cv2.imwrite('img{}.jpg'.format(id),img)

def save_label_image(id,params,labels,save=True,show=False):
    img = np.ones((img_height,img_width,3))
    center,radius,color,thickness = params[0],params[1],params[2],params[3]
    cv2.circle(img,center,radius,color,thickness)
    box_corner,box_length,box_width = labels[0],labels[1],labels[2]
    cv2.rectangle(img,box_corner,(box_corner[0]+box_length,box_corner[1]+box_width),(0,0,0),1)
    if(show):
        cv2.imshow('label_img{}.jpg'.format(id),img)
        cv2.waitKey(1000)
    img = img*255.
    if(save):
        cv2.imwrite('label_img{}.jpg'.format(id),img)


def Create_Dataset(id):
    shape = 'circle'
    imgName = 'img{}.png'.format(id)

    parameters = random_parameter()

    filled=False
    if(parameters[-1]==-1):
        filled=True
    
    newparameters = [id,imgName,shape]
    
    for param in parameters:
        newparameters.append(param)
    
    newparameters.append(filled)
    
    labels = get_labels(parameters)

    for param in labels:
        newparameters.append(param)


    save_image(id,parameters,save=save,show=show)
    save_label_image(id,parameters,labels,save=save,show=show)
    if(save):
        addData(newparameters)
    cv2.destroyAllWindows()

def main():
    for i in tqdm(range(5)):
        Create_Dataset(i)

main()
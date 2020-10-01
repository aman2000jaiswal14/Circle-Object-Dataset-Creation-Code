import pandas as pd
data = pd.read_csv('valueimg1.csv')
radius = 20
center = (100,100)
shape ='circle'
img_name = 'img1.jpg'
color = (0,255,0)
filled = True
thickness = -1
box_corner = (radius,radius)
box_length = radius
box_width = radius
id=0
colName = ['id','img_name','shape','center','radius','color','thickness','filled','box_corner','box_length','box_width']
newdata = [[id,img_name,shape,center,radius,color,thickness,filled,box_corner,box_length,box_width]]
df = pd.DataFrame(newdata,columns= colName)
data = pd.concat([data,df],axis=0)
data.to_csv('valueimg1.csv',index=False)
print(df)
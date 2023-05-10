#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#import cv2
import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#import webbrowser

def color_assigning(sensor_data,axis):
    #input_img = "image_processing.jpg"
    i1_img = cv.imread('image_processing.jpg')
    if sensor_data<15:
       i1_img= cv.circle(i1_img,(axis[0],axis[1]),100,(0,0,150),-1)
    elif sensor_data>15 and sensor_data<40:
       i1_img = cv.circle(i1_img,(axis[0],axis[1]),100,(0,20,180),-1)
    else:
       i1_img = cv.circle(i1_img,(axis[0],axis[1]),100,(1,100,255),-1)
   # cv2.imshow("Drawing Shapes", i1_img)
    #cv2.waitKey(0)
    #var1 = Image.open("image_processing.jpg")
    cv.imwrite('image_processing.jpg', i1_img)
    #st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide")   
    #cv.imwrite('image_processing.jpg', i1_img)
    #st.image(i1_img)

#st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide") 
cred = credentials.Certificate('firebase-sdk.json')
if not firebase_admin._apps:   
    firebase_admin.initialize_app(cred)
#firebase_admin.initialize_app(cred)
ref = db.reference('/')
ref.set(
  {
    'sensorNo' :[2,3,1] , 'sensorData':[10 ,200,35]
}
)

ref = db.reference('sensorNo')   
i1 = ref.get() 
ref = db.reference('sensorData')
i2 = ref.get()
for i in range(0,len(i1)):
    input1 = i1[i]
    sensor_data = i2[i]
    d1 = {1:[237,170],2:[572,170],3:[960,170]}
    color_assigning(sensor_data,d1.get(input1,-1))
st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide")  
var1 = Image.open("image_processing.jpg") 
st.image(var1)


#var1 = Image.open("image_processing.jpg")
#st.image(var1)

#input_img = "image_processing.jpg"
#i1_img = cv2.imread(input_img)

#plt.imshow(cv2.cvtColor(i1_img,cv2.COLOR_BGR2RGB))
#plt.show()

#if input1 == 1:
 #   if sensor_data<15:
  #      cv2.circle(i1_img,(237,170),100,(0,255,0),-1)
   # elif sensor_data>15 and sensor_data<40:
    #    cv2.circle(i1_img,(572,170),100,(255,0,0),-1)
    #else:
     #   cv2.circle(i1_img,(960,170),100,(0,0,255),-1)


#cv2.imshow("Drawing Shapes", i1_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#import cv2
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
#import webbrowser

def color_assigning(sensor_data,axis):
    input_img = "image_processing.jpg"
    i1_img = cv.imread(input_img)
    if sensor_data<15:
        cv.circle(i1_img,(axis[0],axis[1]),100,(0,0,150),-1)
    elif sensor_data>15 and sensor_data<40:
        cv.circle(i1_img,(axis[0],axis[1]),100,(0,20,180),-1)
    else:
        cv.circle(i1_img,(axis[0],axis[1]),100,(1,100,255),-1)
   # cv2.imshow("Drawing Shapes", i1_img)
    #cv2.waitKey(0)
    #var1 = Image.open("image_processing.jpg")
    st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide")   
    st.image(i1_img)

#st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide") 
    
input1 = 2 # int(input("Enter the sensor no: "))
sensor_data = 10 #int (input("Enter the sensor data: "))
d1 = {1:[237,170],2:[572,170],3:[960,170]}
color_assigning(sensor_data,d1.get(input1,-1))


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

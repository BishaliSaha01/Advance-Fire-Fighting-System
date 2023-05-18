#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime #time
from twilio.rest import Client #date
import time

SID = 'AC57837e1f65a82cdf45cb90736e1a7ce4'
AUTH_TOKEN = '3117d74a9a3d534c485f474a5062f54d'
address_list = ["1A, Cathedral Road, Kolkata-700071"] 
location_list = ["https://goo.gl/maps/1R5ZQjyYZhB9XZY19"] 
b_link = "https://shorturl.at/sRY58"
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time1 = now.strftime("%H:%M")



        
def color_assigning(sensor_data,axis):
    #input_img = "image_processing.jpg"
    i1_img = cv.imread('image_processing.jpg')
    if sensor_data<15:
       i1_img= cv.circle(i1_img,(axis[0],axis[1]),90,(0,0,150),-1)
    elif sensor_data>15 and sensor_data<40:
       i1_img = cv.circle(i1_img,(axis[0],axis[1]),90,(0,20,180),-1)
    else:
       i1_img = cv.circle(i1_img,(axis[0],axis[1]),90,(1,100,255),-1)
   # cv2.imshow("Drawing Shapes", i1_img)
    #cv2.waitKey(0)
    #var1 = Image.open("image_processing.jpg")
    cv.imwrite('image_processing.jpg', i1_img)
    #st.image(i1_img)
    
    
def fire_call(sensor_data):
    if sensor_data>=300 :
        ss = "HIGH"
        ent_sms(ss)
    elif sensor_data>=100 and sensor_data<300: 
        ss = "MEDIUM"
        sent_sms(ss)
    else:                          
        ss = "LOW"
        
def sent_sms(ss):
    cl = Client(SID, AUTH_TOKEN)
    address = address_list[0]
    location = location_list[0]
   #cl.messages.create(body='\nURGENT !!! \nFIRE EMERGENCY AT \nAddress: '+address+'\nLocation: '+location+'\nTime: '+ time1+'\nDate: '+date+'\nEvent: Fire Detected'+'\nUrgency: '+ss+'\nBluePrint: '+b_link+'\n*Requesting immediate help from the nearest firefighters and rescue teams. Please respond as soon as possible to help contain the fire*', from_='+12706122154', to='+916290499469')

def main():
    dbURL = 'https://advance-fire-fighting-system-default-rtdb.asia-southeast1.firebasedatabase.app'
    cred = credentials.Certificate('firebase-sdk.json')
    if not firebase_admin._apps:   
        firebase_admin.initialize_app(cred)
    ref = db.reference('/', url= dbURL)    
    ss = ""
    ref1= db.reference('sensorNo', url = dbURL)   
    i1 = ref1.get() 
    ref2 = db.reference('sensorData', url = dbURL)
    i2 = ref2.get()
    for i in range(0,len(i1)):
        input1 = i1[i]
        sensor_data = i2[i]
        d1 = {1:[237,170],2:[572,170],3:[960,170]}
        color_assigning(sensor_data,d1.get(input1,-1))
        fire_call(sensor_data)
    var1 = Image.open("image_processing.jpg") 
    st.image(var1)
        
if __name__ == '__main__':
        
    st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide") 
    #main()
    while True:
        # Clear the Streamlit cache
        #st.experimental_rerun()
        # Run the app
        main()
        #st.balloons()
        # Wait for the refresh interval 
        time.sleep(200)
        st.experimental_rerun()
        
        
#st.set_page_config(page_title="Building's website", page_icon=":tada:", layout="wide", reload=True)  
#var1 = Image.open("image_processing.jpg") 
#st.image(var1)


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

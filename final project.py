import cv2
import math
import numpy as np


def getcontours(vdo,th1):
    contours, hierarchy= cv2.findContours(vdo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    

    

    for contour in contours:
         area= cv2.contourArea(contour)

         if area>1000:
             cv2.drawContours(th1, contours, -1, (0,255,0), 3)

             

             peri=cv2.arcLength(contour, True)

             
            

             approx=cv2.approxPolyDP(contour, 0.02*peri, True)
            
             objcor=len(approx)
             x, y, w, h = cv2.boundingRect(approx)

             if objcor ==7:

                 
                 
                 cv2.rectangle(th1,(x,y),(x+w,y+h), (255,0,0),2)
                 #print(approx[0][0][0])
                 
                 #print(approx)
                 #print(len(approx))
                 
                 startpoint= (approx[0][0][0],approx[0][0][1])
                 
                 

                 endpoint=(int((approx[3][0][0]+approx[4][0][0])/2),int((approx[3][0][1]+approx[4][0][1])/2))

                 
                 #th1 = cv2.arrowedLine(th1, endpoint, startpoint, (255,0,0),3)  

                 slope=(startpoint[0]-endpoint[0])/(startpoint[1]-endpoint[1])
                 angle= math.degrees(math.atan(slope))
                 print(angle)
                 font= cv2.FONT_HERSHEY_SIMPLEX
                 cv2.putText(th1, 'angle= '+str(angle), (50,50), font, 1, (224,0,0), 2)
             else:
                 pass
             
            

             #print(area)
             #print(contour)
    
cap=cv2.VideoCapture(0)



while True:
    _, frame= cap.read()
    blur=cv2.GaussianBlur(frame, (5,5), 0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)


    lower_red=np.array([0,100,100])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_red, upper_red)

    

    result= cv2.bitwise_and(frame, frame, mask=mask)

    ab,th1=cv2.threshold(result, 130,255, cv2.THRESH_BINARY)
    th1=cv2.erode(th1,None, iterations=2)
    th1=cv2.dilate(th1, None, iterations=2)

    getcontours(mask,th1)
    
        

    
    
    
    cv2.imshow('th1', th1)
    cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result", result)
  
    key= cv2.waitKey(500)
    
    if key== 27:
        break

cap.release()
cv2.destroyAllWindows()

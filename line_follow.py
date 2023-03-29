from GUI import GUI
from HAL import HAL
import numpy as np
import cv2

prev_error =0
acc_error=0
# Enter sequential code!

while True:
    img=HAL.getImage()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_thresh = np.array([0,0,0])
    u_thresh = np.array([1,1,360])
    
    mask=cv2.inRange(hsv,l_thresh,u_thresh)
    mask=cv2.bitwise_not(mask)
    h,w,d = img.shape
    top=3*h/4
    bot=top*20
    M=cv2.moments(mask)
    if M["m00"] !=0 :
        x= int(M["m10"]/M["m00"])
        y= int(M["m01"]/M["m00"])
        cv2.circle(img,(x,y),20,(0,0,255),-1)
        err=x-w/2
        print(err)
        p=float(err)
        d=(float(err)-float(prev_error))*0.8
        GUI.showImage(img)
        HAL.setV(4)
        HAL.setW(-p/50 - d/70)
        prev_error = float(err)
    # Enter iterative code!
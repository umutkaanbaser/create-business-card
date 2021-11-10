import cv2
import numpy as np
from kartvizit import * #kartvizit_olustur | create_business_card


print(help(kartvizit_olustur))


def yuz_bul(frame):
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = cascade.detectMultiScale(gri,minNeighbors=7)
    return yuzler

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")

w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourc = cv2.VideoWriter_fourcc(*"DIVX")
writer = cv2.VideoWriter("kamera.mp4",fourc,20,(w,h))


while True:
    ret,frame=cap.read()
    if(ret):
        yuzler = yuz_bul(frame)
        if(len(yuzler)>0):
            yuz= yuzler[0]
            x,y,w,h=yuz
            kisi_foto = cv2.imread("kullanici.jpg") #frame[y:y+h,x:x+w]
            bilgiler = ["Bilgi - 1","Bilgi - 2","Bilgi - 3","Bilgi - 4","Bilgi - 5"]
            frame = kartvizit_olustur(frame,
                                      kisi_foto,
                                      bilgiler,
                                      oran=.7,
                                      arkaplan=[15,45,2220],
                                      seffaf=0.3,
                                      yazi_rengi=(1,1,1))
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        writer.write(frame)
        cv2.imshow("kamera",frame)
        key = cv2.waitKey(1)
        if(key==ord("q")):
            break
    else:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
  

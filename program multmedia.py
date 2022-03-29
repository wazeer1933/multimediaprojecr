import cv2
from tkinter import *
prog=Tk()

prog.title("وسائط متعددة")
prog.geometry('350x450+400+100')
title=Label(prog,text='Project MultiMedia',fg='white',bg='green')

title.pack()
#-----------------------التقاط صورة-----------------------------
def cam():
    cam=cv2.VideoCapture(0)
    ret,image=cam.read()
    cv2.imwrite("image.jpg", image)
    del(cam)
    
    #--------------------تسجيل فيديو----------------------------
def createvideo():
    cap = cv2.VideoCapture(0)
    i = 0
    while( i < 18):
        i = i+1
        print(cap.get(i))
     
    ret = cap.set(3,320)
    ret = cap.set(4,240)
     
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video_creating.avi', fourcc, 20.0, (320,240))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            out.write(frame)
     
            cv2.imshow('image', gray)
            k = cv2.waitKey(1)
            if (k & 0xff == ord('q')):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
#/////////////////////////////////ظغط الصوره ////////////////////////////////////////////////
def imagecomperss():
    from PIL import Image
    import numpy
    im=Image.open('image.jpg')
    new_image=im.resize((1024,800),Image.ANTIALIAS)
    new_image.save(('image_compers.jpg'),optimize=True,quality=95)
 #//////////////////////////////////////////////////////////////////////////////////////////////////
def video_compress():
    import cv2 as cv
    import numpy as np
    cap=cv.VideoCapture('video_creating.avi')
    fourcc=cv.VideoWriter_fourcc(*'XVID')
    out=cv.VideoWriter('video_creating is comperss.avi.mp4',fourcc,5,(1260,720))
    while True:
        ret,frame=cap.read()
        if ret==True:
            b=cv.resize(frame,(1200,620),fx=0,fy=0,interpolation=cv.INTER_CUBIC)
            out.write(b)
        else:
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()    
    


#///////////////////////////////////////////////////////////////////////////////    
btn1=Button(prog,text=' التقاط صورة',bg='blue',fg='white',width=20,height=2,command=cam)
btn3=Button(prog,text=' تسجيل فيديو',bg='blue',fg='white',width=20,height=2,command=createvideo)
btn2=Button(prog,text='Close Program',bg='blue',fg='white',width=20,height=2,command=prog.quit)
btn4=Button(prog,text='ظغط الصوره الملتقطه',bg='blue',fg='white',width=20,height=2,command=imagecomperss)
btn5=Button(prog,text='ظغط الفيديو ',bg='blue',fg='white',width=20,height=2,command=video_compress)

btn1.place(x=100,y=340)
btn2.place(x=100,y=390)
btn3.place(x=100,y=280)
btn4.place(x=100,y=220)
btn5.place(x=100,y=150)


#--------------------------------------------------------------


prog.mainloop()

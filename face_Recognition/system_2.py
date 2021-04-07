import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font



'''window = tk.TK()
window.title("face system")'''

import tkinter

#------------------------------------frame-------------
window = tkinter.Tk()
window.title("Face Recogniser")
window.geometry('1200x700')
dialog_title = 'QUIT' 
dialog_text= "Are you sure?"
window.configure(background="#900C3F")
window.grid_rowconfigure(0,weight =1)
window.grid_columnconfigure(0,weight=20)


#---------------------------------Front Label---------------------------------------------

banner= tk.Label(window, 
    text = "Attendance System",
    bg="#807A80",
    fg="#ffeab0",
    width =30,
    height =1,
    font=("Helvetica",30,"bold"))                                   #200 200 #text filed 550 210
    
banner.place(x=100,y=20)



#--------------------------profile Label------------------------------------
lbl = tk.Label(window, text="Enter ID",width=20  ,height=1  ,fg="#F6ECF6"  ,bg="#900C3F" ,font=('Helvetica', 15, ' bold ') ) 
lbl.place(x=1, y=150)

txt = tk.Entry(window,width=30 ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=200, y=150)

#---------------2
lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="#F6ECF6"  ,bg="#900C3F" ,height=1 ,font=('Helvetica', 15, ' bold ')) 
lbl2.place(x=1, y=200)

txt2 = tk.Entry(window,width=30,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=200, y=200)


#-----------------3
"""notification"""
lbl3 = tk.Label(window, text="Notification : ",width=20  , fg="#F6ECF6"  ,bg="#900C3F" ,height=2 ,font=('Helvetica', 15, ' bold ')) 
lbl3.place(x=1, y=250)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=30  ,height=6, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=200, y=250)

#-------------------------------
lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="#F6ECF6"  ,bg="#900C3F"  ,height=2 ,font=('Helvetica', 15, ' bold')) 
lbl3.place(x=50, y=500)


message2 = tk.Label(window, text="" ,fg="red"   ,bg="white",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=250, y=500)

#--------------------functionality------------------
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    
    if(is_number(Id) and name.isalpha()):
        #folder_name = Id+" "+name
        #os.mkdir(folder_name)
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                
                cv2.imwrite("ColoerImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", img[y:y+h,x:x+w])
                
                #cv2.imwrite("ColoerImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", img[y:y+h,x:x+w])
                
                #cv2.imwrite("ColoerImage\ ",name,".",Id,','+str(sampleNum)+".jpe",img[y:y+h,x:x+w])
                #print(name)
                #print(Id)
                #cv2.imwrite()
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('StudentDetails\studentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
            
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    #recognizer = cv2.face.LBPHFaceRecognizer_create()
    #$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids


def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #cv2.createLBPHFaceRecognizer() 
    #cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    message2.configure(text= res)








#----------------only--button------------------------   
"""For reset Name"""
clearnButton = tk.Button(window, text = "Resat",command=clear,fg = "green",bg = "yellow",width =15,height=1, activebackground ="Red",font = ("times",10,'bold') )
clearnButton.place(x=550, y=150)

"""For reset ID"""
clearnButton2 = tk.Button(window, text = "Resat",command=clear2,fg = "green",bg = "yellow",width =15,height=1, activebackground ="Red",font = ("times",10,'bold') )
clearnButton2.place(x=550, y=200)





"""CAPTURE image button"""
takeImage = tk.Button(window, text = "Take Image",command=TakeImages,fg = "red",bg = "yellow",width =20,height=3, activebackground ="Red",font = ("times",15,'bold') )
takeImage.place(x=900, y=300)


trainImage = tk.Button(window, text = "Train Image",command=TrainImages,fg = "red",bg = "yellow",width =20,height=3, activebackground ="Red",font = ("times",15,'bold') )
trainImage.place(x=900, y=400)

trackImage = tk.Button(window, text = "Track Image",command=TrackImages,fg = "red",bg = "yellow",width =20,height=2, activebackground ="Red",font = ("times",15,'bold') )
trackImage.place(x=900, y=500)

quiteWindow = tk.Button(window, text = "Quite",command=window.destroy,fg = "yellow",bg = "red",width =10,height=2, activebackground ="Red",font = ("times",15,'bold') )
quiteWindow.place(x=400, y=600)




window.mainloop()



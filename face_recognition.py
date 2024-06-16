from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)
        
        #1st img
        img_top = Image.open(r"Images\Face.png")
        img_top = img_top.resize((650,screen_height), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=screen_height)
        
        #2nd image
        img_bottom = Image.open(r"Images\real_black.png")
        img_bottom = img_bottom.resize((950,screen_height), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=45, width=950, height=screen_height)
        
        #button
        b1 = Button(f_lbl, text = "FACE RECOGNITION", cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        b1.place(x = 350, y = 250, width =200, height = 40)
        
    #face recognition
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h), (0,255,0), 3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                
                if confidence > 77:
                    
                
        
        
        



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
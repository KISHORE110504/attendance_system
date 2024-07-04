from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x200")
        self.root.title("Face Recognition System")
        self.root.configure(bg = "black")
        
        # Main window title
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.pack(side=TOP, fill=X)
    
        
        # Button to open the training popup
        open_popup_btn = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        open_popup_btn.pack(pady=50)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L') #Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        
        #Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")
        pass

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

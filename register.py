from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        img = Image.open(r"Images\train_data.png")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)
        
        #main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=100, width=700, height=550)
        
        title = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)
        
        #first name label
        f_name = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        f_name.place(x=50, y=100)
        
        self.txt_fname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)
        
        #last name label
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")   
        l_name.place(x = 400, y = 100)
        
        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=400, y=130, width=250)
        
        #Contact number label
        contact_number = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_number.place(x=50, y=180)
        
        self.txt_fname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=210, width=250)
        
        #email label
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")   
        email_lbl.place(x = 400, y = 180)
        
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=400, y=210, width=250)
        
        #security questionlabel
        security_qus = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_qus.place(x=50, y=260)
        
        
        
        


if __name__ == "__main__":
    root=Tk()
    app= Register(root)
    root.mainloop()        
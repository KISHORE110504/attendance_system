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
        
        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        
        #main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=100, width=700, height=550)
        
        title = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)
        
        #first name label
        f_name = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        f_name.place(x=50, y=100)
        
        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)
        
        #last name label
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")   
        l_name.place(x = 400, y = 100)
        
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=400, y=130, width=250)
        
        #Contact number label
        contact_number = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_number.place(x=50, y=180)
        
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=210, width=250)
        
        #email label
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")   
        email_lbl.place(x = 400, y = 180)
        
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=400, y=210, width=250)
        
        #security questionlabel
        security_qus = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_qus.place(x=50, y=260)
        
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_security, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security["values"] = ("Select", "Your Birth Place", "Your Birth Date", "Your Pet Name")
        self.combo_security.current(0)
        self.combo_security.place(x=50, y=290, width=250)
        
        #answer label
        answer = Label(frame, text="Answer", font=("times new roman", 15, "bold"), bg="white")
        answer.place(x=400, y=260)
        
        self.txt_answer = ttk.Entry(frame,textvariable=self.var_answer, font=("times new roman", 15, "bold"))
        self.txt_answer.place(x=400, y=290, width=250)
        
        #password label
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=340)
        
        self.txt_password = ttk.Entry(frame,textvariable=self.var_password, font=("times new roman", 15, "bold"))
        self.txt_password.place(x=50, y=370, width=250)
        
        #confirm password label
        c_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        c_password.place(x=400, y=340)
        
        self.txt_cpassword = ttk.Entry(frame,textvariable=self.var_cpassword, font=("times new roman", 15, "bold"))
        self.txt_cpassword.place(x=400, y=370, width=250)
        
        #register button
        registerbtn = Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bg="green", fg="white")
        registerbtn.place(x=50, y=420, width=250)
        
        #login button
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="green", fg="white")
        loginbtn.place(x=400, y=420, width=250)
        
        #function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security.get() == "Select" or self.var_password.get() == "" or self.var_cpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror("Error", "Password and confirm password should be same", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="YOUR_PASSWORD", database="YOUR_DATABASE", auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists", parent=self.root)
            else: 
                my_cursor.execute("INSERT INTO register (firstname, lastname, contact, email, question, answer, password) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security.get(),
                    self.var_answer.get(),
                    self.var_password.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                
        


if __name__ == "__main__":
    root=Tk()
    app= Register(root)
    root.mainloop()        

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        img = Image.open(r"Images\real_black.png")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)
        
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=170, width=340, height=450)
        
        img1= Image.open(r"Images\login.jpg")
        img1=img1.resize((100, 100), Image. LANCZOS)
        self.photoimage1=ImageTk. PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=620,y=175, width=100, height=100)
        
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="white", fg="black")
        get_str.place(x=95, y=120)
        
        #style
        style = ttk.Style()
        style.configure("Gray.TEntry", fieldbackground="lightgray", font=("times new roman", 15, "bold"))
        
        #label
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username.place(x= 40, y=180)
        
        self.txtuser = ttk.Entry(frame, text="Username", font=("times new roman", 15, "bold"), style="Gray.TEntry")
        self.txtuser.place(x=40,y=210, width=270)
        
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x= 40, y=250)
        
        self.txtpass = ttk.Entry(frame, text="Password", font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40,y=280, width=270)
        
        #login button
        loginbtn = Button(frame, command=self.login, text= "Login", font=("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg= "black", bg = "darkgreen", activeforeground="white", activebackground="darkgreen")
        loginbtn.place(x=80, y=330, width=180, height= 35)
        
        #register button
        registerbtn = Button(frame, text= "New User? Register", font=("times new roman", 9, "bold"),borderwidth=0, fg= "black", bg = "white", activeforeground="darkgreen", activebackground="white")
        registerbtn.place(x=-5, y=385, width=180, height= 25)
        
        #forget password button
        forgetbtn = Button(frame, text= "Forget Password", font=("times new roman", 9, "bold"), borderwidth=0, fg= "black", bg = "white", activeforeground="darkgreen", activebackground="white")
        forgetbtn.place(x=-13, y=405, width=180, height= 25)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success", "Welcome", parent=self.root)
        else:
            messagebox.showerror("Invalid", "Invalid username and password", parent=self.root)
            
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()

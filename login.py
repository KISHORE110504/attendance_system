from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random
import time
import datetime

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

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
        registerbtn = Button(frame, text= "New User? Register", command=self.register_window, font=("times new roman", 9, "bold"),borderwidth=0, fg= "black", bg = "white", activeforeground="darkgreen", activebackground="white")
        registerbtn.place(x=-5, y=385, width=180, height= 25)
        
        #forget password button
        forgetbtn = Button(frame, text= "Forget Password", command = self.forgot_password_window, font=("times new roman", 9, "bold"), borderwidth=0, fg= "black", bg = "white", activeforeground="darkgreen", activebackground="white")
        forgetbtn.place(x=-13, y=405, width=180, height= 25)
    
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success", "Welcome", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Kishore@1105", database="face_recognizer", auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Invalid username and password", parent=self.root)
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root) 
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return 
            conn.commit()
            conn.close()
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error, please enter email id", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Kishore@1105", database="face_recognizer", auth_plugin='mysql_native_password')
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error, please enter valid username", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x400+500+200")
                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=0, relwidth=1)
            
        
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
            conn = mysql.connector.connect(host="localhost", user="root", password="Kishore@1105", database="face_recognizer", auth_plugin='mysql_native_password')
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

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        
        #bg image
        img = Image.open(r"Images\real_black.png")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)
        
        #student button
        img1 = Image.open(r"Images\students.webp")
        img1 = img1.resize((220,220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        b1 = Button(bg_img, image=self.photoimg1, command = self.student_details, cursor="hand2")
        b1.place(x = 100, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Student Details", command = self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 100, y = 300, width = 220, height = 40)
        
        #Detect Face button
        img2 = Image.open(r"Images\face_detection.jpg")
        img2 = img2.resize((220,220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        b1 = Button(bg_img, image=self.photoimg2, cursor="hand2",command=self.face_data )
        b1.place(x = 400, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 400, y = 300, width = 220, height = 40)
        
        #Attendance button
        img3 = Image.open(r"Images\attendance.jpg")
        img3 = img3.resize((220,220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        b1 = Button(bg_img, image=self.photoimg3, cursor="hand2", command= self.attendance_data)
        b1.place(x = 700, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Attendance", cursor="hand2", command= self.attendance_data, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 700, y = 300, width = 220, height = 40)
        
        #Help desk button
        img4 = Image.open(r"Images\help_desk.webp")
        img4 = img4.resize((220,220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.show_help_popup)
        b1.place(x = 1000, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Help desk", cursor="hand2", command=self.show_help_popup, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 1000, y = 300, width = 220, height = 40)
        
        #Train button
        img5 = Image.open(r"Images\train_data.png")
        img5 = img5.resize((220,220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command = self.train_data)
        b1.place(x = 100, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Train Data", cursor="hand2", command = self.train_data, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 100, y = 600, width = 220, height = 40)
        
        #Photos button
        img6 = Image.open(r"Images\photos.png")
        img6 = img6.resize((220,220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.open_img)
        b1.place(x = 400, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 400, y = 600, width = 220, height = 40)
        
        #Developer button
        img7 = Image.open(r"Images\developer.png")
        img7 = img7.resize((220,220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.open_developer_website)
        b1.place(x = 700, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Developer", cursor="hand2", command=self.open_developer_website, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 700, y = 600, width = 220, height = 40)
        
        #Exit button
        img8 = Image.open(r"Images\exit.png")
        img8 = img8.resize((220,220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.exit)
        b1.place(x = 1000, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 1000, y = 600, width = 220, height = 40)
    
    def open_img(self):
        os.startfile("data")
        
    #functions buttons
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def open_developer_website(self):
        webbrowser.open("https://github.com/KISHORE110504")
        
    def show_help_popup(self):
        def open_link(url):
            webbrowser.open_new(url)
        
        popup = Toplevel(self.root)
        popup.title("Help Desk")
        popup.geometry("300x250")
        
        Label(popup, text="Contact Us", font=("times new roman", 20, "bold")).pack(pady=10)
        
        email_label = Label(popup, text="Email: kishore110504@gmail.com", font=("times new roman", 15), fg="blue", cursor="hand2")
        email_label.pack(pady=5)
        email_label.bind("<Button-1>", lambda e: open_link("mailto:kishore110504@gmail.com"))

        instagram_label = Label(popup, text="Instagram: _kish.xx_", font=("times new roman", 15), fg="blue", cursor="hand2")
        instagram_label.pack(pady=5)
        instagram_label.bind("<Button-1>", lambda e: open_link("https://www.instagram.com/_kish.xx_/"))

        linkedin_label = Label(popup, text="LinkedIn: kishoreanbu", font=("times new roman", 15), fg="blue", cursor="hand2")
        linkedin_label.pack(pady=5)
        linkedin_label.bind("<Button-1>", lambda e: open_link("www.linkedin.com/in/kishoreanbu"))
        
        Button(popup, text="Close", command=popup.destroy, font=("times new roman", 12)).pack(pady=10)
        
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return
        
        
        
        
        
if __name__ == "__main__":
    main()
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
    
    

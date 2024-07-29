from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
import webbrowser
import tkinter

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
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    

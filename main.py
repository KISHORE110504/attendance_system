from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        
        #bg image
        img = Image.open(r"D:\Projects\Attendance_System\Images\real_black.png")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)
        
        #student button
        img1 = Image.open(r"D:\Projects\Attendance_System\Images\students.webp")
        img1 = img1.resize((220,220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        b1 = Button(bg_img, image=self.photoimg1, cursor="hand2")
        b1.place(x = 100, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 100, y = 300, width = 220, height = 40)
        
        #Detect Face button
        img2 = Image.open(r"D:\Projects\Attendance_System\Images\face_detection.jpg")
        img2 = img2.resize((220,220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        b1 = Button(bg_img, image=self.photoimg2, cursor="hand2")
        b1.place(x = 400, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 400, y = 300, width = 220, height = 40)
        
        #Attendance button
        img3 = Image.open(r"D:\Projects\Attendance_System\Images\attendance.jpg")
        img3 = img3.resize((220,220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        b1 = Button(bg_img, image=self.photoimg3, cursor="hand2")
        b1.place(x = 700, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 700, y = 300, width = 220, height = 40)
        
        #Help desk button
        img4 = Image.open(r"D:\Projects\Attendance_System\Images\help_desk.webp")
        img4 = img4.resize((220,220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x = 1000, y = 100, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Help desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 1000, y = 300, width = 220, height = 40)
        
        #Train button
        img5 = Image.open(r"D:\Projects\Attendance_System\Images\train_data.png")
        img5 = img5.resize((220,220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x = 100, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 100, y = 600, width = 220, height = 40)
        
        #Photos button
        img6 = Image.open(r"D:\Projects\Attendance_System\Images\photos.png")
        img6 = img6.resize((220,220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x = 400, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 400, y = 600, width = 220, height = 40)
        
        #Developer button
        img7 = Image.open(r"D:\Projects\Attendance_System\Images\developer.png")
        img7 = img7.resize((220,220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x = 700, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 700, y = 600, width = 220, height = 40)
        
        #Exit button
        img8 = Image.open(r"D:\Projects\Attendance_System\Images\exit.png")
        img8 = img8.resize((220,220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x = 1000, y = 400, width = 220, height = 220)
        
        b1 = Button(bg_img, text = "Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="darkgreen")
        b1.place(x = 1000, y = 600, width = 220, height = 40)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    

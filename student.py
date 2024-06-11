from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
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
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)
        
        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x = 0, y = 45, width = screen_width, height= screen_height)
        
        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=650)
        
        # Current course frame
        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief= RIDGE, text="Current course information", font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=10, y=10, width=630, height=130)
        
        #department
        dep_label = Label(Current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column= 0, padx = 10, pady = 10, sticky = W)
        
        dep_combo = ttk.Combobox(Current_course_frame, font=("times new roman", 13, "bold"), width = 17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "AIDS", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column= 1, padx = 2, pady= 10, sticky = W)
        
        #Course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column= 2, padx = 15, pady= 10, sticky = W)
        
        course_combo = ttk.Combobox(Current_course_frame, font=("times new roman",13,"bold"), state="readonly", width = 17)
        course_combo["values"] = ("Select Course", "FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx = 2, pady = 10, sticky = W)
        
        # Year
        year_label = Label(Current_course_frame, text = "Year", font=("times new roman",13,"bold"), bg="white")
        year_label.grid(row =1,column = 0, padx = 10, sticky = W)

        year_combo = ttk.Combobox(Current_course_frame, font=("times new roman",13,"bold"), state="readonly", width = 17)
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column = 1, padx = 2, pady = 10, sticky = W)

        # Semester
        semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1,column=2, padx=10, sticky=W)
        
        semester_combo = ttk.Combobox(Current_course_frame, font=("times new roman", 13, "bold"), state="readonly", width=17)
        semester_combo["values"]=("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10, sticky=W)
        
        # Class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief= RIDGE, text="Class Student information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=10, y=150, width=630, height=300)
        
        #student id
        studentID_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        studentID_label.grid(row=0,column=0, padx=10, pady= 5, sticky=W)
        
        studentID_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #student name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0,column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #class division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1,column=0, padx=10, pady=5, sticky=W)
        
        class_div_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #Roll no
        roll_no_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1,column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=660, height=650)







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    

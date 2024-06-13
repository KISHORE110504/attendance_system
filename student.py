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
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1,column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        #Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2,column=0, padx=10, pady=5, sticky=W)
        
        gender_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        #DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2,column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        #Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3,column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        #Phone no
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3,column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        #Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4,column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        #Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4,column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_Student_frame, width= 17, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        #radio butttons
        radionbtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row = 6, column = 0)
        
        radionbtn2 = ttk.Radiobutton(class_Student_frame, text="No Photo Sample", value="Yes")
        radionbtn2.grid(row = 6, column = 1)
        
        #bbuttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=4, y=205, width=615, height=70)
        
        save_btn = Button(btn_frame, text="Save", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row =0, column =0)
        
        update_btn = Button(btn_frame, text="Update", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row =0, column =1)
        
        delete_btn = Button(btn_frame, text="Delete", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row =0, column =2)
        
        reset_btn = Button(btn_frame, text="Reset", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row =0, column =3)
        
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=4, y=235, width=615, height=30)
        
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=29, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row =0, column =0)
        
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=31, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row =0, column =1)
        
        #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=660, height=650)

        #search system
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief= RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=10, y=10, width=630, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="white")
        search_label.grid(row=0,column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=17)
        search_combo["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W)
        
        search_entry = ttk.Entry(Search_frame, width= 15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn = Button(Search_frame, text="Search", width=7, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row =0, column =3, padx=4)
        
        showAll_btn = Button(Search_frame, text="Show All", width=7, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row =0, column =4, padx=4)
        
        #table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief= RIDGE)
        table_frame.place(x=10, y=90, width=630, height=300)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("roll", "name", "semester", "id", "course", "department", "year", "gender", "dob", "email", "phone", "address", "teacher", "photo","div"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("roll", text = "Roll No")
        self.student_table.heading("department", text = "Department")
        self.student_table.heading("name", text = "Name")
        self.student_table.heading("semester", text = "Semester")
        self.student_table.heading("id", text = "StudentId")
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("div", text = "Division")
        self.student_table.heading("gender", text = "Gender")
        self.student_table.heading("dob", text = "DOB")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("phone", text = "Phone")
        self.student_table.heading("address", text = "Address")
        self.student_table.heading("teacher", text = "Teacher")
        self.student_table.heading("photo", text = "PhotoSampleStatus")
        
        self.student_table["show"] = "headings"
        
        self.student_table.column("roll", width = 100)
        self.student_table.column("department", width = 100)
        self.student_table.column("name", width = 100)
        self.student_table.column("semester", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("course", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("gender", width = 100)
        self.student_table.column("dob", width = 100)
        self.student_table.column("email", width = 100)
        self.student_table.column("phone", width = 100)
        self.student_table.column("address", width = 100)
        self.student_table.column("teacher", width = 100)
        self.student_table.column("photo", width = 150)
        self.student_table.column("div", width = 100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    

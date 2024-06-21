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

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        #variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_time = StringVar()
        
        #bg image
        img = Image.open(r"D:\Projects\Attendance_System\Images\real_black.png")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=screen_width, height=screen_height)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)
        
        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x = 0, y = 45, width = screen_width, height= screen_height)
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=300)
        
        left_inside_frame = Frame(Left_frame, bd = 2, bg="white", relief= RIDGE)
        left_inside_frame.place(x = 5, y = 15, width = 645, height= 260)
        
        #labels and entry
        #attendance id
        attendanceID_label = Label(left_inside_frame, text="AttendenceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceID_label.grid(row=0,column=0, padx=10, pady= 5, sticky=W)
        
        attendanceID_entry = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #roll no
        rollLabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0,column=2, padx=10, pady= 5, sticky=W)
        
        attendance_roll = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_roll, font=("times new roman", 13, "bold"))
        attendance_roll.grid(row=0, column=3, pady=5, sticky=W)
        
        #name
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        nameLabel.grid(row=1,column=0, padx=10, pady= 5, sticky=W)
        
        attendance_name = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_name, font=("times new roman", 13, "bold"))
        attendance_name.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #department
        departmentLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        departmentLabel.grid(row=1,column=2, padx=10, pady= 5, sticky=W)
        
        attendance_dep = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_dep, font=("times new roman", 13, "bold"))
        attendance_dep.grid(row=1, column=3, pady=5, sticky=W)
        
        #time
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2,column=0, padx=10, pady= 5, sticky=W)
        
        attendance_time = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_time, font=("times new roman", 13, "bold"))
        attendance_time.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        #date
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2,column=2, padx=10, pady= 5, sticky=W)
        
        attendance_date = ttk.Entry(left_inside_frame, width= 17, textvariable=self.var_atten_date, font=("times new roman", 13, "bold"))
        attendance_date.grid(row=2, column=3, pady=5, sticky=W)
        
        #attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg="white")
        attendanceLabel.grid(row=3,column=0, padx=10, pady= 5, sticky=W)
        
        self.attendance_status = ttk.Combobox(left_inside_frame, width= 15, textvariable=self.var_atten_attendance, font=("times new roman", 13, "bold"), state="readonly")
        self.attendance_status["values"] = ("Status", "Present", "Absent")
        self.attendance_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.attendance_status.current(0)
        
        #buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=640, height=35)
        
        import_csv_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_csv_btn.grid(row =0, column =0)
        
        export_csv_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_csv_btn.grid(row =0, column =1)
        
        update_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row =0, column =2)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row =0, column =3)

        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief= RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=660, height=650)
        
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=15, width=635, height=440)
        
        #scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id","roll","name","department","time","attendance","date"), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id", text = "Attendance ID")
        self.AttendanceReportTable.heading("roll", text = "Roll")
        self.AttendanceReportTable.heading("name", text = "Name")
        self.AttendanceReportTable.heading("department", text = "Department")
        self.AttendanceReportTable.heading("time", text = "Time")
        self.AttendanceReportTable.heading("attendance", text = "Attendance")
        self.AttendanceReportTable.heading("date", text = "Date")
        
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width= 100)
        self.AttendanceReportTable.column("roll", width= 100)
        self.AttendanceReportTable.column("name", width= 100)
        self.AttendanceReportTable.column("department", width= 100)
        self.AttendanceReportTable.column("time", width= 100)
        self.AttendanceReportTable.column("attendance", width= 100)
        self.AttendanceReportTable.column("date", width= 100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        #fetch data
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")  
            for i in csvread:
                mydata.append(i)
                self.fetch_data(mydata)
    
    #export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data found to export", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Data exported to "+os.path.basename(fln)+" successfully", parent = self.root)
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)        
    
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]            
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        self.var_atten_date.set(rows[6])
    
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
            
        
if __name__ == "__main__":
    root = Tk()
    obj =Attendance(root)
    root.mainloop()

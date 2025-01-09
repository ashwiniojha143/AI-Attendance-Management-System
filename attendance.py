from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog
import win32com.client


mydata = []
def Attendance(root):
    # configure window
    root.title("Attendance marking system using multiple face recognition system")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("Desktop_Icon.ico")

    # variavle define 
    global Attendance_report_table,var_atten_attendance,var_atten_date,var_atten_time,var_atten_dep,var_atten_name,var_atten_PRN,var_atten_roll

    var_atten_PRN = StringVar()
    var_atten_roll = StringVar()
    var_atten_name = StringVar()
    var_atten_dep = StringVar()
    var_atten_time = StringVar()
    var_atten_date = StringVar()
    var_atten_attendance = StringVar()


    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Student Attendance reports & Details", font=("Helvetica", 40, "bold"), bg="white", fg='green')
    title_label.pack(pady=20)

    # Background box with rounded edges (resembling a shadow)
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Background image inside the box
    bg_image = Image.open("public/background.jpg")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()

    # main frame 
    main_frame = Frame(background_box,bd=2)
    main_frame.place(x=15,y=30,width=1470,height=600)

    # left frame 
    left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),fg="red")
    left_frame.place(x=20,y=20,width=700,height=560)




    # ========================student information frame=====================================
    student_info_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12))
    student_info_frame.place(x=0,y=25,width=695,height=200)

    # Student PRN  
    PRN_label = Label(student_info_frame,text="PRN",font=("times new roman",12),bg="white")
    PRN_label.grid(row=0,column=0,padx=10,sticky=W)

    PRN_entry = ttk.Entry(student_info_frame,textvariable=var_atten_PRN,width=20,font=("times new roman",12))
    PRN_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    # Student Name  
    Name_label = Label(student_info_frame,text="Student Name",font=("times new roman",12),bg="white")
    Name_label.grid(row=0,column=2,padx=10,sticky=W)

    Name_entry = ttk.Entry(student_info_frame,textvariable=var_atten_name,width=20,font=("times new roman",12))
    Name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    # Roll No.  
    Roll_label = Label(student_info_frame,text="Roll No.",font=("times new roman",12),bg="white")
    Roll_label.grid(row=1,column=0,padx=10,sticky=W)

    Roll_entry = ttk.Entry(student_info_frame,textvariable=var_atten_roll,width=20,font=("times new roman",12))
    Roll_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

    # Department  
    Dep_label = Label(student_info_frame,text="Department",font=("times new roman",12),bg="white")
    Dep_label.grid(row=1,column=2,padx=10,sticky=W)

    Dep_entry = ttk.Entry(student_info_frame,textvariable=var_atten_dep,width=20,font=("times new roman",12))
    Dep_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    # Time   
    Time_label = Label(student_info_frame,text="Time",font=("times new roman",12),bg="white")
    Time_label.grid(row=2,column=0,padx=10,sticky=W)

    Time_entry = ttk.Entry(student_info_frame,textvariable=var_atten_time,width=20,font=("times new roman",12))
    Time_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

    # Date  
    Date_label = Label(student_info_frame,text="Date",font=("times new roman",12),bg="white")
    Date_label.grid(row=2,column=2,padx=10,sticky=W)

    Date_entry = ttk.Entry(student_info_frame,textvariable=var_atten_date,width=20,font=("times new roman",12))
    Date_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

    # Status   
    Status_label = Label(student_info_frame,text="Attendance Status",font=("times new roman",12),bg="white")
    Status_label.grid(row=3,column=0,padx=10,sticky=W)

    Status_combo = ttk.Combobox(student_info_frame,textvariable=var_atten_attendance,font=("times new roman",12),state="readonly")
    Status_combo["values"] = ("Status","Present","Absent")
    Status_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
    Status_combo.current(0)



    # ========================Button frame information frame=====================================
    Buttons_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
    Buttons_frame.place(x=0,y=230,width=695,height=50)

    Import_button = Button(Buttons_frame,text="Import csv",command=lambda:importCsv(root),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="green",fg="white")
    Import_button.grid(row=0,column=0,padx=5,pady=7)

    Export_button = Button(Buttons_frame,text="Export csv",command=lambda:exportCsv(root),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="blue",fg="white")
    Export_button.grid(row=0,column=1,padx=5,pady=7)

    Update_button = Button(Buttons_frame,text="All Attendance",command=lambda:openCsv(root) ,width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="brown",fg="white")
    Update_button.grid(row=0,column=2,padx=5,pady=7)

    Reset_button = Button(Buttons_frame,text="Reset",command=lambda:reset_data(),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="yellow",fg="black")
    Reset_button.grid(row=0,column=3,padx=5,pady=7)

    # ========================Button frame information frame=====================================
    Image_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
    Image_frame.place(x=0,y=280,width=695,height=250)

    # Background image left box
    bg_image = Image.open("public/face_bg.jpg")
    bg_image = bg_image.resize((695, 250), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(Image_frame, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()

    # right frame 
    right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Table",font=("times new roman",15,"bold"),fg="blue")
    right_frame.place(x=740,y=20,width=700,height=560)




    # =========================Table=======================
    Attendance_report_table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Report Table",font=("times new roman",12))
    Attendance_report_table_frame.place(x=0,y=25,width=695,height=495)

    scroll_x=ttk.Scrollbar(Attendance_report_table_frame,orient=HORIZONTAL)      
    scroll_y=ttk.Scrollbar(Attendance_report_table_frame,orient=VERTICAL)  

    Attendance_report_table = ttk.Treeview(Attendance_report_table_frame,columns=("PRN","Roll","Name","Dep","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Attendance_report_table.xview)
    scroll_y.config(command=Attendance_report_table.yview)

    Attendance_report_table.heading("Dep",text="Department")
    Attendance_report_table.heading("PRN",text="PRN")
    Attendance_report_table.heading("Name",text="Name")
    Attendance_report_table.heading("Roll",text="Roll No.")
    Attendance_report_table.heading("Time",text="Time")
    Attendance_report_table.heading("Date",text="Date")
    Attendance_report_table.heading("Attendance",text="Attendance")
    Attendance_report_table["show"] = "headings"

    Attendance_report_table.column("Dep",width=100)
    Attendance_report_table.column("PRN",width=100)
    Attendance_report_table.column("Name",width=100)
    Attendance_report_table.column("Roll",width=100)
    Attendance_report_table.column("Time",width=100)
    Attendance_report_table.column("Date",width=100)
    Attendance_report_table.column("Attendance",width=100)

    Attendance_report_table.pack(fill=BOTH,expand=1)
    Attendance_report_table.bind("<ButtonRelease>",get_cursor)
   

# ============== fetch data functiona============
def fetchData(rows):
    try:
        Attendance_report_table.delete(*Attendance_report_table.get_children())
        for i in rows:
            Attendance_report_table.insert("",END,values=i)  
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.", parent=root)
    except Exception as error:
        messagebox.showerror("Error", f"Error occurred: {str(error)}", parent=root)



#import csv
def importCsv(root):
    try:
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.path.join(os.getcwd(), "attendance_report"),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=root
        )
        if not fln:
            messagebox.showerror("Error", "No file selected.", parent=root)
            return
        
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            fetchData(mydata)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.", parent=root)
    except Exception as error:
        messagebox.showerror("Error", f"Error occurred: {str(error)}", parent=root)


# export csv file 
def exportCsv(root):
    try:
        if len(mydata)<1:
            messagebox.showerror("No Data","No data found to export",parent=root)
            return False
        fln = filedialog.asksaveasfilename(
            initialdir=os.path.join(os.getcwd(), "attendance_report"),
            title = "Open CSV",
            filetypes=(("CSV File","*csv"),("All File","*.*")),
            parent = root
        )
        with open(fln,mode="w",newline="") as myfile:
            exp_write = csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to " + os.path.basename(fln)+" Successfully")
    except Exception as error:
        messagebox.showerror("Error",f"Due To:{str(error)}",parent=root)

def get_cursor(event=""):
    cursor_row = Attendance_report_table.focus()
    content = Attendance_report_table.item(cursor_row)
    row = content['values']
    if row: 
        if len(row) >= 6:
            var_atten_PRN.set(row[0])
            var_atten_roll.set(row[1])
            var_atten_name.set(row[2])
            var_atten_dep.set(row[3])
            var_atten_time.set(row[4])
            var_atten_date.set(row[5])
            var_atten_attendance.set(row[6])



# =========update attendace======= 
def openCsv(root):
    try:
        os.startfile("attendance_report")
    except Exception as error:
        messagebox.showerror("Error",f"Due To:{str(error)}",parent=root)





# ========reset data =========
def reset_data():
    var_atten_PRN.set("")
    var_atten_roll.set("")
    var_atten_name.set("")
    var_atten_dep.set("")
    var_atten_time.set("")
    var_atten_date.set("")
    var_atten_attendance.set("Status")

if __name__ == "__main__":
    root = Tk()
    Attendance(root)
    root.mainloop()

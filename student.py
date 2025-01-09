import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import mysql.connector.locales.eng.client_error
from db_connection import get_database_connection




def Student(root):
    # configure window
    root.title("Real Time Attendance Marking System")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("Desktop_Icon.ico")


    global var_dep, var_year, var_sem, var_PRN, var_name, var_div, var_roll, var_gender, var_mobile, var_radio, student_table,search_entry,search_combo


    # ==========varibales=========
    var_dep = StringVar()
    var_year = StringVar()
    var_sem = StringVar()
    var_PRN = StringVar()
    var_name = StringVar()
    var_div = StringVar()
    var_roll = StringVar()
    var_gender = StringVar()
    var_mobile = StringVar()
    var_radio = StringVar()

    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Student Informations & Details", font=("Helvetica", 40, "bold"), bg="white", fg='green')
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

    # ========================current course frame=====================================
    current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12))
    current_course_frame.place(x=0,y=15,width=695,height=120)

    # Current Department 
    dep_label = Label(current_course_frame,text="Department",font=("times new roman",12),bg="white")
    dep_label.grid(row=0,column=0,padx=10,sticky=W)

    dep_combo = ttk.Combobox(current_course_frame,textvariable=var_dep,font=("times new roman",12),state="readonly")
    dep_combo["values"] = ("Select Department","Computer","IT","ENTC","Civil,Mechnical,Chemical")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    # Final Year 
    year_label = Label(current_course_frame,text="Final Year",font=("times new roman",12),bg="white")
    year_label.grid(row=0,column=3,padx=20,sticky=W)

    year_combo = ttk.Combobox(current_course_frame,textvariable=var_year,font=("times new roman",12),state="readonly")
    year_combo["values"] = ("Select Final Year","2024","2025","2026","2027")
    year_combo.current(0)
    year_combo.grid(row=0,column=4,padx=2,pady=10,sticky=W)

    # Current Semester 
    sem_label = Label(current_course_frame,text="Current Semester",font=("times new roman",12),bg="white")
    sem_label.grid(row=1,column=0,padx=10,sticky=W)

    sem_combo = ttk.Combobox(current_course_frame,textvariable=var_sem,font=("times new roman",12),state="readonly")
    sem_combo["values"] = ("Select Semester","I","II","III","IV","V","VI","VII","VIII")
    sem_combo.current(0)
    sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


     # ========================student information frame=====================================
    student_info_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12))
    student_info_frame.place(x=0,y=150,width=695,height=200)

    # Student ID  
    PRN_label = Label(student_info_frame,text="PRN",font=("times new roman",12),bg="white")
    PRN_label.grid(row=0,column=0,padx=10,sticky=W)

    PRN_entry = ttk.Entry(student_info_frame,textvariable=var_PRN,width=20,font=("times new roman",12))
    PRN_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    # Student Name  
    Name_label = Label(student_info_frame,text="Student Name",font=("times new roman",12),bg="white")
    Name_label.grid(row=0,column=2,padx=10,sticky=W)

    Name_entry = ttk.Entry(student_info_frame,width=20,textvariable=var_name,font=("times new roman",12))
    Name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    # Roll No.  
    Roll_label = Label(student_info_frame,text="Roll No.",font=("times new roman",12),bg="white")
    Roll_label.grid(row=1,column=0,padx=10,sticky=W)

    Roll_entry = ttk.Entry(student_info_frame,width=20,textvariable=var_roll,font=("times new roman",12))
    Roll_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

    # DIVISION  
    Division_label = Label(student_info_frame,text="Division",font=("times new roman",12),bg="white")
    Division_label.grid(row=1,column=2,padx=10,sticky=W)

    Division_combo = ttk.Combobox(student_info_frame,textvariable=var_div,font=("times new roman",12),state="readonly")
    Division_combo["values"] = ("Select Division","I","II","III")
    Division_combo.current(0)
    Division_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    # Mobile  
    Mobile_label = Label(student_info_frame,text="Mobile",font=("times new roman",12),bg="white")
    Mobile_label.grid(row=2,column=0,padx=10,sticky=W)

    Mobile_entry = ttk.Entry(student_info_frame,width=20,textvariable=var_mobile,font=("times new roman",12))
    Mobile_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)


    # Gender  
    Gender_label = Label(student_info_frame,text="Gender",font=("times new roman",12),bg="white")
    Gender_label.grid(row=2,column=2,padx=10,sticky=W)
    
    Gender_combo = ttk.Combobox(student_info_frame,textvariable=var_gender,font=("times new roman",12),state="readonly")
    Gender_combo["values"] = ("Male","Female")
    Gender_combo.current(0)
    Gender_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)

 
    # ========================Button frame information frame=====================================
    Buttons_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
    Buttons_frame.place(x=0,y=360,width=695,height=50)

    save_button = Button(Buttons_frame,text="Save",command=lambda: add_data(root),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="green",fg="white")
    save_button.grid(row=0,column=0,padx=5,pady=7)

    update_button = Button(Buttons_frame,text="Update",command=lambda: update_data(root),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="blue",fg="white")
    update_button.grid(row=0,column=1,padx=5,pady=7)

    Delete_button = Button(Buttons_frame,text="Delete",command=lambda: delete_data(root),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="red",fg="white")
    Delete_button.grid(row=0,column=2,padx=5,pady=7)

    Reset_button = Button(Buttons_frame,text="Reset",command=lambda: reset_data(),width=17,cursor="hand2" ,font=("times new roman",12,"bold"),bg="yellow",fg="black")
    Reset_button.grid(row=0,column=3,padx=5,pady=7)

    
    Buttons_frame1 = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
    Buttons_frame1.place(x=0,y=425,width=695,height=105)

    # Note Label
    note_label = Label(Buttons_frame1, text="Note: Please save the user before taking  photo sample", font=("times new roman", 12, "bold"), bg="white", fg="red")
    note_label.grid(row=0, column=0, columnspan=4, pady=5)

    Add_Photo_button = Button(Buttons_frame1,text="TAKE PHOTO SAMPLE",command=lambda: generate_dataset(root),cursor="hand2",width=74,height=2,font=("times new roman",12,"bold"),bg="black",fg="white")
    Add_Photo_button.grid(row=1,column=0,padx=7,pady=5)


    # right frame 
    right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Table",font=("times new roman",15,"bold"),fg="blue")
    right_frame.place(x=740,y=20,width=700,height=560)

    # ========================Search  frame=====================================
    search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="View Student Informations & Seacrh details",font=("times new roman",12))
    search_frame.place(x=0,y=15,width=695,height=80)

    search_label = Label(search_frame,text="Search By : ",font=("times new roman",12),bg="red",fg="white")
    search_label.grid(row=0,column=0,padx=6,pady=5,sticky=W)

    search_combo = ttk.Combobox(search_frame,font=("times new roman",12),state="readonly")
    search_combo["values"] = ("PRN","Roll No.")
    search_combo.current(0)
    search_combo.grid(row=0,column=1,padx=6,pady=5,sticky=W)

    search_entry = ttk.Entry(search_frame,width=20,font=("times new roman",12))
    search_entry.grid(row=0,column=2,padx=6,pady=5,sticky=W)

    # Creating the search_button
    search_button = Button(search_frame, text="Search", cursor="hand2", width=10, font=("times new roman", 12, "bold"), bg="black", fg="white")
    search_button.grid(row=0, column=3, padx=6, pady=5, sticky=W)

    # Creating the showAll_button
    showAll_button = Button(search_frame, text="Show All", cursor="hand2", width=10, font=("times new roman", 12, "bold"), bg="black", fg="white")
    showAll_button.grid(row=0, column=5, padx=6, pady=5, sticky=W)

    # Binding the functions to the buttons
    search_button.config(command=lambda:search_student(root))
    showAll_button.config(command=lambda:show_all_students(root))



    # =========================Table=======================
    student_table_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Student Table",font=("times new roman",12))
    student_table_frame.place(x=0,y=110,width=695,height=410)

    scroll_x=ttk.Scrollbar(student_table_frame,orient=HORIZONTAL)      
    scroll_y=ttk.Scrollbar(student_table_frame,orient=VERTICAL)  

    student_table = ttk.Treeview(student_table_frame,columns=("Dep","Year","Sem","PRN","Name","Div","Roll","Gender","Mobile","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)

    student_table.heading("Dep",text="Department")
    student_table.heading("Year",text="Year")
    student_table.heading("Sem",text="Semester")
    student_table.heading("PRN",text="PRN")
    student_table.heading("Name",text="Name")
    student_table.heading("Div",text="Division")
    student_table.heading("Roll",text="Roll No.")
    student_table.heading("Gender",text="Gender")
    student_table.heading("Mobile",text="Mobile")
    student_table.heading("Photo",text="Photo Taken")
    student_table["show"] = "headings"

    student_table.column("Dep",width=100)
    student_table.column("Year",width=100)
    student_table.column("Sem",width=100)
    student_table.column("PRN",width=100)
    student_table.column("Name",width=100)
    student_table.column("Div",width=100)
    student_table.column("Roll",width=100)
    student_table.column("Gender",width=100)
    student_table.column("Mobile",width=100)
    student_table.column("Photo",width=100)

    student_table.pack(fill=BOTH,expand=1)
    student_table.bind("<ButtonRelease>",get_cursor)
    fetch_data()







# ============functions=============

# ==========fetch data ==========
def fetch_data():
    try:
        conn = get_database_connection()
        my_cursur = conn.cursor()
        my_cursur.execute("select * from student")
        data = my_cursur.fetchall()

        if len(data)!=0:
            student_table.delete(*student_table.get_children())
            for i in data:
                student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  
    except Exception as error:
        messagebox.showinfo("Error",f"Due To:{str(error)}",parent=root)

# ========get cursor ===========
def get_cursor(event=""):
    cursor_focus = student_table.focus()
    content = student_table.item(cursor_focus)
    data = content["values"]

    if data:  # Check if data is not empty
        # Check if data has sufficient elements before assigning values
        if len(data) >= 10:
            var_dep.set(data[0])
            var_year.set(data[1])
            var_sem.set(data[2])
            var_PRN.set(data[3])
            var_name.set(data[4])
            var_div.set(data[5])
            var_roll.set(data[6])
            var_gender.set(data[7])
            var_mobile.set(data[8])
            var_radio.set(data[9])


# =========add data ============
def add_data(root):
    if var_dep.get()=="Select Department" or var_name.get() == "" or var_PRN.get() == "":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        try:
            conn = get_database_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                var_dep.get(),
                var_year.get(),
                var_sem.get(),
                var_PRN.get(),
                var_name.get(),
                var_div.get(),
                var_roll.get(),
                var_gender.get(),
                var_mobile.get(),
                "No"  # Default value for var_radio set to "No"
            ))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details have been added successfully",parent=root)
            
        except Exception as error:
            messagebox.showinfo("Error",f"Due To:{str(error)}",parent=root)


#========= update data =========
def update_data(root):
    if var_dep.get()=="Select Department" or var_name.get() == "" or var_PRN.get() == "":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        try:
            update = messagebox.askyesno("Update","Do you want to update this Student Details",parent=root)
            if update > 0:
                conn = get_database_connection()
                my_cursor = conn.cursor()
                
                # If a photo sample is taken, update var_radio to "Yes"
                if var_radio.get() == "Yes":
                    radio_value = "Yes"
                else:
                    radio_value = "No"
                    
                my_cursor.execute("update student set Dep=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Mobile=%s,PhotoSample=%s where PRN=%s",(
                    var_dep.get(),
                    var_year.get(),
                    var_sem.get(),
                    var_name.get(),
                    var_div.get(),
                    var_roll.get(),
                    var_gender.get(),
                    var_mobile.get(),
                    radio_value,
                    var_PRN.get()
                ))
                
                conn.commit()
                fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been updated successfully",parent=root)
                
            else:
                if not update:
                    return
        except Exception as error:
            messagebox.showinfo("Error",f"Due To:{str(error)}",parent=root)


# ======Delete data ========
def delete_data(root):
    if var_PRN.get() == "":
        messagebox.showerror("Error", "Student PRN must be required", parent=root)
    else:
        try:
            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this Student", parent=root)
            if delete > 0:
                conn = get_database_connection()
                my_cursor = conn.cursor()
                # Fetching the user's data before deletion
                my_cursor.execute("SELECT * FROM student WHERE PRN=%s", (var_PRN.get(),))
                data = my_cursor.fetchone()
                if data:
                   if data[9] == "Yes":  
                        prn_value = int(var_PRN.get())
                        for img_id in range(1, 101):  
                            file_path = f"data/user.{prn_value}.{img_id}.jpg"
                            try:
                                os.remove(file_path)
                            except FileNotFoundError:
                                pass  # Skip if the file doesn't exist
                sql = "DELETE FROM student WHERE PRN=%s"
                val = (var_PRN.get(),)
                my_cursor.execute(sql, val)
                conn.commit()
                fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been Deleted Successfully", parent=root)
        except Exception as error:
            messagebox.showerror("Error", f"Due To: {str(error)}", parent=root)

# ========reset data =========
def reset_data():
    var_dep.set("Select Department"),
    var_year.set("Select Final Year"),
    var_sem.set("Select Semester"),
    var_PRN.set(""),
    var_name.set(""),
    var_div.set("Select Division"),
    var_roll.set(""),
    var_gender.set("Male"),
    var_mobile.set(""),
    var_radio.set("")



# =============generate data set and take photo samples=====
def generate_dataset(root):
    if var_dep.get() == "Select Department" or var_name.get() == "" or var_PRN.get() == "":
        messagebox.showerror("Error", "Please fill all the required fields before taking a photo sample", parent=root)
    else:
        try:
            conn = get_database_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE PRN=%s", (var_PRN.get(),))
            user_data = my_cursor.fetchone()

            if user_data:
                update = messagebox.askyesno("Update", "Do you want to take photo sample", parent=root)
                if update:
                    curr_PRN = int(var_PRN.get())

                    prn_value = int(user_data[3])
                    
                    if prn_value == curr_PRN:
                        var_radio.set("Yes")

                        # Updating the database with new values
                        my_cursor.execute("UPDATE student SET Dep=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Mobile=%s, PhotoSample=%s WHERE PRN=%s", (
                            var_dep.get(),
                            var_year.get(),
                            var_sem.get(),
                            var_name.get(),
                            var_div.get(),
                            var_roll.get(),
                            var_gender.get(),
                            var_mobile.get(),
                            var_radio.get(),
                            curr_PRN
                        ))

                        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
                        def face_cropped(img):
                            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                            for (x, y, w, h) in faces:
                                face_cropped = img[y:y+h, x:x+w]
                                return face_cropped

                        if prn_value == curr_PRN:
                            cap = cv2.VideoCapture(0)
                            img_id = 0
                            while True:
                                ret, my_frame = cap.read()

                                if ret:
                                    cropped_face = face_cropped(my_frame)
                                    
                                    if cropped_face is not None:
                                        img_id += 1
                                        face = cv2.resize(cropped_face, (450, 450))
                                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                        file_name_path = f"data/user.{curr_PRN}.{img_id}.jpg"
                                        cv2.imwrite(file_name_path, face)
                                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                        cv2.imshow("Cropped Face", face)


                                if cv2.waitKey(1) == 13 or int(img_id) == 500:
                                    break
                            cap.release()
                            cv2.destroyAllWindows()
                            messagebox.showinfo("Result", "Generating Data Sets Completed!!", parent=root)
                        
                    conn.commit()
                    fetch_data()
                    reset_data()            
                    conn.close()
                else:
                    return
            else:
                messagebox.showerror("Error", "Please save the user before taking a photo sample", parent=root)

        except Exception as error:
            messagebox.showinfo("Error", f"Due To: {str(error)}", parent=root)

# Function to search for a specific student
def search_student(root):
    search_by = search_combo.get()
    search_text = search_entry.get()
    try:
        conn = get_database_connection()
        my_cursor = conn.cursor()
        if search_by == "PRN":
            my_cursor.execute("SELECT * FROM student WHERE PRN=%s", (search_text,))
        elif search_by == "Roll No.":
            my_cursor.execute("SELECT * FROM student WHERE Roll=%s", (search_text,))
        else:
            messagebox.showerror("Error", "Please select a valid search category.",parent=root)
            return

        data = my_cursor.fetchall()
        if data:
            student_table.delete(*student_table.get_children())
            for row in data:
                student_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Not Found", "No matching records found.",parent=root)
        conn.close()
    except Exception as error:
        messagebox.showerror("Error", f"Search error: {str(error)}",parent=root)

# Function to show all students
def show_all_students(root):
    try:
        conn = get_database_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if data:
            student_table.delete(*student_table.get_children())
            for row in data:
                student_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Empty", "No records found.",parent=root)
        conn.close()
    except Exception as error:
        messagebox.showerror("Error", f"Error in fetching data: {str(error)}",parent=root)




if __name__ == "__main__":
    root = Tk()
    Student(root)
    root.mainloop()

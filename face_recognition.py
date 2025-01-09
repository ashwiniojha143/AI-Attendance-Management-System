import os
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import mysql.connector.locales.eng.client_error
from db_connection import get_database_connection
import threading



def Face_Recognition(root):
    # configure window
    root.title("Real Time Attendance Marking System")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")
    root.wm_iconbitmap("Desktop_Icon.ico")
 
    global var_dep,var_year,var_sem,var_faculty,var_div,var_subject,var_date,var_time,right_frame,list_frame,Sort_combo,selected_file_label

    # ==========varibales=========
    var_dep = StringVar()
    var_year = StringVar()
    var_sem = StringVar()
    var_div = StringVar()
    var_faculty = StringVar()
    var_subject= StringVar()
    var_date = StringVar()
    var_time = StringVar()
    

    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Face Recognition System", font=("Helvetica", 40, "bold"), bg="white", fg='brown')
    title_label.pack(pady=20)

    # Background box with rounded edges (resembling a shadow)
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Background image inside the box
    bg_image = Image.open("public/face_bg.png")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()

    # top frame 
    top_frame = LabelFrame(background_box,bd=2,relief=RIDGE,text="Attendacne Details",font=("times new roman",15,"bold"),fg="red",bg="white")
    top_frame.place(x=10,y=10,width=1480,height=150)

    # faculty Name  
    Name_label = Label(top_frame, text="Faculty Name", font=("times new roman", 12), bg="white")
    Name_label.grid(row=0, column=0, padx=(10, 20), pady=10, sticky=W)

    Name_entry = ttk.Entry(top_frame, width=20, textvariable=var_faculty, font=("times new roman", 12))
    Name_entry.grid(row=1, column=0, padx=(10, 20), pady=10, sticky=W)

    # Subject Name  
    Subject_label = Label(top_frame, text="Subject", font=("times new roman", 12), bg="white")
    Subject_label.grid(row=0, column=2, padx=(10, 20), pady=10, sticky=W)

    Subject_entry = ttk.Entry(top_frame, width=20, textvariable=var_subject, font=("times new roman", 12))
    Subject_entry.grid(row=1, column=2, padx=(10, 20), pady=10, sticky=W)

    # Current Department 
    dep_label = Label(top_frame, text="Department", font=("times new roman", 12), bg="white")
    dep_label.grid(row=0, column=4, padx=(10, 20), pady=10, sticky=W)

    dep_combo = ttk.Combobox(top_frame, textvariable=var_dep, font=("times new roman", 12), state="readonly")
    dep_combo["values"] = ("Select Department", "Computer", "IT", "ENTC", "Civil")
    dep_combo.current(0)
    dep_combo.grid(row=1, column=4, padx=(10, 20), pady=10, sticky=W)

    # Final Year 
    year_label = Label(top_frame, text="Final Year", font=("times new roman", 12), bg="white")
    year_label.grid(row=0, column=6, padx=(10, 20), pady=10, sticky=W)

    year_combo = ttk.Combobox(top_frame, textvariable=var_year, font=("times new roman", 12), state="readonly")
    year_combo["values"] = ("Select Final Year", "2024", "2025", "2026", "2027")
    year_combo.current(0)
    year_combo.grid(row=1, column=6, padx=(10, 20), pady=10, sticky=W)

    # Current Semester 
    sem_label = Label(top_frame, text="Current Semester", font=("times new roman", 12), bg="white")
    sem_label.grid(row=0, column=8, padx=(10, 20), pady=10, sticky=W)

    sem_combo = ttk.Combobox(top_frame, textvariable=var_sem, font=("times new roman", 12), state="readonly")
    sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
    sem_combo.current(0)
    sem_combo.grid(row=1, column=8, padx=(10, 20), pady=10, sticky=W)

    # DIVISION  
    Division_label = Label(top_frame, text="Division", font=("times new roman", 12), bg="white")
    Division_label.grid(row=0, column=10, padx=(10, 20), pady=10, sticky=W)

    Division_combo = ttk.Combobox(top_frame, textvariable=var_div, font=("times new roman", 12), state="readonly")
    Division_combo["values"] = ("Select Division", "I", "II", "III")
    Division_combo.current(0)
    Division_combo.grid(row=1, column=10,  padx=(10, 20), pady=10, sticky=W)

    # Date
    date_label = Label(top_frame, text="Date", font=("times new roman", 12), bg="white")
    date_label.grid(row=0, column=12, padx=(10, 20), pady=10, sticky=W)
   

    date = datetime.now().date()
    var_date.set(date.strftime("%Y-%m-%d"))

    date_display = Label(top_frame, textvariable=var_date, font=("times new roman", 12), bg="white")
    date_display.grid(row=1, column=12, padx=(10, 20), pady=10, sticky=W)
   

    # Time
    def update_time():
        current_time = strftime('%H-%M-%S-%p')
        var_time.set(current_time)
        time_display.after(1000, update_time)

    time_label = Label(top_frame, text="Time", font=("times new roman", 12), bg="white")
    time_label.grid(row=0, column=11, padx=(10, 20), pady=10, sticky=W)

    time_display = Label(top_frame, textvariable=var_time, font=("times new roman", 12), bg="white")
    time_display.grid(row=1, column=11, padx=(10, 20), pady=10, sticky=W)

    update_time()

    # Note Label
    note_label = Label(top_frame, text="Note: Please fill the required Details before taking Attendance", font=("times new roman", 14, "bold"), bg="white", fg="red")
    note_label.place(x=10, y=90)

    # create csv file 
    create_csv_btn = Button(top_frame, text="Create Empty Attendance File", command=lambda:create_csv_file(root),cursor="hand2", width=25, font=("times new roman", 12, "bold"), bg="green", fg="white")
    create_csv_btn.place(x=1210, y=90)

    # right frame 
    right_frame = LabelFrame(background_box, bd=2, relief=RIDGE, text="List of All Attendance File", font=("times new roman", 15, "bold"), fg="red", bg="white")
    right_frame.place(x=1010, y=170, width=480, height=410)


    # Sorting ComboBox
    Sort_label = Label(right_frame, text="Order By:", font=("times new roman", 12), bg="red", fg="white")
    Sort_label.grid(row=0, column=0, padx=(10, 20), pady=10, sticky=W)

    Sort_combo = ttk.Combobox(right_frame, font=("times new roman",12), state="readonly")
    Sort_combo["values"] = ("Newest First", "Oldest First", "Name")
    Sort_combo.current(0)
    Sort_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    Show_list_button = Button(right_frame, text="Show List", command=lambda:display_csv_files(),cursor="hand2", width=10, font=("times new roman", 12, "bold"), bg="black", fg="white")
    Show_list_button.grid(row=0, column=2, padx=10, pady=10, sticky=W)

    # list frame 
    list_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
    list_frame.place(x=5, y=50, width=465, height=320)

     # Bottom frame 
    bottom_frame = LabelFrame(background_box, bd=2, relief=RIDGE, text="Selected Attendance File", font=("times new roman", 15, "bold"), fg="red", bg="white")
    bottom_frame.place(x=550, y=590, width=940, height=60)

    selected_file_label = Label(bottom_frame, text="", font=("times new roman", 12), bg="white")
    selected_file_label.place(x=5)

    # Button
    Recog_btn_image = Image.open("public/face_detect.jpg")
    Recog_btn_image = Recog_btn_image.resize((300, 300), Image.LANCZOS)
    Recog_btn_photo = ImageTk.PhotoImage(Recog_btn_image)

    btn1 = Button(background_box, image=Recog_btn_photo ,borderwidth=5, command=lambda:face_recog(root))
    btn1.image = Recog_btn_photo 
    btn1.place(x=550, y=200)


def display_csv_files():

    global listbox
    file_list = os.listdir("attendance_report")

    sort_criteria = Sort_combo.get()

    if sort_criteria == "Name":
        file_list.sort() 
    elif sort_criteria == "Oldest First":
        file_list.sort(key=lambda x: os.path.getctime(f"attendance_report/{x}"))
    else:
        file_list.sort(key=lambda x: os.path.getctime(f"attendance_report/{x}"), reverse=True)

    for widget in list_frame.winfo_children():
        widget.destroy()

    listbox = Listbox(list_frame, width=55, height=20, font=("times new roman", 12))
    listbox.pack(side="left", fill="y")

    def on_select(event):
        global selected_file
        selected_index = listbox.curselection()
        selected_file = file_list[selected_index[0]] if selected_index else ""
        selected_file_label.config(text=f"Selected File: {selected_file}")

        # Check if the selection is valid and then proceed
        if selected_index:
            
            selected_item_text = listbox.get(selected_index)
            
            selected_filename = selected_item_text.split(". ")[1]

            
            selected_file = selected_filename
            selected_file_label.config(text=f"Selected File: {selected_filename}")
        else:
            selected_file = ""  


    listbox.bind('<<ListboxSelect>>', on_select)


    for index, file_name in enumerate(file_list, start=1):
        listbox.insert(END, f"{index}. {file_name}")

    scrollbar = Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    xscrollbar = Scrollbar(list_frame, orient="horizontal")
    xscrollbar.config(command=listbox.xview)
    xscrollbar.pack(side="bottom", fill="x")

    listbox.config(yscrollcommand=scrollbar.set, xscrollcommand=xscrollbar.set)


# Function to handle CSV file creation
def create_csv_file(root):
    global csv_file_name
    if (
        var_faculty.get() != ""
        and var_subject.get() != ""
        and var_dep.get() != "Select Department"
        and var_year.get() != "Select Final Year"
        and var_sem.get() != "Select Semester"
        and var_div.get() != "Select Division"
    ):
        # Concatenate all variables to create the CSV file name
        csv_file_name = f"{var_dep.get()}_{var_year.get()}_{var_sem.get()}_{var_div.get()}_{var_faculty.get()}_{var_subject.get()}_{var_date.get()}_{var_time.get()}.csv"

        try:
            with open(f"attendance_report/{csv_file_name}", "w", newline="\n") as f:
                pass  
            messagebox.showinfo("Success", f"{csv_file_name} created successfully!", parent=root)
        except Exception as e:
            messagebox.showerror("Error", f"Error creating file: {e}", parent=root)
    else:
        messagebox.showerror("Error", "All fields are required!",parent=root)


# ==============Mark attendance functions ================

def mark_attendance(p, r, n, d, selected_file):
    try:
        with open(f"attendance_report/{selected_file}", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]
            if (p not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{p},{r},{n},{d},{dtString},{d1},Present")
    except FileNotFoundError:
        messagebox.showerror("File Error", f"File '{selected_file}' not found!", parent=root)
    except Exception as e:
        messagebox.showerror("Error", f"Error marking attendance: {e}", parent=root)


# make frame 
def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
    try:
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            conn = get_database_connection()
            my_cursor = conn.cursor()

            my_cursor.execute("select Name from student where PRN=" + str(id))
            n = my_cursor.fetchone()
            if n:  
                n = "+".join(n)
            else:
                n = ""  

            my_cursor.execute("select Roll from student where PRN=" + str(id))
            r = my_cursor.fetchone()
            if r:  
                r = "+".join(r)
            else:
                r = ""  
            my_cursor.execute("select Dep from student where PRN=" + str(id))
            d = my_cursor.fetchone()
            if d:  
                d = "+".join(d)
            else:
                d = ""  

            my_cursor.execute("select PRN from student where PRN=" + str(id))
            p = my_cursor.fetchone()
            if p:  
                p = "+".join(p)
            else:
                p = ""  

            if confidence > 77:
                cv2.putText(img, f"PRN:{p}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                if p and r and n and d: 
                    mark_attendance(p, r, n, d, selected_file)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, f"Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        return img
    except Exception as e:
        messagebox.showerror("Error", f"Error in boundary drawing: {e}", parent=root)


# Function for countdown timer
def countdown_timer():
    seconds = 30
    while seconds > 0:
        print("Time Left: {seconds}")
        seconds -= 1
        time.sleep(1)


def recognize(img, clf, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
    return img

selected_file=""

def face_recog(root):
    global selected_file
    if selected_file:
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        try:
            start_time = time.time()
            while True:
                ret, img = video_cap.read()
                if ret:
                    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
                    elapsed_time = int(time.time() - start_time)
                    remaining_time = max(0, 20 - elapsed_time)
                    cv2.putText(img, f"Time Left: {remaining_time}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 2)
                    cv2.imshow(f"Welcome to Face Recognition", img)

                    if elapsed_time >= 20:
                        break

                    key = cv2.waitKey(1)
                    if key == 13:
                        break

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}", parent=root)

        finally:
            if video_cap.isOpened():
                video_cap.release()
                cv2.destroyAllWindows()

    else:
        messagebox.showinfo("Select File", "Please select a file to take attendance!", parent=root)




if __name__ == "__main__":
    root = Tk()
    Face_Recognition(root)
    root.mainloop()
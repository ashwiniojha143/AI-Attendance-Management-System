from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from about import About
from help import Help
import os
from time import strftime
from datetime import datetime

def main(root):
    try:
        # configure window
        root.title("Real Time Attendance Marking System")
        root.configure(background="gray")
        root.geometry("1520x780+0+0")
        root.wm_iconbitmap("Desktop_Icon.ico")



        # Header
        header_frame = ttk.Frame(root, style="Header.TFrame")
        header_frame.place(x=10, y=10, width=1500, height=100)

        style = ttk.Style()
        style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

        # Title in the header
        title_label = Label(header_frame, text="Attendance Marking System", font=("Helvetica", 40, "bold"), bg="white", fg='skyblue')
        title_label.pack(pady=20)

        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(header_frame,font=('times new roman',14,'bold'),background='white',foreground='black')
        lbl.place(x=10,y=20,width=110,height=50)
        time()

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


        # Student Information
        btn_image1 = Image.open("public/register.png")
        btn_image1 = btn_image1.resize((200, 200), Image.LANCZOS)
        btn_photo1 = ImageTk.PhotoImage(btn_image1)

        btn1_text = Button(background_box,command=lambda:student_details(root), text="Attendee Information", font=("Helvetica", 14, "bold"),bg="skyblue", fg='black',width=17)
        btn1_text.place(x=40, y=50)  

        btn1 = Button(background_box,command=lambda:student_details(root), image=btn_photo1, borderwidth=5)
        btn1.image = btn_photo1  
        btn1.place(x=40, y=80) 


        # Train Data
        btn_image4 = Image.open("public/train_model.png")
        btn_image4 = btn_image4.resize((200, 200), Image.LANCZOS)
        btn_photo4 = ImageTk.PhotoImage(btn_image4)

        btn4_text = Button(background_box, text="Train Data",command=lambda:train_data(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn4_text.place(x=450, y=50)  

        btn4 = Button(background_box, image=btn_photo4, borderwidth=5,command=lambda:train_data(root))
        btn4.image = btn_photo4  
        btn4.place(x=450, y=80) 


        # Face Detector 
        btn_image2 = Image.open("public/face_recog.png")
        btn_image2 = btn_image2.resize((200, 200), Image.LANCZOS)
        btn_photo2 = ImageTk.PhotoImage(btn_image2)

        btn2_text = Button(background_box, text="Face Detector",command=lambda:face_detection(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn2_text.place(x=850, y=50)  

        btn2 = Button(background_box, image=btn_photo2, borderwidth=5,command=lambda:face_detection(root))
        btn2.image = btn_photo2 
        btn2.place(x=850, y=80) 


        # Student Attendance
        btn_image3 = Image.open("public/attendance.jpg")
        btn_image3 = btn_image3.resize((200, 200), Image.LANCZOS)
        btn_photo3 = ImageTk.PhotoImage(btn_image3)

        btn3_text = Button(background_box, text="Attendance",command=lambda:attendance_report(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn3_text.place(x=1250, y=50)  

        btn3 = Button(background_box, image=btn_photo3, borderwidth=5,command=lambda:attendance_report(root))
        btn3.image = btn_photo3  
        btn3.place(x=1250, y=80) 



        # Student Photos
        btn_image1 = Image.open("public/gallery.jpeg")
        btn_image1 = btn_image1.resize((200, 200), Image.LANCZOS)
        btn_photo1 = ImageTk.PhotoImage(btn_image1)

        btn1_text = Button(background_box, text="Attendee Photos",command=lambda:open_image(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn1_text.place(x=40, y=350)  

        btn1 = Button(background_box, image=btn_photo1, borderwidth=5,command=lambda:open_image(root))
        btn1.image = btn_photo1  
        btn1.place(x=40, y=380) 


        # About Us 
        btn_image2 = Image.open("public/developer.jpg")
        btn_image2 = btn_image2.resize((200, 200), Image.LANCZOS)
        btn_photo2 = ImageTk.PhotoImage(btn_image2)

        btn2_text = Button(background_box, text="Developers",command=lambda:about_us(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn2_text.place(x=450, y=350)  

        btn2 = Button(background_box, image=btn_photo2, borderwidth=5,command=lambda:about_us(root))
        btn2.image = btn_photo2 
        btn2.place(x=450, y=380) 


        # Help Contact 
        btn_image3 = Image.open("public/help.png")
        btn_image3 = btn_image3.resize((200, 200), Image.LANCZOS)
        btn_photo3 = ImageTk.PhotoImage(btn_image3)

        btn3_text = Button(background_box, text="Help",command=lambda:help_func(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn3_text.place(x=850, y=350)  

        btn3 = Button(background_box, image=btn_photo3, borderwidth=5,command=lambda:help_func(root))
        btn3.image = btn_photo3  
        btn3.place(x=850, y=380) 


        # Exit 
        btn_image4 = Image.open("public/exit.png")
        btn_image4 = btn_image4.resize((200, 200), Image.LANCZOS)
        btn_photo4 = ImageTk.PhotoImage(btn_image4)

        btn4_text = Button(background_box, text="Exit Application",command=lambda:main_exit(root), font=("Helvetica", 14, "bold"), bg="skyblue", fg='black',width=17)
        btn4_text.place(x=1250, y=350)  

        btn4 = Button(background_box, image=btn_photo4, borderwidth=5,command=lambda:main_exit(root))
        btn4.image = btn_photo4  
        btn4.place(x=1250, y=380) 
    except Exception as e:
        messagebox.showerror("Error", f"Error in Train function: {e}", parent=root)




# Function for opening images
def open_image(root):
    try:
        os.startfile("data")
    except FileNotFoundError as e:
        messagebox.showerror("Error", f"File not found: {e}", parent=root)
    except OSError as e:
        messagebox.showerror("OS Error", f"OS Error: {e}", parent=root)

# Handle Student Details window creation
def student_details(root):
    try:
        new_window = Toplevel(root)
        app = Student(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating Student Details window: {e}", parent=root)

# Handle Train Data window creation
def train_data(root):
    try:
        new_window = Toplevel(root)
        app = Train(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating Train Data window: {e}", parent=root)

# Handle Face Detection window creation
def face_detection(root):
    try:
        new_window = Toplevel(root)
        app = Face_Recognition(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating Face Detection window: {e}", parent=root)

# Handle Attendance Report window creation
def attendance_report(root):
    try:
        new_window = Toplevel(root)
        app = Attendance(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating Attendance Report window: {e}", parent=root)

# Handle About Us window creation
def about_us(root):
    try:
        new_window = Toplevel(root)
        app = About(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating About Us window: {e}", parent=root)

# Handle Help window creation
def help_func(root):
    try:
        new_window = Toplevel(root)
        app = Help(new_window)
    except Exception as e:
        messagebox.showerror("Error", f"Error creating Help window: {e}", parent=root)

# Handle main exit
def main_exit(root):
    try:
        main_exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit", parent=root)
        if main_exit > 0:
            root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Error during exit: {e}", parent=root)




if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


def About(root):
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
    title_label = Label(header_frame, text="About Us", font=("Helvetica", 40, "bold"), bg="white", fg='green')
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

    # Top Frame
    top_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Prof. D.K. Ray", font=("times new roman", 15,"bold"), fg="red")
    top_frame.place(x=15,y=5, width=1435, height=200)

    # Load and resize the teacher's photo
    btn_image1 = Image.open(r"C:\Users\Ashwini\AI-Face-Recogniotion-Attendance-Management\public\ajay sir.png")            #Ajay sir photo change 
    btn_image1 = btn_image1.resize((120, 150), Image.LANCZOS)
    btn_photo1 = ImageTk.PhotoImage(btn_image1)

    # Display the teacher's photo in the top frame
    image_label = Label(top_frame, image=btn_photo1)
    image_label.image = btn_photo1
    image_label.place(x=15, y=10)

    # Teacher's name in the middle, top, in large size
    teacher_name_label = Label(top_frame, text="Prof. Dr. Ajay Kumar Kushwaha", font=("times new roman", 25,"bold"), fg="black")
    teacher_name_label.place(relx=0.5, rely=0.15, anchor="center")  # Positioned in the center horizontally

    # Project Description
    project_label = Label(top_frame, text="Final Year Project: Real time Attendance marking system using face recognition ", font=("times new roman", 18), fg="black")
    project_label.place(relx=0.5, rely=0.35, anchor="center")  # Positioned in the center horizontally

    # Guidance Note
    guidance_label = Label(top_frame, text="Under the guidance of Prof. Dr. Ajay Kumar Kushwaha", font=("times new roman", 14), fg="black")
    guidance_label.place(relx=0.5, rely=0.55, anchor="center")  # Positioned in the center horizontally

    # Additional beautiful lines about the project
    beautiful_lines = Label(top_frame, text="Through pixels and code, faces unfold, In the tapestry of AI, stories untold", font=("times new roman", 14), fg="black")
    beautiful_lines.place(relx=0.5, rely=0.75, anchor="center")

    # Left Frame - Student 1 Details
    left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Ashwini ", font=("times new roman", 15,"bold"), fg="green")
    left_frame.place(x=10, y=220, width=352, height=300)

    # Load and resize Student 1's image
    student1_image = Image.open("public/Ashwini.png")
    student1_image = student1_image.resize((120, 150), Image.LANCZOS)
    student1_photo = ImageTk.PhotoImage(student1_image)

    # Display Student 1's image in the middle
    student1_label = Label(left_frame, image=student1_photo)
    student1_label.image = student1_photo
    student1_label.place(relx=0.5, rely=0.25, anchor="center")

    # Student 1's name just below the image
    student1_name_label = Label(left_frame, text="Ashwini Ojha", font=("times new roman", 20,"bold"), fg="black")
    student1_name_label.place(relx=0.5, rely=0.5, anchor="center")

    # Student 1's details
    student1_details_label = Label(left_frame, text="Electronics and Telecommunication\nContact: +91 9693961331\nEmail: ashwaniojha021@gmail.com", font=("times new roman", 14), fg="black")
    student1_details_label.place(relx=0.5, rely=0.75, anchor="center")

      # Left Frame - Student 2 Details
    left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Somya", font=("times new roman", 15,"bold"), fg="green")
    left_frame.place(x=362, y=220, width=352, height=300)

    # Load and resize Student 2's image
    student1_image = Image.open(r"C:\Users\Ashwini\AI-Face-Recogniotion-Attendance-Management\public\somya.png")
    student1_image = student1_image.resize((120, 150), Image.LANCZOS)
    student1_photo = ImageTk.PhotoImage(student1_image)

    # Display Student 2's image in the middle
    student1_label = Label(left_frame, image=student1_photo)
    student1_label.image = student1_photo
    student1_label.place(relx=0.5, rely=0.25, anchor="center")

    # Student 2's name just below the image
    student1_name_label = Label(left_frame, text="Somya Kumari", font=("times new roman", 20,"bold"), fg="black")
    student1_name_label.place(relx=0.5, rely=0.5, anchor="center")

    # Student 2's details
    student1_details_label = Label(left_frame, text="Electronics and Telecommunication\nContact: +91 6201142529\nEmail: skumari21-etc@bvucoep.edu.in", font=("times new roman", 14), fg="black")
    student1_details_label.place(relx=0.5, rely=0.75, anchor="center")

    # Middle Frame - Student 3 Details
    mid_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Ankit ", font=("times new roman", 15,"bold"), fg="green")
    mid_frame.place(x=724, y=220, width=352, height=300)

    # Load and resize Student 3's image
    student2_image = Image.open(r"C:\Users\Ashwini\AI-Face-Recogniotion-Attendance-Management\public\ankit.png")
    student2_image = student2_image.resize((120, 150), Image.LANCZOS)
    student2_photo = ImageTk.PhotoImage(student2_image)

    # Display Student 3's image in the middle
    student2_label = Label(mid_frame, image=student2_photo)
    student2_label.image = student2_photo
    student2_label.place(relx=0.5, rely=0.25, anchor="center")

    # Student 3's name just below the image
    student2_name_label = Label(mid_frame, text="Ankit Raj", font=("times new roman", 20,"bold"), fg="black")
    student2_name_label.place(relx=0.5, rely=0.5, anchor="center")

    # Student 3's details
    student2_details_label = Label(mid_frame, text="Electronics and Telecommunication\nContact: +91 7209956659\nEmail: araj21-etc@bvucoep.edu.in", font=("times new roman", 14), fg="black")
    student2_details_label.place(relx=0.5, rely=0.75, anchor="center")

    # Right Frame - Student 4 Details
    right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Ankit ", font=("times new roman", 15,"bold"), fg="green")
    right_frame.place(x=1086, y=220, width=352, height=300)

    # Load and resize Student 4's image
    student3_image = Image.open(r"C:\Users\Ashwini\AI-Face-Recogniotion-Attendance-Management\public\deadpool.png")
    student3_image = student3_image.resize((120, 150), Image.LANCZOS)
    student3_photo = ImageTk.PhotoImage(student3_image)

    # Display Student 4's image in the middle
    student3_label = Label(right_frame, image=student3_photo)
    student3_label.image = student3_photo
    student3_label.place(relx=0.5, rely=0.25, anchor="center")

    # Student 4's name just below the image
    student3_name_label = Label(right_frame, text="Ankit Raj", font=("times new roman", 20,"bold"), fg="black")
    student3_name_label.place(relx=0.5, rely=0.5, anchor="center")

    # Student 4's details
    student3_details_label = Label(right_frame, text="Electronics and Telecommunication\nContact: +91 7061179675\nEmail: araj121-etc@bvucoep.edu.in", font=("times new roman", 14), fg="black")
    student3_details_label.place(relx=0.5, rely=0.75, anchor="center")

if __name__ == "__main__":
    root = Tk()
    About(root)
    root.mainloop()
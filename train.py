import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

def Train(root):
    try:
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
        title_label = Label(header_frame, text="Train Model Using Multiple Face Data", font=("Helvetica", 40, "bold"), bg="white", fg='red')
        title_label.pack(pady=20)

        # Background box
        background_box = ttk.Frame(root, style="Background.TFrame")
        background_box.place(x=10, y=110, width=1500, height=660)
        style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

        # Background image
        bg_image = Image.open("public/background.jpg")
        bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(background_box, image=bg_photo)
        bg_label.image = bg_photo  
        bg_label.pack()

        # Button
        train_btn_image = Image.open("public/train_model.png")
        train_btn_image = train_btn_image.resize((200, 200), Image.LANCZOS)
        train_btn_photo = ImageTk.PhotoImage(train_btn_image)
        btn1 = Button(background_box, image=train_btn_photo, borderwidth=0, command=lambda: train_classifier(root))
        btn1.image = train_btn_photo 
        btn1.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the button
    except Exception as e:
        messagebox.showerror("Error", f"Error in Train function: {e}", parent=root)

# Training Classifier Function
def train_classifier(root):
    try:
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        messagebox.showinfo("Result", "Training datasets Completed", parent=root)
        cv2.destroyAllWindows()

    except FileNotFoundError as e:
        messagebox.showerror("File Not Found", f"File not found: {e}", parent=root)
    except OSError as e:
        messagebox.showerror("OS Error", f"OS Error: {e}", parent=root)
    except Exception as e:
        messagebox.showerror("Error", f"Error in train_classifier function: {e}", parent=root)


if __name__ == "__main__":
    root = Tk()
    Train(root)
    root.mainloop()

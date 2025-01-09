from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

rapid_api_key = config.get('RapidAPI', 'API_KEY')
rapid_api_host = config.get('RapidAPI', 'HOST')

url = "https://" + rapid_api_host + "/ask"

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": rapid_api_key,
    "X-RapidAPI-Host": rapid_api_host
}

global root

def Help(root):
    try:
        root.title("Attendance marking system using multiple face recognition system")
        root.configure(background="lightgray")
        root.geometry("1520x780+0+0")
        root.wm_iconbitmap("Desktop_Icon.ico")

        # Header
        header_frame = ttk.Frame(root, style="Header.TFrame")
        header_frame.place(x=10, y=10, width=1500, height=100)
        style = ttk.Style()
        style.configure("Header.TFrame", background="white", relief="raised")

        # Title in the header
        title_label = Label(header_frame, text="Help - Facial Recognition & Attendance System", font=("Helvetica", 30, "bold"), bg="white", fg='#3498db')
        title_label.pack(pady=20)

        # Background box
        background_box = ttk.Frame(root, style="Background.TFrame")
        background_box.place(x=10, y=110, width=1500, height=660)
        style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove")

        # Background image inside the box
        bg_image = Image.open("public/background.jpg")
        bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = Label(background_box, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.pack()

        # Main frame
        main_frame = Frame(background_box, bd=2, bg="white")
        main_frame.place(x=15, y=30, width=600, height=600)

        # Add content to the main frame
        section_title = Label(main_frame, text="Welcome to Help Section", font=("Helvetica", 20, "bold"), bg="white", fg="#3498db")
        section_title.pack(pady=20)


        # Section 2 - Process

        process_text = Text(main_frame, wrap=WORD, font=("Helvetica", 10), height=10, width=70)
        process_text.insert(END, "1. Start the system.\n\n2. Register and Gather the Students Details\n\n3. Make Sure that the every student have their respective images.\n\n4. Train the Model.\n\n5. Start Recognition and Mark Attendance.\n\n6. Review attendance logs.")
        process_text.place(x=0,y=50)


        # Chat frame
        chat_frame = LabelFrame(root, text='Rapid API ChatBot To Improve Your Q&A', bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"), fg="red")
        chat_frame.place(x=30, y=370, width=590, height=360)

        chat_log = Text(chat_frame, wrap=WORD, font=("Helvetica", 10), height=15, width=70)
        chat_log.pack(padx=10, pady=10)

        user_input = Entry(chat_frame, width=50, fg="green")
        user_input.pack(pady=5)
        user_input.bind("<Return>", lambda event: send_message(user_input, chat_log, event))

        send_button = Button(chat_frame, text="Send", command=lambda: send_message(user_input, chat_log), cursor="hand2", width=10, font=("times new roman", 12, "bold"), bg="black", fg="white")
        send_button.pack()

        

        # section 3     
        video_canvas = Canvas(background_box, bg="black")
        video_canvas.place(x=630, y=30, width=860, height=600)

        video_frames = [
            "public/page1.png",
            "public/page2.png",
            "public/page3.png",
            "public/page4.png",
            "public/page5.png",
            "public/page6.png",
        ]
        video_image_list = [Image.open(frame).resize((860, 660), Image.LANCZOS) for frame in video_frames]
        video_photo_list = [ImageTk.PhotoImage(img) for img in video_image_list]

        def update_video_frame(idx):
            video_canvas.create_image(0, 0, anchor=NW, image=video_photo_list[idx])
            root.after(2000, lambda: update_video_frame((idx + 1) % len(video_photo_list)))

        update_video_frame(0)
    except configparser.Error as e:
        messagebox.showerror("Config Error", f"Error reading config.ini: {e}", parent=root)
    except FileNotFoundError as e:
        messagebox.showerror("File Not Found", f"File not found: {e}", parent=root)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Rapid API Error", f"Error connecting to Rapid API: {e}", parent=root)
    except Exception as e:
        messagebox.showerror("Error", f"Error in Help function: {e}", parent=root)


def send_message(user_input, chat_log, event=None):
    try:
        message = user_input.get()
        chat_log.config(state=NORMAL)
        chat_log.tag_config("user", foreground="blue")
        chat_log.tag_config("bot", foreground="red", background="yellow")

        chat_log.insert(END, "You: " + message + "\n", "user")

        payload = {
            "query": message,
            "wordLimit": "50"
        }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        ai_reply = response_data['response']

        chat_log.insert(END, "ChatBot: " + ai_reply + "\n", "bot")
        chat_log.config(state=DISABLED)

        user_input.delete(0, END)
    except Exception as e:
        print(f"Error in send_message function: {e}")



if __name__ == "__main__":
    root = Tk()
    Help(root)
    root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import webbrowser

def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="login"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS login")
    cursor.execute("USE login")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), age INT, email VARCHAR(255), phone VARCHAR(15))")

    connection.commit()
    connection.close()

def open_forgot_password_link():
    webbrowser.open("https://example.com/forgot_password")

def login_screen():
    options_frame.pack_forget()
    register_frame.pack_forget()
    login_frame.pack()

def register_screen():
    login_frame.pack_forget()
    register_frame.pack()
    options_frame.pack_forget()

def options_screen():
    login_frame.pack_forget()
    register_frame.pack_forget()
    username = login_username.get()
    password = login_password.get()

    # Check if user exists in the database
    if check_user_in_database(username, password):
        options_frame = Frame(root, bg='#f0f0f0') 
        # Back button for Options Screen
        back_button_options = Button(options_frame, command=lambda: [options_frame.pack_forget(), login_screen()], bg='#f0f0f0', bd=0)
        back_icon = Image.open("C:\\Users\\Aditya\\OneDrive\\Desktop\\pngtree-vector-back-icon-png-image_931209.jpg")
        back_icon = back_icon.resize((25, 25), Image.LANCZOS)
        back_photo = ImageTk.PhotoImage(back_icon)
        back_button_options.config(image=back_photo)
        back_button_options.image = back_photo
        back_button_options.place(relx=0.02, rely=0.02) # Adjusted position

        # Option  1
        option1_frame = Frame(options_frame, bg='#f0f0f0')
        option1_frame.place(relx=0.5, rely=0.2, anchor="center")
 
        image1 = Image.open("C:\\Users\\Aditya\\OneDrive\\Desktop\\WhatsApp Image 2023-12-24 at 00.16.59_b235e783.jpg")
        image1 = image1.resize((200, 200), Image.LANCZOS)
        photo1 = ImageTk.PhotoImage(image1)
        option1_button = Button(option1_frame, text="Food Donators", image=photo1, compound="top", command=option1_function, bg='#f0f0f0', bd=0)
        option1_button.image = photo1
        option1_button.pack()

        # Option 2
        option2_frame = Frame(options_frame, bg='#f0f0f0')
        option2_frame.place(relx=0.5, rely=0.5, anchor="center")

        image2 = Image.open("C:\\Users\\Aditya\\OneDrive\\Desktop\\WhatsApp Image 2023-12-24 at 00.16.59_a7014c33.jpg")
        image2 = image2.resize((200, 200), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(image2)
        option2_button = Button(option2_frame, text="NGO", image=photo2, compound="top", command=option2_function, bg='#f0f0f0', bd=0)
        option2_button.image = photo2
        option2_button.pack()

        # Option 3
        option3_frame = Frame(options_frame, bg='#f0f0f0')
        option3_frame.place(relx=0.5, rely=0.8, anchor="center")

        image3 = Image.open("C:\\Users\\Aditya\\OneDrive\\Desktop\\WhatsApp Image 2023-12-24 at 00.16.58_c402b7c4.jpg")
        image3 = image3.resize((200, 200), Image.LANCZOS)
        photo3 = ImageTk.PhotoImage(image3)
        option3_button = Button(option3_frame, text="Nutrition Checker", image=photo3, compound="top", command=option3_function, bg='#f0f0f0', bd=0)
        option3_button.image = photo3
        option3_button.pack()

        options_frame.pack(fill=BOTH, expand=True)
    else:
        messagebox.showerror("Login Failed", "User not found. Please register.")

def check_user_in_database(username, password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="login"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    return result is not None

def option1_function():
    messagebox.showinfo("Option 1", "You clicked Food Donators!")

def option2_function():
    messagebox.showinfo("Option 2", "You clicked NGO!")

def option3_function():
    messagebox.showinfo("Option 3", "You clicked Nutrition Checker!")

def register():
    username = register_username.get()
    password = register_password.get()
    age = register_age.get()
    email = register_email.get()
    phone = register_phone.get()

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="login"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose another.")
    else:
        cursor.execute("INSERT INTO users (username, password, age, email, phone) VALUES (%s, %s, %s, %s, %s)", (username, password, age, email, phone))
        messagebox.showinfo("Registration Successful", "User registered successfully!")

    connection.commit()
    connection.close()

# Main window
root = Tk()
root.title("User Authentication")
root.geometry("480x853")
root.configure(bg='#f0f0f0')

create_database()

# Frames
login_frame = Frame(root, bg='#f0f0f0')
register_frame = Frame(root, bg='#f0f0f0')
options_frame = Frame(root, bg='#f0f0f0')

# Login Frame
login_label = Label(login_frame, text="LOGIN", font=("Arial", 40, "bold"), bg='#f0f0f0', fg='black')
login_label.pack(pady=(120, 0), anchor="center")

login_username_label = Label(login_frame, text="Username:", bg='#f0f0f0', fg='black')
login_username_label.pack()

login_username = Entry(login_frame)
login_username.pack()

login_password_label = Label(login_frame, text="Password:", bg='#f0f0f0', fg='black')
login_password_label.pack()

login_password = Entry(login_frame, show="*")
login_password.pack()

login_button = Button(login_frame, text="Login", command=options_screen, bg='black', fg='white', font=("Arial", 14))
login_button.pack(pady=15)

forgot_password_label = Label(login_frame, text="Forgot Password?", fg="blue", font=("Arial", 12, "underline"), bg='#f0f0f0')
forgot_password_label.pack()
forgot_password_label.bind("<Button-1>", lambda e: open_forgot_password_link())

# Initial login frame pack
login_frame.pack()

# Register Frame
register_label = Label(register_frame, text="Register", font=("Arial", 40, "bold"), bg='#f0f0f0', fg='black')
register_label.pack(pady=(120, 0), anchor="center")

# Back button for Register Screen
back_button_register = Button(register_frame, command=login_screen, bg='#f0f0f0', bd=0)
back_icon_register = Image.open("C:\\Users\\Aditya\\OneDrive\\Desktop\\pngtree-vector-back-icon-png-image_931209.jpg")
back_icon_register = back_icon_register.resize((25, 25), Image.LANCZOS)
back_photo_register = ImageTk.PhotoImage(back_icon_register)
back_button_register.config(image=back_photo_register)
back_button_register.image = back_photo_register
back_button_register.place(relx=0.02, rely=0.02)  # Adjusted position

# Rest of the code remains the same

register_username_label = Label(register_frame, text="Username:", bg='#f0f0f0', fg='black')
register_username_label.pack()

register_username = Entry(register_frame)
register_username.pack()

register_password_label = Label(register_frame, text="Password:", bg='#f0f0f0', fg='black')
register_password_label.pack()

register_password = Entry(register_frame, show="*")
register_password.pack()

register_age_label = Label(register_frame, text="Age:", bg='#f0f0f0', fg='black')
register_age_label.pack()

register_age = Entry(register_frame)
register_age.pack()

register_email_label = Label(register_frame, text="Email:", bg='#f0f0f0', fg='black')
register_email_label.pack()

register_email = Entry(register_frame)
register_email.pack()

register_phone_label = Label(register_frame, text="Phone Number:", bg='#f0f0f0', fg='black')
register_phone_label.pack()

register_phone = Entry(register_frame)
register_phone.pack()   

register_button = Button(register_frame, text="Confirm Registration", command=register, bg='black', fg='white', font=("Arial", 14))
register_button.pack(pady=15)

# Button to switch between Login and Register
login_register_button = Button(root, text="Register", command=register_screen, bg='black', fg='white', font=("Arial", 14))
login_register_button.place(relx=0.8, rely=0.02)  # Adjusted position and size

# Main loop
root.mainloop()

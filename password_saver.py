import random
import tkinter
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    letterss = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "|", "{", "}",
               "[", "]", ":", ";", "''", ">", "<", ",", ".", "?", "/", "\\", "~", "`", ]
    pass_input.insert(random.randint(0, 10), random.randint(100, 999))
    pass_input.insert(random.randint(0, 10), random.choice(letterss))
    pass_input.insert(random.randint(0, 10), random.choice(letterss))
    pass_input.insert(random.randint(0, 10), random.choice(letters))
    pass_input.insert(random.randint(0, 10), random.choice(letterss))
    pass_input.insert(random.randint(0, 10), random.choice(letters))
    pass_input.insert(random.randint(0, 10), random.choice(symbols))
    pass_input.insert(random.randint(0, 10), random.choice(symbols))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def savepassword():
    if len(pass_input.get()) == 0 or len(email_input.get()) == 0 or len(web_input.get()) == 0:
        messagebox.showinfo("WARNING!", "can't leave a field blank!")

    else:
        listof_data = []
        result1 = web_input.get()
        result2 = email_input.get()
        result3 = pass_input.get()
        listof_data.append(result1)
        listof_data.append(result2)
        listof_data.append(result3)
        # print(listof_data)

        with open("passworddata.txt", "a") as fil:
            fil.write(" | ".join(listof_data))
            fil.write("\n")

        messagebox.showinfo("Success", "login successful. Data saved!")
        web_input.delete(0, 'end')
        pass_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Generator/Saver")
window.config(padx=100, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 105, image=lock_img)
canvas.grid(row=0, column=1)
website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password: ", padx=0, pady=0)
password_label.grid(row=3, column=0)

web_input = tkinter.Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "maitreyeeh@email.com")
pass_input = tkinter.Entry(width=21)
pass_input.grid(row=3, column=1)

button_pass = tkinter.Button(text="Generate Password", padx=0, pady=0, command=generate_password)
button_pass.grid(row=3, column=2)
add_but = tkinter.Button(text="Add", width=36, command=savepassword)
add_but.grid(row=4, column=1, columnspan=2)
window.mainloop()

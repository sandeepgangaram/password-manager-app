from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password = random_letters + random_numbers + random_symbols
    random.shuffle(password)
    password_output = ''.join(password)

    password_input.delete(0, END)
    password_input.insert(0, password_output)

    pyperclip.copy(password_output)
    messagebox.showinfo(title="Copied!", message="Password copied to clipboard!")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_inputs():
    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


def save_details():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields!", message="Do not leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title="confirm Save", message=f"""Credentials for Website:{website}\n
    Email: {username}\n
    Password: {password}\n
    Press OK to confirm or Cancel to edit.""")

    if is_ok:
        save_data = f"{website} | {username} | {password}\n"

        with open('data.txt', mode='a') as file:
            file.write(save_data)

        clear_inputs()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(height=200, width=200, pady=50, padx=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)


# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_details)

# Inputs
website_input = Entry()
email_input = Entry()
password_input = Entry()

website_input.focus()
# Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2, sticky='EW')
username_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2, sticky='EW')
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky='EW')
generate_button.grid(row=3, column=2, sticky='EW')
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
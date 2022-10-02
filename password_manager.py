from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    website = website_input.get().title().strip()

    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops! Error", message="No data file found. Go ahead and save your passwords.")
    else:
        if website in data:
            credentials = data[website]
            messagebox.showinfo(title=f"{website}",
                                message=f"Email:{credentials['email']}\nPassword:{credentials['password']}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"No details found for {website}")

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
# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_inputs():
    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


def save_details():
    website = website_input.get().title().strip()
    username = email_input.get().strip()
    password = password_input.get().strip()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields!", message="Do not leave any fields empty!")
        return
    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass
    else:
        if website in data:
            overwrite = messagebox.askokcancel(title="Duplicate data",
                                               message=f"Details for {website} already exist. Want to overwrite?")
            if not overwrite:
                return

    is_ok = messagebox.askokcancel(title="confirm Save", message=f"""Credentials for Website:{website}\n
    Email: {username}\n
    Password: {password}\n
    Press OK to confirm or Cancel to edit.""")

    if not is_ok:
        return

    save_data = {
        website: {
            "email": username,
            "password": password
            }
        }
    try:
        with open('data.json', mode='r') as file:
            # read data
            data = json.load(file)
            data.update(save_data)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('data.json', mode='w') as file:
            json.dump(save_data, file, indent=4)
    else:
        with open('data.json', mode='w') as file:
            json.dump(data, file, indent=4)
    finally:
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
search_button = Button(text="Search", command=search_password)

# Inputs
website_input = Entry()
email_input = Entry()
password_input = Entry()

website_input.focus()
# Layout
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, sticky='EW')
search_button.grid(row=1, column=2, sticky='EW')
username_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2, sticky='EW')
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky='EW')
generate_button.grid(row=3, column=2, sticky='EW')
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()

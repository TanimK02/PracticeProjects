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

    nr_letters = random.randint(7, 9)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    letter = [letter for letter in random.choices(letters, k=nr_letters)]
    number = [number for number in random.choices(numbers, k=nr_numbers)]
    symbol = [symbol for symbol in random.choices(symbols, k=nr_symbols)]

    password = letter + number + symbol

    random.shuffle(password)
    final = "".join(password)
    password_entry.insert(0, final)
    pyperclip.copy(final)
    messagebox.showinfo(message='Password saved to clipboard')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pass():
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n User/Email: {user}"
                                                              f" \n Password: {password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website} | {user} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:", font=('Arial', 14), fg='black', bg='white')
website_entry = Entry(width=35, bg='white', fg='black', highlightthickness=0.1, borderwidth=0.5)
website_entry.grid(column=1, row=1, columnspan=2)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", font=('Arial', 14), fg='black', bg='white')
username_entry = Entry(width=35, bg='white', fg='black', highlightthickness=0.1, borderwidth=0.5)
username_entry.grid(column=1, row=2, columnspan=2)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=('Arial', 14), fg='black', bg='white')
password_entry = Entry(width=21, bg='white', fg='black', highlightthickness=0.1, borderwidth=0.5)
password_entry.grid(column=1, row=3)
password_label.grid(column=0, row=3)
gen_pass = Button(width=10, border=0, highlightbackground='white', borderwidth=0, highlightthickness=0.5,
                  text='Generate Password', command=generate_password)
gen_pass.grid(column=2, row=3)
add_button = Button(width=36, border=0, highlightbackground='white', highlightthickness=0.5, borderwidth=0, text='add',
                    command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

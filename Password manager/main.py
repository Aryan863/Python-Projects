from tkinter import *           # '*' only imports all the classes, constants , etc. it does not import additional tkinter modules
from tkinter import messagebox  # 'messagebox' is a tkinter module. hence needs to be imported additionally
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_entry.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
   


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername/Email:  {username}\nPassword:  {password}\nIs it ok to save ?")

        if is_ok:
            pyperclip.copy(password)
            with open("./Password manager/data.txt", mode='a') as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, 'end')
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_logo = PhotoImage(file="./Password manager/logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_label.config(pady=4)

website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()



username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_label.config(pady=4)

username_entry = Entry(width=51)
username_entry.grid(row=2, column=1, columnspan=2)



password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_label.config(pady=4)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)
#generate_pass_button.config(padx=5)

add_button = Button(text="Add", width=43, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
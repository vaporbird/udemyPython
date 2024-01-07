from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
	
	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
	
	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)
	
	password = "".join(password_list)
	password_entry.insert(0, password)
	
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	
	if len(website) == 0 or len(password) == 0:
	    messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
		                                              f"\nPassword: {password} \nIs it ok to save?")
	if is_ok:
		while True:
			try:
				with open("data.json", "r") as data_file:
					data = json.load(data_file)

				new_data = {website : {"email" : email, "password" : password}}
				data.update(new_data)

				with open("data.json", "w") as data_file:
					json.dump(data, data_file, indent = 4)

			except FileNotFoundError:
				with open("data.json", "w") as data_file:
					pass

			except json.decoder.JSONDecodeError:
					data = {}
					new_data = {website : {"email" : email, "password" : password}}
					data.update(new_data)
					with open("data.json", "a") as data_file:
						json.dump(data, data_file, indent = 4)
					break

			else:
				break
			


		website_entry.delete(0, END)
		password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
	try:
		with open("data.json", "r") as pass_file:
			passwords = json.load(pass_file)
	except FileNotFoundError:
	    messagebox.showinfo(title="Sorry!", message="You haven't saved any passwords yet.")
	    return
	
	website = website_entry.get()
	password_entry.delete(0, END)
	email_entry.delete(0, END)

	if website in passwords:
		password_entry.insert(0, passwords[website]["password"])
		email_entry.insert(0, passwords[website]["email"])
	else:
		messagebox.showinfo(title="Sorry!", message="No password saved for this website.")
		email_entry.insert(0, "example@mail.com")
		
		
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@mail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text="Search", command=search_password)
add_button.grid(row=1, column=2, columnspan=1)

window.mainloop()

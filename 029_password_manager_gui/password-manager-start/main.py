import tkinter as tk
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def gen_pass():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
	
	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)
	
	password_list = []
	
	for char in range(nr_letters):
		password_list.append(random.choice(letters))
	
	for char in range(nr_symbols):
		password_list += random.choice(symbols)
	
	for char in range(nr_numbers):
		password_list += random.choice(numbers)
	
	random.shuffle(password_list)
	
	password = ""
	for char in password_list:
		password += char
	
	pass_entry.delete(0, tk.END)
	pass_entry.insert(0, password)

	
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password ():
	file = open("./data.txt", "r")
	all_passwords = file.readlines()
	file.close()

	new_pass = (f"{web_entry.get()} | {usr_entry.get()} | {pass_entry.get()}\n")
	if new_pass not in all_passwords:
		messagebox.showinfo(title = "Success", message = "Password saved!")
		file = open("./data.txt", "a")
		file.write(new_pass)
		file.close()
		web_entry.delete(0,tk.END)
		pass_entry.delete(0,tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)
window.minsize(200,200)

canvas = tk.Canvas(height = 200, width = 200)
pic = tk.PhotoImage(file = "./logo.png")
logo = canvas.create_image(100, 100, image = pic)
canvas.grid(column = 1, row = 0)

website = tk.Label(text = "Website:")
website.grid(column = 0, row = 1)

username = tk.Label(text = "Email/Username:")
username.grid(column = 0, row = 2)

password = tk.Label(text = "Password")
password.grid(column = 0, row = 3)

web_entry = tk.Entry(width = 35)
web_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "w")
web_entry.focus()

usr_entry = tk.Entry(width = 35)
usr_entry.grid(column = 1, row = 2, columnspan = 2, sticky ="w")
usr_entry.insert(0,"example@mail.com")

pass_entry = tk.Entry(width = 21)
pass_entry.grid(column = 1, row = 3, sticky = "w")

gen_pass = tk.Button(width = 14, text="Generate Password", command = gen_pass)
gen_pass.grid(column = 2, row = 3, sticky = "w")

add = tk.Button(text = "Add", width = 32, command = save_password)
add.grid(column = 1, row = 4, columnspan = 2, sticky = "w")

window.mainloop()

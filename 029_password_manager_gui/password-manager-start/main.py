import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- SAVE PASSWORD ------------------------------- #

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

usr_entry = tk.Entry(width = 35)
usr_entry.grid(column = 1, row = 2, columnspan = 2, sticky ="w")

passr_entry = tk.Entry(width = 21)
passr_entry.grid(column = 1, row = 3, sticky = "w")

gen_pass = tk.Button(width = 14, text="Generate Password")
gen_pass.grid(column = 2, row = 3, sticky = "w")

add = tk.Button(text = "Add", width = 32)
add.grid(column = 1, row = 4, columnspan = 2, sticky = "w")

window.mainloop()

import requests
import tkinter as tk

def gen_quote():
	req = requests.get("https://api.kanye.rest")
	quote = req.json()["quote"]
	cv.itemconfig(quote_text, text = quote)


win = tk.Tk()
win.minsize(300,500)
win.title("Kanye Quote Generator")
win.config(padx=50, pady=50)

cv = tk.Canvas(win, width = 300, height = 420)
bg_img = tk.PhotoImage(file = "./background.png")
bg = cv.create_image(150, 200, image = bg_img, anchor = tk.CENTER)
quote_text = cv.create_text(150, 200, text="Some Text", width=180, font=("Times New Roman", 20, "bold"), fill="darkred")

button_img = tk.PhotoImage(file = "./kanye.png")
button = tk.Button(win, image = button_img, command = gen_quote)

cv.grid(row = 0, column = 1)
button.grid(row = 1, column = 1)
tk.mainloop()


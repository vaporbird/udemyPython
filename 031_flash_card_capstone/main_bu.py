BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Times New Roman", 28)
WORD_FONT = ("Times New Roman", 36, "bold")
LANG = "French"

import tkinter as tk
import pandas as pd
import random as rand
from PIL import Image, ImageTk

#-------------------- LOGIC ------------------------------
class Logic():
	def __init__(self, card):
		self.card = card
		self.flip = None
		with open ("./data/french_words.csv") as data:
			df = pd.read_csv(data)
		self.words = df.to_dict(orient = "records")
		self.curr_word = self.update_card()

	def gen_word(self):
		rand_word = rand.choice(self.words)
		l = rand_word[LANG]
		en = rand_word["English"]
	
		return(l, en)
	
	def update_card(self):
		self.curr_word = self.gen_word()
		self.card.itemconfigure(word, text = self.curr_word[0])
		self.card.itemconfigure(lang, text = LANG)
		self.card.itemconfigure(card_side, image = front_card_img)
		window.cancel(self.flip)
		self.flip = window.after(3000, self.flip_card)
		
	
	def flip_card(self):
		self.card.itemconfigure(lang, text = "English")
		self.card.itemconfigure(word, text = self.curr_word[1])
		self.card.itemconfigure(card_side, image = back_card_img)
	
#------------------------ UI ------------------------
#Window
window = tk.Tk()
window.config(bg = BACKGROUND_COLOR)
window.title("Flash Card Capstone")
window.minsize(900,750)

#Card
card_text = "Placeholder"
card = tk.Canvas(window, width = 900, height = 600, bg = BACKGROUND_COLOR, highlightthickness = 0)
front_card_img = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
back_card_img = ImageTk.PhotoImage(Image.open("./images/card_back.png"))
card_side = card.create_image(450, 300, image = front_card_img)
lang = card.create_text(450, 100, font = LANG_FONT, text = LANG, justify = tk.CENTER)
word = card.create_text(450, 281, font = WORD_FONT, text = card_text, justify = tk.CENTER)

logic = Logic(card)
#Buttons
img_right = tk.PhotoImage(file = "./images/right.png")
right = tk.Button(image = img_right, highlightthickness = 0, command = logic.update_card)
img_wrong = tk.PhotoImage(file = "./images/wrong.png")
wrong = tk.Button(image = img_wrong, highlightthickness = 0, command = logic.update_card)

#Positions
card.grid(row = 0, column = 0, columnspan = 2)
right.grid(row = 1, column = 0)
wrong.grid(row = 1, column = 1)

#logic.update_card()
window.mainloop()

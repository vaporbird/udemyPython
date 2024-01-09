BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Times New Roman", 28)
WORD_FONT = ("Times New Roman", 36, "bold")
LANG = "French"

import tkinter as tk
from tkinter import messagebox as mb
import pandas as pd
import random as rand
from os.path import exists as exists
from PIL import Image, ImageTk
import csv

#-------------------- LOGIC ------------------------------
class Logic():
	def __init__(self):
		self.flip = None
		if not exists("./data/french_words_to_learn.csv"):
			self.reset_data()

		self.gen_words()
		self.update_card()

	def known(self):
		#apparently there is remove method words.remove(), which I forgot about
		self.words = [word for word in self.words if word[LANG] != self.curr_word[0]]
		
		try:
			keys = self.words[0].keys()
		except IndexError:
			self.reset_data()
			keys = self.words[0].keys()
			mb.showinfo(title = "Congratulations", message = "You know all words!\nAutomatically reseting the list :)")
		with open("./data/french_words_to_learn.csv", "w") as output_file:
			#also here there is a panda method to_csv
			#data = pandas.DataFrame(self.words)
			#data.to_csv("french_words_to_learn.csv")
			#but I forgot aswell

    			dict_writer = csv.DictWriter(output_file, keys)
    			dict_writer.writeheader()
    			dict_writer.writerows(self.words)
		
		self.update_card()

	def unknown(self):
		self.update_card()

	def gen_word(self):
		rand_word = rand.choice(self.words)
		l = rand_word[LANG]
		en = rand_word["English"]
	
		return(l, en)
	
	def update_card(self):
		self.curr_word = self.gen_word()
		card.itemconfigure(word, text = self.curr_word[0], fill = "black")
		card.itemconfigure(lang, text = LANG, fill = "black")
		card.itemconfigure(card_side, image = front_card_img)
		try:
			window.after_cancel(self.flip)
		except ValueError:
			pass
		self.flip = window.after(3000, self.flip_card)
		
	
	def flip_card(self):
		card.itemconfigure(lang, text = "English", fill = "darkred")
		card.itemconfigure(word, text = self.curr_word[1], fill = "darkred")
		card.itemconfigure(card_side, image = back_card_img)

	def reset_data(self):
		with open ("./data/french_words.csv") as data:
			with open ("./data/french_words_to_learn.csv", "w") as new_data:
				old_data = data.readlines()
				new_data.write("".join(old_data))
		self.gen_words()
	
	def gen_words(self):
		with open ("./data/french_words_to_learn.csv", "r") as data:
			df = pd.read_csv(data)
		self.words = df.to_dict(orient = "records")


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

logic = Logic()
#Buttons
img_right = tk.PhotoImage(file = "./images/right.png")
right = tk.Button(image = img_right, highlightthickness = 0, command = logic.known)
img_wrong = tk.PhotoImage(file = "./images/wrong.png")
wrong = tk.Button(image = img_wrong, highlightthickness = 0, command = logic.unknown)

#Positions
card.grid(row = 0, column = 0, columnspan = 2)
wrong.grid(row = 1, column = 0)
right.grid(row = 1, column = 1)

#logic.update_card()
window.mainloop()

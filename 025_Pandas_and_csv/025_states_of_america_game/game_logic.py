import pandas
from turtle import Turtle, TK

FONT = ("Arial", 12)
ALIGN = "center"

class Guesser(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.color("red")
		self.penup()
		self.data = pandas.read_csv("50_states.csv").to_dict(orient = "records")
	
	def guess(self, guess):
		guess = " ".join(w.capitalize() for w in guess.split(" "))
		#print(type(w.capitalize() for w in guess.split(" ")))
		for count, dict_ in enumerate(self.data):
			if dict_["state"] != guess:
				continue

			self.goto(dict_["x"], dict_["y"])
			self.write(dict_["state"], False, align = "center", font = ("Arial", 12))
			self.data.pop(count)
			return True
		return False

	def is_game_over(self):
		return len(self.data) == 0
	
	
	def guessed(self):
		return 50 - len(self.data)

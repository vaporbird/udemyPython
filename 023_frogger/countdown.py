from turtle import Turtle
import time
FONT = ("Courier", 28, "bold")
ALIGN = "center"

class Countdown(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.goto(0,0)
		self.color("white")

	def display(self, text):
		self.clear()
		self.write(text, align = ALIGN, font = FONT)

from turtle import Turtle
from random import randint as rand
import math

class Food(Turtle):

	def __init__(self,s):
		self.s = s
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.color("orange")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		ww_squares = int(math.ceil(((self.s.window_width()/2) - 20)/20))
		wh_squares = int(math.ceil(((self.s.window_height()/2) - 20)/20))
		self.goto(x = rand(-1 * ww_squares ,ww_squares) * 20, y = rand(-1 * wh_squares, wh_squares) * 20)


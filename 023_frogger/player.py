from turtle import Turtle
from time import time

class Player (Turtle):
	def __init__(self, screen_size): # [0] = x [1] = y
		self.screen_size = screen_size
		super().__init__()
		self.shape("turtle")
		self.color("black")
		self.penup()
		self.setheading(90)
		self.reset()
		self.last_reset = time()

	def move_up(self):
		if time() > self.last_reset + 1.5:
			if self.screen_size[0]/2 - 20 > self.ycor():
				self.forward(10)
	def move_down(self):
		if time() > self.last_reset + 1.5:
			if -1 * self.screen_size[0]/2 + 20 < self.ycor():
				self.backward(10)
	def move_right(self):
		if time() > self.last_reset + 1.5:
			if self.screen_size[1]/2 - 20 > self.xcor():
				self.goto(x = self.xcor() + 10, y = self.ycor())
	def move_left(self):
		if time() > self.last_reset + 1.5:
			if -1 * self.screen_size[1]/2 + 20 < self.xcor():
				self.goto(x = self.xcor() - 10, y = self.ycor())
	def reset(self):
		self.goto(x = 0, y = (-1 * self.screen_size[1]/2) + 20)
		self.last_reset = time()

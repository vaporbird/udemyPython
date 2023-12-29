from turtle import Turtle
from random import randint as rand

class Car(Turtle):
	def __init__(self, screen_size):
		self.screen_size = screen_size
		self.stretch_factor = (rand(5,20)/10, rand(20,60)/10)
		self.movespeed = rand(4,20)
		super().__init__("square")
		self.penup()
		self.color((rand(0,255)/255, rand(0,255)/255, rand(0,255)/255,))
		self.goto(((rand(-1 * self.screen_size[0]/2 + 60, self.screen_size[0]/2 - 60)), rand(-1 * self.screen_size[0]/2 + 60, self.screen_size[0]/2 - 60)))
		self.shapesize(stretch_wid = self.stretch_factor[0], stretch_len = self.stretch_factor[1])
	
	def move(self, multiplier):
		self.forward(self.movespeed * multiplier)
		if self.xcor() > self.screen_size[1]/2 + 10* self.stretch_factor[1]:
			self.setx(-1 * self.screen_size[1]/2 - 2 * 10 * self.stretch_factor[1])

from turtle import Turtle
from random import randint as rand
import math
from functions import upd_scr

class Ball(Turtle):

	def __init__(self,s):
		self.s = s
		super().__init__()
		self.shape("circle")
		#self.penup()
		self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		self.penup()
		self.home()
		self.pendown()
		self.color((rand(0,255)/255, rand(0,255) / 255, rand(0,255) / 255))
		self.setheading(rand(0,360))
		while(self.heading() % 180 > 60 and self.heading() % 180 < 120):
			self.setheading(rand(0,360))
		upd_scr(self.s)

	def move(self):
		self.forward(4)
		upd_scr(self.s)

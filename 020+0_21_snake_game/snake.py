from turtle import Turtle, Screen
from functions import upd_scr

class Snake():
	def __init__(self, screen):
		self.s = screen
		self.snake_body = []

		for i in range (3):
			t = Turtle()
			self.snake_body.append(t)
			t.color("white")
			t.shape("square")
			t.penup()
			t.setx(i*-20)
			t.sety(0)
			t.speed(1)
		upd_scr(self.s)

		self.head = self.snake_body[0]
		self.tail = self.snake_body[len(self.snake_body) - 1]

	def automove(self):
		for i in range (len(self.snake_body) - 1, 0, -1):
			self.snake_body[i].goto(self.snake_body[i-1].pos())
		self.snake_body[0].forward(20)
		upd_scr(self.s)

	def up(self):
		if self.snake_body[0].heading() == 0 or self.snake_body[0].heading() == 180:
			self.snake_body[0].setheading(90)

	def down(self):
		if self.snake_body[0].heading() == 0 or self.snake_body[0].heading() == 180:
			self.snake_body[0].setheading(270)

	def left(self):
		if self.snake_body[0].heading() == 90 or self.snake_body[0].heading() == 270:
			self.snake_body[0].setheading(180)

	def right(self):
		if self.snake_body[0].heading() == 90 or self.snake_body[0].heading() == 270:
			self.snake_body[0].setheading(0)


	

from turtle import Turtle
from config import *
from functions import upd_scr, upd_scr_nowait # upd_scr_nowait can be removed for performance from everywhere

class Platforms():
	def __init__(self, s):
		self.s = s
		self.p1_body = []
		self.p2_body = []
		for i in range(5):
			for item in [self.p1_body, self.p2_body]:
				t = Turtle("square")
				t.color("white")
				t.setheading(90)
				t.penup()
				t.goto(x = (SCREEN_WIDTH/2 - 40) if item == self.p1_body else -1* (SCREEN_WIDTH/2 - 40), y = -2 * PLATFORM_SECTOR_SIZE + i* PLATFORM_SECTOR_SIZE)
				item.append(t)

	def p1_move_up(self):
		if self.p1_body[len(self.p1_body) - 1].ycor() < (SCREEN_HEIGHT/2) - 15:
			for sector in self.p1_body:
				sector.forward(20)
			upd_scr_nowait(self.s)	
	
	def p1_move_down(self):
		if self.p1_body[0].ycor() > (-1 * SCREEN_HEIGHT/2) + 15:
			for sector in self.p1_body:
				sector.backward(20)
			upd_scr_nowait(self.s)

	def p2_move_up(self):
		if self.p2_body[len(self.p2_body) - 1].ycor() < (SCREEN_HEIGHT/2) - 15:
			for sector in self.p2_body:
				sector.forward(20)
			upd_scr_nowait(self.s)	
	
	def p2_move_down(self):
		if self.p2_body[0].ycor() > (-1 * SCREEN_HEIGHT/2) + 15:
			for sector in self.p2_body:
				sector.backward(20)
			upd_scr_nowait(self.s)

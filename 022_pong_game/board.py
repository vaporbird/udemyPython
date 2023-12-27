from turtle import Turtle, Screen
from config import *
FONT = ("Courier", 28, "bold")
ALIGN = "center"
class Board():
	round_going = False
	def __init__(self, screen):	
		self.screen = screen
		self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
		self.screen.bgcolor("gray")
		self.painter = Turtle()
		self.painter.penup()
		self.painter.color("white")
		self.painter.hideturtle()
		self.painter.sety(SCREEN_HEIGHT/2)
		self.painter.setheading(270)
		
		self.writer = Turtle()
		self.writer.color("white")
		self.writer.hideturtle()
		self.writer.penup()

		dotted_line_width = 10
		self.painter.forward(dotted_line_width/2)
		for i in range (int(SCREEN_HEIGHT/(dotted_line_width*2)) - 1):
			self.painter.penup()
			self.painter.fd(dotted_line_width)
			self.painter.pendown()
			self.painter.fd(dotted_line_width)
		
		self.painter.penup()
	
	def write_scores(self):
		self.writer.clear()
		self.writer.goto(x = -40, y = SCREEN_HEIGHT/2 - 60)
		self.writer.write(self.score_l, align = ALIGN, font = FONT)
		self.writer.goto(x = 40, y = SCREEN_HEIGHT/2 - 60)
		self.writer.write(self.score_r, align = ALIGN, font = FONT)
		
	def init_score(self):
		#init the player scores
		self.score_r = 0
		self.score_l = 0
		self.write_scores()
		
	def p1_score_inc(self):
		self.score_l += 1
		self.write_scores()
	
	def p2_score_inc(self):
		self.score_r += 1
		self.write_scores()
	
	def start_round(self):
		if not self.round_going:
			self.round_going = True
			print("Round is starting")

	def end_round(self):
		self.round_going = False

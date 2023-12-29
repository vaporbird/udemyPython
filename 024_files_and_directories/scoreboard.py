from turtle import Turtle
import os

class Scoreboard(Turtle):
	def __init__(self, s, score):
		super().__init__()
		self.s = s
		self.score = score
		self.color("magenta")
		self.penup()
		self.hideturtle()
		ww = -1 * (self.s.window_width()/2 - 20)
		wh = self.s.window_height()/2 - 40
		self.goto(x= ww, y= wh)

		#You either swap the if and with and use append mode(doesn't work with write) or you do it this way, but you need to have the file created. Its again some kind of handle interaction
		if os.stat("highscore.txt").st_size == 0:
			with open ("./highscore.txt", mode = "w") as hs:
				 hs.write("0")
		
		# I guess its a handle so I have to reopen it to refresh contents, doesn't work otherway
		with open ("./highscore.txt", mode = "r") as hs:
			self.highscore = int(hs.read())
			print(self.highscore)

		#The above ~10 lines of code took me 1 hour of debugging

		self.write(f"Score : {self.score} Highscore : {self.highscore}", False, align = "left", font = ("Arial", 12))

	def update(self):
		self.score += 1
		self.clear()
		self.write(f"Score : {self.score} Highscore : {self.highscore}", False, align = "left", font = ("Arial", 12))

	def game_over(self):
		over = Turtle()
		over.hideturtle()
		over.color("white")
		self.write(f"Score : {self.score} Highscore : {self.highscore}", False, align = "left", font = ("Arial", 12))
	
		if self.score > int(self.highscore):
			with open("./highscore.txt", mode = "w") as hs:
				hs.write(str(self.score))

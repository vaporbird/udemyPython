from turtle import Turtle

class Scoreboard(Turtle):
	def __init__(self, s, score):
		super().__init__()
		self.s = s
		self.score = score
		self.color("magenta")
		self.penup()
		self.hideturtle()
		ww = -1 * (self.s.window_width()/2 - 40)
		wh = self.s.window_height()/2 - 40
		self.goto(x= ww, y= wh)
		self.write(f"Score : {self.score}", False, align = "center", font = ("Arial", 12))
	def update(self):
		self.score += 1
		self.clear()
		self.write(f"Score : {self.score}", False, align = "center", font = ("Arial", 12))
	def game_over(self):
		over = Turtle()
		over.hideturtle()
		over.color("white")
		over.write("Game Over !", False, align = "center", font = ("Courier", 24, "bold"))

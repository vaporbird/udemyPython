from turtle import Turtle

class Scoreboard(Turtle):
	def __init__(self, s, score):
		super().__init__()
		self.s = s
		self.score = score
		self.text = Turtle()
		self.text.color("cyan")
		self.text.penup()
		self.text.hideturtle()
		ww = -1 * (self.s.window_width()/2 - 40)
		wh = self.s.window_height()/2 - 40
		self.text.goto(x= ww, y= wh)
		self.text.write(f"Score : {self.score}", False, align = "center", font = ("Arial", 12))
	def update(self):
		self.score += 1
		self.text.clear()
		self.text.write(f"Score : {self.score}", False, align = "center", font = ("Arial", 12))

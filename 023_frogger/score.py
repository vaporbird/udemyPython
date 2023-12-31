from turtle import Turtle

FONT = ("Times New Roman", 14, "bold")
ALIGN = "left"

class Text(Turtle):
	def __init__(self, screen_size):
		self.level = 1
		self.screen_size = screen_size
		super().__init__()
		self.hideturtle()
		self.color("white")
		self.goto(- 1 * screen_size[0]/2 + 20, 1 * screen_size[1]/2 - 40)
		self.display_level(self.level)

	def display_level(self, level):
		self.clear()
		self.level = level
		self.write(f"Level: {self.level}", align = ALIGN, font = FONT)

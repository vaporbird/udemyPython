from turtle import Turtle, Screen, TK
from random import randint

colors = ["red","orange","yellow","green","blue","navy","violet"]
s = Screen()
s.setup(width = 900, height = len(colors) * 75 + 150)
s.bgcolor("lightgray")

prediction = s.textinput(title = "Pick a winner!", prompt = "Select your winner (red/orange/yellow/green/blue/navy/violet)").strip().lower()
while prediction not in colors:
	prediction = s.textinput(title = "Pick a winner!", prompt = "Please enter a valid input (red/orange/yellow/green/blue/navy/violet)").strip().lower()
	
turtles = {}

def setup():
	i = 1
	for color in colors:
		t = Turtle(shape = "turtle")
		t.color(color)
		turtles[color] = t
		t.penup()
		t.goto(-1 * (s.window_width()/2 - 20), (-1 * s.window_height()/2 + 20) + i * 75)
		i+=1
setup()
is_over = False
while(not is_over):
	for color in colors:
		t = turtles[color]
		t.forward(randint(-1,10)) # -1 because it is funny
		if t.xcor() >= s.window_width()/2 - 10:
			is_over = True
winner = turtles[colors[0]]			
for color in colors:
	t = turtles[color]
	if t.xcor() > winner.xcor():
		winner = t
print(winner.color()[0])
if (winner.color()[0] == prediction):
	TK.messagebox.showinfo(title="Well Done!", message= f"Congradulations, you guessed correctly {winner.color()[0]}")
else:
	TK.messagebox.showinfo(title="Good try!", message= f"You picked wrong, the correct color was {winner.color()[0]}")

s.exitonclick()

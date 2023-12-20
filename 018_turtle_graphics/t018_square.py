from turtle import *

t = Turtle()
t.color("orange")
t.shape("turtle")
for _ in range(4):
	t.forward(100)
	t.right(90)

screen = Screen()
screen.exitonclick() 


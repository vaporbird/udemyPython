from turtle import *
from random import randint as rand
s = Screen()
t = Turtle()

colors = ["red", "green", "blue", "brown", "black", "purple", "pink", "orange"]

t.width(10)
for _ in range(1000):
	t.color(colors[rand(0,len(colors) - 1)])
	t.fd(10)
	t.left(rand(-1,1)*90)
	
s.exitonclick()

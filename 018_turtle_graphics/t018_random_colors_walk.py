from turtle import *
from random import randint as rand, random
s = Screen()
t = Turtle()

t.width(10)
for _ in range(1000):
	t.color((random(), random(), random()))
	t.fd(10)
	t.left(rand(-1,1)*90)
	
s.exitonclick()

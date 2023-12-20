from turtle import *
s = Screen()
t = Turtle()
t.speed("fastest")
for _ in range (int(360/2)):
	t.circle(100)
	t.left(2)
s.exitonclick()

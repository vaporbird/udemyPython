from turtle import Turtle, Screen
s = Screen()
t = Turtle()

t.color("red")
t.shape("turtle")

for _ in range(50):
	t.fd(5)
	t.pu()
	t.fd(5)
	t.pd()

s.exitonclick()

from turtle import Turtle, Screen
t = Turtle()
s = Screen()

def move_forwards():
	t.fd(10)


s.listen()
s.onkey(key = "space", fun = move_forwards)
s.exitonclick()


from turtle import Turtle, Screen
t = Turtle()
s = Screen()



def move_fd():
	t.fd(8)
def move_bw():
	t.fd(-8)
def turn_lt():
	t.left(10)
def turn_rt():
	t.right(10)
def clear_scr():
	t.home()
	t.clear()

s.listen()
s.onkey(move_fd, "w")
s.onkey(move_bw, "s")
s.onkey(turn_lt, "a")
s.onkey(turn_rt, "d")
s.onkey(clear_scr, "c")
s.exitonclick()

from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_body = []
def setup():
	global snake_body 
	snake_body = []
	for i in range (3):
		t = Turtle()
		snake_body.append(t)
		t.color("white")
		t.shape("square")
		t.penup()
		t.setx(i*-20)
		t.sety(0)
		t.speed(1)
	screen.update()

setup()
def automove():
	for i in range(len(snake_body)):
		snake_body[i].forward(20)
	time.sleep(0.2)
	screen.update()
automove()
automove()
automove()
automove()
automove()
automove()
automove()
automove()
automove()
automove()
#while True:
#	automove()
#	screen.update()

screen.exitonclick()

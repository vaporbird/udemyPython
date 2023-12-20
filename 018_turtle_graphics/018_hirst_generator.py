#don't ask me how I came up with those algorithms, there is logic behind them, but I probably won't remember a hour from now
#everytime I play with graphics the code ends up unreadable :(
import colorgram
from turtle import *
colors = colorgram.extract("./hirst.jpg", 25)

t = Turtle()
s = Screen()
t.shape("turtle")

def go_to_start(t):
	t.penup()
	t.goto(
	(-1 + (1/len(colors) ** (1/2))) * (s.window_width()/2),
	(-1 + (1/len(colors) ** (1/2))) * ((s.window_height()/2) + s.window_width()/(3/4 * (4 * (len(colors) ** (1/2))))),
	)

def draw_circle(t):
	t.pendown()
	t.begin_fill()
	t.circle((s.window_width() if s.window_width() < s.window_height() else window_height())/(4 * (len(colors) ** (1/2))))
	t.end_fill()
	t.penup()

def move(t):
	t.setx(int(t.xcor() + 2*(1/len(colors) ** (1/2)) * (s.window_width()/2)))
	if t.xcor() >= ((s.window_width() / 2) - s.window_width()/(4 * (len(colors) ** (1/2)))) :
		t.goto((-1 + (1/len(colors) ** (1/2))) * (s.window_width()/2), t.ycor() + 2 * (1/len(colors) ** (1/2)) * (s.window_height()/2))


go_to_start(t)
for i in range(len(colors)):
	color = (colors[i].rgb.r/255, colors[i].rgb.g/255, colors[i].rgb.b/255)
	t.color(color)
	t.fillcolor(color)
	draw_circle(t)
	move(t)
t.hideturtle()



s.exitonclick()

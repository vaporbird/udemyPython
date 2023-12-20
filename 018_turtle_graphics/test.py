import setuptools
import turtle
turtle.color("green")
turtle.hideturtle()
turtle.speed(1)
turtle.left(90)

for i in range(4):
    turtle.forward(30)
    turtle.penup()
    turtle.forward(30)    
    turtle.pendown()

turtle.exitonclick()

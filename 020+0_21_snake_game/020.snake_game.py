import turtle
from turtle import Turtle,Screen
from snake import Snake, upd_scr
from functions import upd_scr
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(screen)
food = Food(screen)

screen.listen()
screen.onkeypress(snake.up,"w")
screen.onkeypress(snake.down,"s")
screen.onkeypress(snake.left,"a")
screen.onkeypress(snake.right,"d")

game_is_on = True
while game_is_on:
	snake.automove()

	#Detect collision with food
	if snake.head.distance(food) < 10:
		food.refresh()
		collision = True
		while collision:
			for part in snake.snake_body:
				if part.distance(food) == 0:
					food.refresh()
					break
			collision = False

screen.exitonclick()

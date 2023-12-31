import turtle
from turtle import Turtle, Screen, TK
from snake import Snake, upd_scr
from functions import upd_scr
from food import Food
from scoreboard import Scoreboard

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
score = 0
scoreboard = Scoreboard(screen, 0)
while game_is_on:
	snake.automove()

	#Detect collision with food
	if snake.head.distance(food) < 15:
		scoreboard.update()
		food.refresh()
		snake.expand()
		collision = True

		while collision:
			collision = False
			for part in snake.snake_body:
				if part.distance(food) < 15:
					collision = True
					food.refresh()
					break

	#Detect collision with wall
	if abs(snake.head.xcor()) >= screen.window_width()/2 or abs(snake.head.ycor()) >= screen.window_height()/2:
		print("You lost")
		#TK.messagebox.showinfo(title="Game Over!", message= f"You hit a wall!\nYour finals score is: {scoreboard.score}")
		scoreboard.game_over()
		game_is_on = False

	#Detect collision with body	
	for segment in snake.snake_body[1::]:
		if segment.distance(snake.head.pos()) < 15:
			print("You lost")
			#TK.messagebox.showinfo(title="Game Over!", message= f"You bit yourself!\nYour finals score is: {scoreboard.score}")
			scoreboard.game_over()
			game_is_on = False

screen.exitonclick()

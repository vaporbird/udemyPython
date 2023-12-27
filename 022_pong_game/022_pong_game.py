from turtle import Turtle, Screen, TK
from board import Board
from config import *
from platforms import Platforms
from functions import upd_scr
from ball import Ball
import time

s = Screen()
s.tracer(0)

#Init the board
board = Board(s)
board.init_score()

platforms = Platforms(s)
ball = Ball(s)

def start_game():
	last_hit_time = 0

	board.start_round()
	while (board.round_going):
		ball.move()
		ycor = ball.ycor()
		xcor = ball.xcor()
		heading = ball.heading()

		if abs(ycor) > (SCREEN_HEIGHT/2 - 10):
			ball.setheading(heading * - 1)
	
		for sector in (platforms.p1_body + platforms.p2_body):
			if ball.distance(sector) < 20:
				hit_end_time = time.time()
	
				if last_hit_time + 0.2 < time.time(): #0.2 sec I think is reasonable
					last_hit_time = time.time()
					if sector in platforms.p1_body:
						index = platforms.p1_body.index(sector)
						factor = 0.7 + 0.15 * index
					else:
						index = platforms.p2_body.index(sector)
						factor = 0.7 + 0.15 * index

					ball.setheading(int((heading * - 1 + 180) * factor))

		if abs(xcor) > SCREEN_WIDTH/2:
			if xcor < 0:
				board.p2_score_inc()			
			else:
				board.p1_score_inc()
			
			ball.refresh()
			board.end_round()

s.onkey(key = "Up", fun = platforms.p1_move_up)
s.onkey(key = "Down", fun = platforms.p1_move_down)
s.onkey(key = "w", fun = platforms.p2_move_up)
s.onkey(key = "s", fun = platforms.p2_move_down)
s.onkeypress(fun = start_game, key = "space")
s.listen()

upd_scr(s)

TK.messagebox.showinfo(title="Instructions!", message= f"Start the Round: Spacebar\nPlayer1: W & S\nPlayer2: Up & Down")
is_game_over = False

s.exitonclick()

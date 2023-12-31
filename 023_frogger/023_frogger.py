from turtle import Turtle, Screen, TK
from player import Player
from car import Car
from functions import upd_scr
from score import Text
from countdown import Countdown
from time import time

SCREEN_WIDTH = 610
SCREEN_HEIGHT = 610
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
cars = []
level = 1

s = Screen()
s.bgcolor("gray")
s.setup(height = SCREEN_HEIGHT ,width = SCREEN_WIDTH)
s.tracer(0)

p = Player(screen_size)
t = Text(screen_size)
cl = Countdown()

for _ in range(20):
	cars.append(Car(screen_size))

def keys_activate():
	s.onkey(p.move_up, "w")
	s.onkey(p.move_down, "s")
	s.onkey(p.move_left, "a")
	s.onkey(p.move_right, "d")
def keys_deactivate():
	s.onkey(None, "w")   
	s.onkey(None, "s") 
	s.onkey(None, "a") 
	s.onkey(None, "d") 

keys_activate()
s.listen()

is_game_over = False
new_round_timer_on = True
last_reset = time()
upd_scr(s)
while not is_game_over:
	if p.ycor() > SCREEN_HEIGHT/2 - 30:
		level += 1
		p.reset()
		t.display_level(level)
		keys_deactivate()
		last_reset = time()
		new_round_timer_on = True
	for car in cars:
		car.move(0.05* level)
		if abs(car.ycor() - p.ycor()) < 10 + 10 * car.stretch_factor[0] and abs(car.xcor() - p.xcor()) < 10 + 10 * car.stretch_factor[1]:
			is_game_over = True
			TK.messagebox.showinfo(title="Game Over!", message= "You got hit by a car!")

	upd_scr(s)
	
	if new_round_timer_on:
		if time() > last_reset + 1.5:
			new_round_timer_on = False
			keys_activate()
			cl.display("")
			continue
		if time() > last_reset + 1:
			cl.display("1")
			continue
		if time() > last_reset + 0.5:
			cl.display("2")
			continue
		cl.display("3")
	
s.exitonclick()

from turtle import Turtle, Screen, TK
import pandas
from game_logic import Guesser

s = Screen()
s.setup(725,491)
s.bgpic("./blank_states_img.gif")
g = Guesser()


is_game_over = False
prompt = "Guess a state"
counter = 0
while not is_game_over:
	
	guess = s.textinput(title = "Guess a state!", prompt = prompt)
	if (g.guess(guess)):
		counter = g.guessed()
		prompt = f"{counter}/50\nCorrect guess, try another state"
	else:
		prompt = f"{counter}/50\nIncorrect guess or already guessed, guess a state"
	is_game_over = g.is_game_over()

s.exitonclick()

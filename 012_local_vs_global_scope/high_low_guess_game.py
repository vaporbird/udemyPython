#Testing global and local scope
from random import randint as random
number = 0
difficulty = ""
lives = 0

def reset_game():
	global difficulty
	global number
	global lives
	number = random(1,100)
	difficulty = input("Choose a difficulty (hard/easy): ").strip().lower()
	while difficulty not in ["hard","easy"]:
		difficulty = input("Please enter a valid input (hard/easy): ").strip().lower()

	match difficulty:
		case 'hard':
			lives = 5
		case 'easy':
			lives = 10

def guess_number():
	global number
	global lives
	guess = ""
	while(lives > 0 and guess != number):
		while(True):
			try:
				guess = int(input("Choose a valid number : ").strip())
			except Exception:
				print("Invalid input")
				continue
			break

		if guess > number:
			lives -= 1
			print(f"Too high, remaining lives {lives} \n")
			continue

		elif guess < number:
			lives -= 1
			print(f"Too low, remaining lives {lives} \n")
			continue

		return "You win!"
	return f"You lose!, the number was {number}"

keep_going = True
while(keep_going):
	reset_game()
	print(f"Number of lives : {lives}")
	print(guess_number())
	do_we_cont = input("Do you want to play another game?(Y/n) : ").strip().lower()
	while do_we_cont not in ["y","n"]:
		do_we_cont = input("Please enter a valid input (Y/n) : ").strip().lower()
	if do_we_cont == 'n':
		keep_going = False

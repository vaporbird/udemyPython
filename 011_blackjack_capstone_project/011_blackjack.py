from random import randint as rand

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
values = {
"2":2,
"3":3,
"4":4,
"5":5,
"6":6,
"7":7,
"8":8,
"9":9,
"10":10,
"J":10,
"Q":10,
"K":10,
"A":11,
}

player_hand = []
cpu_hand = []
hand_is_over = False
play_again = True
def start_new_game():
	player_hand.clear()
	cpu_hand.clear()
	global hand_is_over
	hand_is_over = False

def generate_starting_hands():
	for i in range(2):
		card = cards[rand(0,len(cards) - 1)]
		player_hand.append(card)
	card = cards[rand(0,len(cards) - 1)]
	cpu_hand.append(card)
	print(f"CPU hand is {cpu_hand}")

def check_score(hand):
	aces_count = 0
	score = 0
	for card in hand:
		score += values[card]
		if card == "A":
			aces_count += 1
		while(score > 21 and aces_count > 0):
			aces_count -= 1
			score -= 10
	return score

def player_turn():
	print(f"\nYour hand is {player_hand}")
	print(f"Your score is {check_score(player_hand)} ")

	while(True):
		draw = input ("Do you want to draw another card (y/N): ").strip().lower()
		while draw not in ["y","n"]:
			draw = input ("Please enter a valid input (y/N): ")
		if draw == "n":
			break
	
		draw_card(player_hand)
		print(f"\nYour hand is {player_hand}")
		print(f"Your score is {check_score(player_hand)} ")	
		if check_score(player_hand) > 21:
			global hand_is_over
			hand_is_over = True
			break


def draw_card(hand):
	card = cards[rand(0,len(cards)-1)]
	hand.append(card)

def cpu_turn():
	draw_card(cpu_hand)
	score = check_score(cpu_hand)
	while(score < 17):
		draw_card(cpu_hand)
		score = check_score(cpu_hand)
	if score > 21:
		global hand_is_over
		hand_is_over = True
	print(f"\nThe CPU hand is : {cpu_hand} ")
	print(f"CPU score is : {score}")

def who_is_winner():
	winner = check_score(player_hand) - check_score(cpu_hand)
	if winner > 0:
		return 1
	if winner < 0:
		return -1
	return 0

def do_play_another():
	keep_going = input("\nDo you want to play again? (Y/n): ").strip().lower()
	while keep_going not in ["y","n"]:
		keep_going = ("Please enter a valid input! (Y/n): ")
	if keep_going =="n":
		print("Thank you for playing !")
		return False

	return True
	
while(play_again):
	start_new_game()
	
	generate_starting_hands()
	player_turn()
	if (hand_is_over):
		print("Player loses! ")
		play_again = do_play_another()
		continue
	cpu_turn()
	if (hand_is_over):
		print("Player wins!" )
		play_again = do_play_another()
		continue

	if who_is_winner() == 1:
		print ("Player Wins! ")
	elif who_is_winner() == -1:
		print("CPU wins! ")
	else:
		print("It's a Tie!" )
	play_again = do_play_another()

	#print(check_score(player_hand))
#print(player_hand)
#print(check_score(cpu_hand))
#print(cpu_hand)

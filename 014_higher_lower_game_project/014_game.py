from art import logo, vs
from game_data import data as game_data
from random import randint as rand
import os
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def select_person(used_index):
	current_index = rand(0, len(game_data) - 1) 
	while current_index in used_index:
		current_index = rand(0, len(game_data) - 1)
	return current_index

def is_choice_correct(choice, countA, countB, first_index, second_index):
	if choice == "A" and countA >= countB :
		print(f"You choose corectly with {game_data[first_index]['follower_count']} > {game_data[second_index]['follower_count']} ")
		return True
	elif choice == "B" and countB >= countA :
		print(f"You choose corectly with {game_data[second_index]['follower_count']} > {game_data[first_index]['follower_count']} ")
		return True	
	elif choice == "A":
		print(f"Unfortunately you choose wrong with {game_data[first_index]['follower_count']} > {game_data[second_index]['follower_count']} ")
		return False
	else:
		print(f"Unfortunately you choose wrong with {game_data[second_index]['follower_count']} > {game_data[first_index]['follower_count']} ")
		return False

def print_info(index):
#name,follower_count,descriotion,country
	print(f"{game_data[index]['name']}, A {game_data[index]['description']}, from {game_data[index]['country']}")

def play_game():
	is_game_over = False
	used_index = []
	first_index = -1
	while(not is_game_over):
		clear()
		print(len(used_index))
		print(len(game_data))
		if len(used_index) == len(game_data):
			print("You already exhausted the list of persons, therefore you win ! :) ")
			return

		print(logo)
		if (first_index == -1):
			first_index = select_person(used_index)
			used_index.append(first_index)
		print("Option A: ")
		print_info(first_index)

		print(vs)
		second_index = select_person(used_index)
		used_index.append(second_index)
		print("Option B: ")
		print_info(second_index)

		player_choose = input("A or B : ").strip().upper()
		while player_choose not in ["A", "B"] :
			player_choose = input("Please enter a valid input (A/B): ").strip().upper()


		correct = is_choice_correct(player_choose, game_data[first_index]["follower_count"], game_data[second_index]["follower_count"], first_index, second_index)
		if(correct):
			if game_data[second_index]["follower_count"] > game_data[first_index]["follower_count"]:
				first_index = second_index
			input("\nenter anything to continue")
			continue
		else:
			is_game_over = True
do_we_play = True
while(do_we_play):
	play_game()
	choice = input("Do you want to play again?(Y/n) : ").strip().upper()
	while choice not in ["Y","N"]:
		choice = input("Please enter a valid input?(Y/n) : ").strip().upper()
	if choice == "N":
		print("Thanks for playing :)")
		do_we_play = False

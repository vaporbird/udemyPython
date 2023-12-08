from random import randint as rand
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
used_letter_list = []
word_list = ["cow", "chicken", "hen", "bull"]
known_indexes = []

#could also use rand.choice() here
word = word_list[rand(0, len(word_list) -1)]

def guess_letter():
	letter = input("\nGuess a letter: ").strip().lower()
	while(True):
		if(letter not in letter_list):
			letter = input("Invalid input, please try again: ").strip().lower()
			continue

		if(letter in used_letter_list):
			letter = input("Already guessed letter, please try again: ").strip().lower()
			continue

		used_letter_list.append(letter)
		return letter

def get_indexes_of_letter_in_word(letter):
	index_list = []
	for i in range (len(word)):
		if letter == word[i]:
			index_list.append(i)
	return index_list

def print_known_indexes_in_word():
	print("Your word is : \n")
	string = ""
	for i in range (len(word)):
		if i in known_indexes:
			string += (word[i] + " ")
			continue
		string += ("_ ")
	print(string)

game_is_over = False
lives = 6
while (not game_is_over):
	print_known_indexes_in_word()
	if lives <= 0:
		print(f"You ran out of lives, GAME OVER!, the word was: {word}")
		game_is_over = True
		continue

	if len(known_indexes) == len(word):
		print("Congradulations, you guessed the word")
		game_is_over = True
		continue

	letter = guess_letter()
	new_indexes = get_indexes_of_letter_in_word(letter)
	if len(new_indexes) == 0:
		lives -= 1
		print("Unfortunately the word does not contain this letter")
		print(f"Remaining lives {lives}")
		continue
	
	for i in new_indexes:
		known_indexes.append(i)
		continue

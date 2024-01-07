
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

is_not_okay = True
while(is_not_okay):
	word = input("Enter a word: ").upper()
	try:
		output_list = [phonetic_dict[letter] for letter in word]
		print(output_list)
	except KeyError:
		print("Please enter a string of only characters")
	else:
		is_not_okay = False


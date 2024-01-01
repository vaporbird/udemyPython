import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}
keep_going = True
print("Enter Invalid input to exit")
while keep_going:
	try:
		user_msg = input("Enter a word to be transformed to nato code: ").strip().upper()
		print([nato_alphabet[code] for code in user_msg])
	except Exception:
		print("exiting ...")
		exit(0)

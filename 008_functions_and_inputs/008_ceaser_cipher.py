alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt (message, offset):
	encrypted_message = ""
	for letter in message:
		if letter not in alphabet:
			encrypted_message += letter
			continue

		new_letter = alphabet.index(letter) + offset
		if new_letter > len(alphabet) - 1:
			new_letter =  new_letter - len(alphabet)
		encrypted_message += alphabet[new_letter]
	print(encrypted_message)

def decrypt (message, offset):
	decrypted_message = ""
	for letter in message:
		if letter not in alphabet:
			decrypted_message += letter
			continue
	
		new_letter = alphabet.index(letter) - offset
		decrypted_message += alphabet[new_letter]
	print(decrypted_message)

message = input ("Please enter a message : \n").strip().lower()
offset = int (input ("Please enter a offset : \n").strip())%len(alphabet)
command = input ("Do you want to encrypt or decrypt ").strip().lower()
while not (command == "encrypt" or command == "decrypt"):
	command = input("Invalid input, please try again (encrypt/decrypt) : ")
exec(f"{command}(message,offset)")

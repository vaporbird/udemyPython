#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode = "r") as file:
	names = file.readlines()

with open("./Input/Letters/starting_letter.txt", mode = "r") as file:
	greeting = file.read()

for name in names:
	name = name.strip()
	personal_greeting = greeting.replace("[name]", name)

	with open(f"./Output/Personal_not_invitation_to_{name}.txt", mode = "w") as file:
		file.write(personal_greeting)
		

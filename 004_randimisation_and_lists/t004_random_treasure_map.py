from random import randint as rand
treasure = \
[["[]","[]","[]"] , \
["[]","[]","[]"] , \
["[]","[]","[]"]]  

dug = \
[["[]","[]","[]"] , \
["[]","[]","[]"] , \
["[]","[]","[]"]]  



treasure[rand(0,2)][rand(0,2)] = "[X]"

done = False
while (not done):
	try:
		row = int(input("Which line would you like to dig? "))
		col = int(input("Which row would you like to dig? "))
		if(row > 2 or row < 0 or col > 2 or row < 0):
			print("Wrong input, Try again ")
			continue
	except Exception: 
		print("Wrong input, Try again! ")
		continue
	if(treasure[row][col] == "[X]"):
		dug[row][col] = "[x]"
		print("\nCongratulations !!! You found the treasure !")
		done = True
	elif (dug[row][col] == "[]"):
		dug[row][col] = "[.]" 
	else:
		print("You already dug here! ")
	for x in dug:
		print(x)




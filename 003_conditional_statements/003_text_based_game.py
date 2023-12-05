print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/]
*******************************************************************************
''' + "\n\n\n Welcome to your first adventure :)")

crossroad = input("You are on a crossroads, would you like to go left or right? ").lower().strip()

if crossroad == "right":
	print(" You get eaten by a bear. Game Over! ")
	exit(0)
elif crossroad != "left":
	print(" You can't type, therefore you choose left, which is the right path ")

lake = input("You come across a lake, would you like to swim it or wait for a boat? ").lower().strip()

if lake == "swim":
	print(" You drown, Game Over! ")
	exit(0)
elif lake !="wait":
	print(" You can't type, therefore you choose to wait ")

door = input("You sail to an island and find a house with three doors, one is green, one is red and one is blue, which one would you like to open? ").lower().strip()

if door == "green":
	print(" You choose Bulbasaur ")
	exit(0)
elif door == "red":
	print(" You choose Charmander ")
	exit(0)
elif door == "blue":
	print(" You choose squirtle ")
else:
	print(" You can't type, you don't deserve a treaseure ")

# 0- rock, 1- paper, 2- scissors
import asciiModule as am
from random import randint as randint

choices = [am.rock, am.paper, am.scissors]
computer = randint(0,2)
try:
	player = int(input("Pick 0 for rock, 1 for paper, 2 for scissors ").strip())
except Exception:
	print("Invalid input, Try again! ")
	exit(0)
if player >2 or player < 0:
	print("Invalid input, Try again! ")
	exit(0)

print("Computer choose: \n")
print(choices[computer])
print("\nPlayer choose: \n")
print(choices[player])

if player == computer:
	print("It's a draw! ")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
	print("Player wins! ")
else:
	print("Computer wins! ")

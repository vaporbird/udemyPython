size = input("What size would you like your pizza to be? L/M/S : ")
match(size):
	case "L":
		bill = 20
	case "M":
		bill = 15
	case "S":
		bill = 10
	case default:
		print("Please try again!" )
		exit(0)

pepperoni = input("Would you like pepperoni? Y/N : ")
if pepperoni == "Y":
	bill += (2 if bill == 10 else 3)
elif pepperoni != "N":
	print("Please try again!" )
	exit(0)

cheese = input("Would you like extra cheese? Y/N : ")
if cheese == "Y":
	bill += 1
elif cheese != "N":
	print("Please try again!" )
	exit(0)
	
print(f"Your total bill is ${bill}")

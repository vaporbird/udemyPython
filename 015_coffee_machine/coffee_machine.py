from info import MENU as menu, resources, profit

def print_status():
	for r in resources:
		print(f"{r} : {resources[r]}")
	print(f"profit : {round(profit['profit'], 2)}")

def insert_coins():
	total = 0.0
	print("Please insert coins!")
	is_input_correct = False
	while not is_input_correct:
		try :
			total += abs(int(input("How many Pennies would you like to insert? : ")) * 0.01)
			total += abs(int(input("How many Nickels would you like to insert? : ")) * 0.05)
			total += abs(int(input("How many Dimes would you like to insert? : ")) * 0.10)
			total += abs(int(input("How many Quarters would you like to insert? : ")) * 0.25)
		except Exception :
			total = 0.0
			print("Invalid input, please try again!")
			continue
		is_input_correct = True
	return total

def reduce_resources(drink):
	if drink == "espresso" :
		resources["water"] -= menu["espresso"]["ingredients"]["water"]
		resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]

	elif drink == "latte":
		resources["water"] -= menu["latte"]["ingredients"]["water"]
		resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
		resources["milk"] -= menu["latte"]["ingredients"]["milk"]

	elif drink == "cappuccino":
		resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
		resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
		resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]

def are_resources_enough(drink):
	if drink == "espresso" :
		if (resources["water"] - menu["espresso"]["ingredients"]["water"]) < 0:
			print("Not enough water")
			return False
		if (resources["coffee"] - menu["espresso"]["ingredients"]["coffee"]) < 0:
			print("not enough coffee")
			return False
	
	elif drink == "latte":
		if (resources["water"] - menu["latte"]["ingredients"]["water"]) < 0:
			print("not enough water")
			return False
		if (resources["coffee"] - menu["latte"]["ingredients"]["coffee"]) < 0:
			print("not enough coffee")
			return False
		if (resources["milk"] - menu["latte"]["ingredients"]["milk"]) < 0:
			print("not enough milk")
			return False

	elif drink == "cappuccino":
		if (resources["water"] - menu["cappuccino"]["ingredients"]["water"]) < 0:
			print("not enough water")
			return False
		if (resources["coffee"] - menu["cappuccino"]["ingredients"]["coffee"]) < 0:
			print("not enough coffee")
			return False
		if(resources["milk"] - menu["cappuccino"]["ingredients"]["milk"]) < 0:
			print("not enough milk")
			return False

	return True

def are_funds_enough (drink, money):
	if drink == "espresso" and money > menu["espresso"]["cost"]:
		return True
	elif drink == "latte" and money > menu["latte"]["cost"]:
		return True
	elif drink == "cappuccino" and money > menu["cappuccino"]["cost"]:
		return True
	return False

def return_change(drink, money):
	if(drink == "abort"):
		print(f"Not enough funds, refunding {round(money, 2)}")
		return money
	change = money - menu[drink]["cost"]
	print(f"Your change is: {round(change,2)} ")
	return change

def ask_for_drink():
	
	print(profit["profit"])
	drink = input("What would you like? (Espresso/Latte/Cappuccino) ").strip().lower()
	while drink not in ['espresso', 'latte', 'cappuccino','status']:
		drink = input("Please enter a valid input? (Espresso/Latte/Cappuccino) ").strip().lower()
	if drink == "status":
		print_status()
		return
	if not are_resources_enough(drink):
		exit(0)
	credit = insert_coins()
	if not are_funds_enough(drink, credit):
		drink = "abort"
		return_change(drink,credit)
		return
	return_change(drink, credit)
	reduce_resources(drink)
	print("Please take your drink :)")
	#for some reason if profit is just primitive variable (not in a dictionary), it can't be found because of scope???? why does it work with list instead????
	profit["profit"] += menu[drink]["cost"]

is_over = False
while(not is_over):
	ask_for_drink()
	answer = input("Would you like to order again ? (Y/n) : ").strip().upper()
	while answer not in ["Y","N"]: 
		answer = input("Would you like to order again ? (Y/n) : ").strip().upper()
	if answer == "N":
		is_over = True

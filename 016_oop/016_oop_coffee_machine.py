from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_over = False
while(not is_over):
	order = input(f"What would you like to order ? ({menu.get_items()}) : ").lower().strip()
	while not menu.find_drink(order) and order != "off" and order != "report":
		order = input(f"Please enter a valid input. ({menu.get_items()}) : ").lower().strip()
	if order == "off":
		print("Shutting down")
		exit(0)
	if order == "report" :
		coffee_maker.report()
		money_machine.report()
		continue
	drink = menu.find_drink(order)

	if not coffee_maker.is_resource_sufficient(drink):
		print("Sorry not enough resources for this menu item.")
		prompt = input("Do you want to order anything else? (Y/n) ").lower().strip()
		while prompt not in ["y","n"]:
			prompt = input("Please enter a valid input? (Y/n) ").lower().strip()
		if prompt == "n":
			is_over = True
		continue
	
	if not money_machine.make_payment(drink.cost):
		continue
	coffee_maker.make_coffee(drink)
	prompt = input("Do you want to order anything else? (Y/n) ").lower().strip()
	while prompt not in ["y","n"]:
		prompt = input("Please enter a valid input? (Y/n) ").lower().strip()
	if prompt == "n":
		is_over = True


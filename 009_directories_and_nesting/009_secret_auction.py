import os
from art import logo

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


bids = {}

num_of_bidder = 0
bidding_is_over = False
while (not bidding_is_over):
	clear()
	print(logo)
	print("Welcome to the hidden auction")

	num_of_bidder += 1
	name = input(f"Name of Bidder No: {num_of_bidder}: ").strip()

	is_okay = False
	while(not is_okay):
		if(name in bids.keys()):
			name = input("That name is already taken, please choose another one: ").strip()	
			continue
		is_okay = True

	bid = 0.0
	is_okay = False
	while(not is_okay):
		try:
			bid = round(float(input("How much would you like to bid? $").strip()),2)
		except Exception:
			print("Please enter a valid bid: $")
			continue
		is_okay = True

	bids[name] = bid

	is_okay = False
	loop = input("Are there any more bidders (Y/n)?: ").strip().lower() 
	while loop not in ['y','n']:
		loop = input("Please enter a valid input (Y/n): ")
	if loop == 'n':
		bidding_is_over = True

max_bid = 0
max_bidder = ""
for bid in bids:
	if(max_bid < bids[bid]):
		max_bid = bids[bid]
		max_bidder = bid
print(f"Auction is Over!\nThe max bidder is {max_bidder} with ${max_bid}, Congradulations for the win! \n")

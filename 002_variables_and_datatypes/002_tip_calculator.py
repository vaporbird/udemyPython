print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
bill = bill.replace(",",".") #really don't want to error check everything, there is probably a better way to do it than with try catch
correctInput = False
while (not correctInput):
	tipPerc = input("What percentage tip would you like to give? 10,12,15 or 0 :") 
	try:
		tipInt = int(tipPerc)
	except Exception:
		print("Please enter valid input")
		continue

	if ( tipInt == 10 or tipInt == 12 or tipInt == 15 or tipInt == 0):
		correctInput = True
		continue

	print("Please enter valid input")

people = input("How many pople to split the bill? ")

totalPerPerson = round(float(bill) / float(people) * (float(tipPerc) * 0.01 + 1) , 2)
print("Each person should pay : $%.2f" %totalPerPerson) 

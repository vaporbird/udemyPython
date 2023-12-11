def custom_sum(a,b):
	return a + b
def custom_sub(a,b):
	return a - b
def custom_mul(a,b):
	return a * b
def custom_div(a,b):
	return a / b

total = float(input("choose your first number: ").strip())

is_done = False
while(True):
	print(f"Your accumulated result so far s : {total}")
	op = input("Choose an operation: \n+\n-\n*\n/\noperation: ").strip()
	while op not in ["+", "-", "*", "/"]:
		op = input("Invalid input, Please try again (+/-/*//): ")
	
	b = float(input("Choose another number: ").strip())
	def switch(op):
		if op == "+":
			return custom_sum(total,b)
		elif op == "-":
			return custom_sub(total,b)
		elif op == "*":
			return custom_mul(total,b)
		elif op == "/":
			return custom_div(total,b)
		else:
			return 0.0
	total = switch(op)
	print(f"Your result is: {total} ")
	cont = input("Do you want to continue (Y/n): ").strip().lower()
	while(cont not in ["y","n"]):
		cont = input("Please enter a valid input (Y/n): ").strip().lower()
	if cont == "n":
		print(f"Your result it {total}")
		#exit(0)
		break
print("================================= just a test\n")
dictionary = {"+":custom_sum, "-":custom_sub, "*":custom_mul, "/":custom_div}
test1 = dictionary["+"]
test2 = dictionary["-"]
test3 = dictionary["*"]
test4 = dictionary["/"]

print(test1(5,10))
print(test2(5,10))
print(test3(5,10))
print(test4(5,10))

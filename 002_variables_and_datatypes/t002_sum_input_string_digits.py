import sys
input = input("Please enter a number sequence: ")
sum = 0
if len(input) == 0:
	print("\n\033[91mPlease enter an input!\033[0m\n")
	print('This is in the error channel', file=sys.stderr)
	exit(1)
for n in input:
	try:
		int(n)
	except:
		print("\n\033[91mInvalid string, please use numbers only.\n\033[0m")
		print('This is in the error channel', file=sys.stderr)
		exit(1)
	sum = sum + int(n)
print(f"The sum of the digits is : {sum}")

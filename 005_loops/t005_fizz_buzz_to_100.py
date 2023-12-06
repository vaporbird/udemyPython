for i in range (1, 101):
	if not (i % 3 == 0 or i % 5 == 0):
		print(i)
		continue
	if(i % 3 == 0):
		if(i % 5 == 0):
			print("FizzBuzz")
			continue
		print("Fizz")
		continue
	print("Buzz")

def is_it_prime(number):
	for i in range(2, number):
		if number%i == 0:
			return False
	return True

number = int(input("Plese enter a number ").strip())
print(f"The number {number} is : " + "Prime" if is_it_prime(number) else "Not prime")


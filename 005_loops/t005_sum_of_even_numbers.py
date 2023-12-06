try:
	start = int(input("Start Value: ").strip())
	end = int(input("End Value: ").strip())
except Exception:
	print("Invalid input")
	exit(0)
if (start > end):
	print("Invalid input")
	exit(0)
sumator = 0
for i in range (start if start%2 == 0 else start + 1, end + 1 if end > 0 else end - 1, 2):
	sumator += i
print(f"The sum of the even numbers in the range is: {sumator} ")

my_pie = eval(input("Choose your pie! (0-2) : "))
fruits = ["Apple", "Pear", "Peach"]

def make_pie(index):
	try:
		fruit = fruits[index]
	except IndexError:
		fruit = "fruit"
	finally:
		print(fruit + " pie")

make_pie(my_pie)

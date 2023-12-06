heights = [180, 124, 170, 195, 201, 168, 159, 170, 186, 183, 185, 179, 180]

sumator = 0
count = 0
tallest = 0
for height in heights:
	sumator += height
	count += 1
	if tallest < height:
		tallest = height
print(f"The average height of students(manual for) is : {round(sumator/count,2)}")

print(f"The average height of students(build-ins) is : {round(sum(heights)/len(heights),2)}")

print(f"Max height of a student is(manual for): {tallest}")
print(f"Max height of a student is(manual for): {max(heights)}")

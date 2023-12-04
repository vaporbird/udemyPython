print("Hello,\nThe formula for calculating BMI is weight(kg)/height^2(m^2)")
correct = False
while(not correct):
	try:
		height = float(input("Please enter valid height : "));
	except ValueError: #need to put this, because ctrl + c don't work
		print("try again!")
		continue
	print(height)
	correct = True
correct = False

while(not correct):
	try:
		weight = float(input("Please enter valid weight : "));
	except Exception: # or this 
		print("try again!")
		continue

	print(weight)
	correct = True

#Tried weight/ height * height, but the two heights cancel each other, keep in mind, because first you divide, then you multiply by the same value. Took me a fair 10 minutes and chatGPT to figure out why. Sometimes I'm dumb :D
print("Your BMI is : " + str(weight / height ** 2) +"\n")

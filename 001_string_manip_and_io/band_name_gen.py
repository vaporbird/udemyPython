done = False
while(not done):
    city = input("What city did you grew in? ")
    petName = input("What is/was your last pet's name? ")
    print("Your band name should be: " + city + " " + petName)

    tryAgain = input("Do you want to try again? Y/n: ")
    while(tryAgain != "Y" and tryAgain != "y" and tryAgain != "n" and tryAgain != 'N'):
        tryAgain = input("Please enter valid input, Y/n: ")
    
    if (tryAgain == "N" or tryAgain == "n"):
        done = True

print("Thank you for playing :) ...")
print("Created by Ivan Yanchev - vaporbird on 02.12.2023")

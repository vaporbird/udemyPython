#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def jump():
    turn_left()
    move()
    turn_right()
    height = 1

    while not front_is_clear():
        turn_left()
        move()
        turn_right()
        height+=1

    move()
    turn_right()
    for i in range(0,height):
        move()
    turn_left()

def turn_right():
    for i in range(0,3):
        turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

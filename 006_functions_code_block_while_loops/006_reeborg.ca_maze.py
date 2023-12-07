#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    for i in range(0, 3):
        turn_left()

preventInfinite = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        preventInfinite += 1
        if preventInfinite >= 4:
            if front_is_clear():
                preventInfinite = 0
                move()
    elif front_is_clear():
        preventInfinite = 0
        move()
    else:
        while not front_is_clear():
            turn_left()
            preventInfinite = 0
        move()



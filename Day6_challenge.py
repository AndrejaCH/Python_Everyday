###############################################
## WHILE LOOPS AND FUNCTIONS
##############################################

## NOTES: CHECK THIS WHILE LOOP - WORKS AS IF/ELSE
## SEE THE INDENTATION AT THE WHILE 
## MAZE ROBOT PRACTICE: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
            move()
    turn_left()

while at_goal() == False:
    if wall_in_front():
            jump()
    else:
        move()

##############################################################
## MAZE CHALLENGE: DAY 6
##############################################################
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
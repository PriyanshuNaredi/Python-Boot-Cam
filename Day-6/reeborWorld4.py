def up():
    turn_left()
    move()
    
def down():
    turn_left()
    turn_left()
    turn_left()
    move()
def right():
    turn_left()
    turn_left()
    turn_left()
    
def jump(): 
    turn_left()
    while wall_on_right():
        move()
    right()
    move()
    right()
    while front_is_clear():
        move()
    turn_left()
    

    
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

    
import numpy as np
     
layout = np.array([
    ['|','|','|'],
    ['|','|','|'],
    ['|','|','|']
])


is_empty = ([
    [True,True,True],
    [True,True,True],
    [True,True,True]
])

def check(list,player):
    return(all(player == i for i in list))


players = ['X','O']

def user(str):
    print(layout)
    row = int(input("Enter row no. "))
    col = int(input("Enter col no. "))
    if is_empty[row][col]:
        layout[row][col] = str
        is_empty[row][col] = False
    else:
        print("dhang se khel le")
        user(str)

def check_winner():

    for i in players:
        for j in range(3):
            if (check(list(layout[j]),i) 
                or check(list(layout[:,j]),i)
                or check(list(np.diag(layout)),i)
                or check(list(np.fliplr(layout).diagonal()),i)   ):
                return True
                break
                


is_game_on = True
while is_game_on:

    for i in players:
        user(i)
        if check_winner():
            print(f"Player{i} is the Winner")
            is_game_on=False
            break
    
    

# print(np.diag(layout))
# print(np.fliplr(layout).diagonal())
import art
import game_data
import random
import os
# Logo
print(art.logo)
# score
# USER_SCORE = 0
# randomB = random.choice(game_data.data)

def game_on(USER_SCORE,randomB):
    print(f"Current Score is {USER_SCORE}")
    # compare A
    # global randomB
    randomA = randomB
    randomB = random.choice(game_data.data)
    while randomA == randomB:
        randomB = random.choice(game_data)
    print("Compare A : " + randomA["name"] + ", a " +
        randomA["description"] + ", from "+randomA["country"])
    A = randomA["follower_count"]
    # VS logo
    print(art.vs)
    # Compare
    print("Compare B : " + randomB["name"] + ", a " +
        randomB["description"] + ", from "+randomB["country"])
    B = randomB["follower_count"]
    # user choice
    print(f"{A} & {B}")
    user_choice = input("Who has more followers? Type A or B ").upper()
    if user_choice == "A" and A > B:
        os.system('cls')
        game_on(USER_SCORE + 1,randomB)
    elif user_choice == "B" and A < B:
        os.system('cls')
        game_on(USER_SCORE + 1,randomB)
    else:
        print(f"You Loose, Your score was {USER_SCORE}")
        wanna_play_more = input("press Y to play again ").upper()
        if wanna_play_more == 'Y':
            os.system('cls')
            game_on(0,random.choice(game_data.data))
        

game_on(0,random.choice(game_data.data))

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock,paper,scissors]

user_input = int(input("What do you choose?\n Type 0 for Rock \n Type 1 for Paper \n Type 2 for Scissors \n"))
if user_input >= 3 or user_input < 0:
    print("sahi sa type kar") 
else:
    print(game_images[user_input])
    comp_input = random.randint(0,2)
    print("Computer choose")
    print(game_images[comp_input])


    if user_input == 0 and comp_input ==2:
        print("you win")
    elif comp_input == 0 and user_input ==2:
        print("you lose")
    elif comp_input > user_input:
        print("computer Wins!!")
    elif user_input>comp_input:
        print("You Win!!")
    elif comp_input == user_input:
        print("Draw")
   

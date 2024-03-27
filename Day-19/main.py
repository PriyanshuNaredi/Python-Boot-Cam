import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title = "Make your bet", prompt = "which turtle will win the race? Entre a color:")

is_game_on = False

all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = [-70, -40, -10, 20, 50, 80]

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto( x = -230, y = y_pos[i] )
    all_turtles.append(tim)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won. The {winning_color} turtle is the winner")
            else:
                print(f"you have lost. The {winning_color} turtle is the winner")
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)        



screen.exitonclick()

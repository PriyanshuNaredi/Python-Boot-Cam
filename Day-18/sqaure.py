import turtle
from turtle import Turtle,Screen

tim = turtle.Turtle()
print(tim)
tim.shape("turtle")
tim.color("coral")

for i in range(4):
    tim.forward(100)
    tim.left(90)




my_screen = Screen()
my_screen.exitonclick()
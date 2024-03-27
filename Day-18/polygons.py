import turtle
from turtle import Turtle,Screen
import random

tim = turtle.Turtle()
print(tim)
tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_polygon():
    for i in range(3,11):
        angle = 360 / i
        tim.color(random.choice(colours))
        for i in range(i):
            tim.forward(100)
            tim.left(angle)


draw_polygon()
my_screen = Screen()
my_screen.exitonclick()
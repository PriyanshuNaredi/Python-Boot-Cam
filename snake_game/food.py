import random
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        rand_x = random.randint(-200,200)
        rand_y = random.randint(-200,200)
        self.goto(rand_x,rand_y)
        
    def refresh(self):
        rand_x = random.randint(-200,200)
        rand_y = random.randint(-200,200)
        self.goto(rand_x,rand_y)
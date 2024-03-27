import turtle as t

tim = t.Turtle()
for i in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    


my_screen = t.Screen()
my_screen.exitonclick()
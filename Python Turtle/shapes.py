from turtle import Turtle, Screen
from random import choice
turtle = Turtle()

for i in range(4,11):
   # turtle.pencolor(choice["yellow", "green", "red", "blue", "orange", "pink"])
    angel = 360/i
    while i>0:
        turtle.forward(100)
        turtle.right(angel)
        i-=1




screen = Screen()
screen.exitonclick()
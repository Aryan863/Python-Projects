from turtle import Turtle, Screen
import turtle
import random 


tim = Turtle()
turtle.colormode(255)
tim.pensize(width=5)
direction=[0, 90, 180, 270]
tim.pensize(9)
tim.speed("fastest")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.color(random_colour())

screen = Screen()
screen.exitonclick()
import turtle
import random
import colorgram
import math

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
turtle.colormode(255)
colours = colorgram.extract("Python Turtle\hirst-1.webp", number_of_colors=450)
rgb_colours = []
num_dots = 100

tim.setheading(220)
tim.forward(300)
tim.setheading(0)

def RGBcolours(colours):
    for colour in colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        i = (r, g, b)
        rgb_colours.append(i)

    return rgb_colours


def hirst():
    for i in range(10):
        for j in range(10):
            tim.color(random.choice(RGBcolours(colours)))
            tim.dot(size=15)
            tim.forward(50)
    
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        


hirst()
screen = turtle.Screen()
screen.exitonclick()
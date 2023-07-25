import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.pensize(width=5)
direction=[0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
def draw_spirograph(tilt):
    for _ in range(int(360/tilt)):
        tim.circle(radius=100)
        heading = tim.heading()
        tim.setheading(heading+tilt)
        tim.color(random_colour())

draw_spirograph(2)
screen = turtle.Screen()
screen.exitonclick()
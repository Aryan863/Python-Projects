import turtle
import random

is_game_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? : Enter colour- ")
colours = ["red", "gold", "cyan", "green", "blue", "orange"]
all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]


for i in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win!!!. The winning color is {winning_colour}")
            else:
                print(f"You lose. The winning color is {winning_colour}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        

screen.exitonclick()
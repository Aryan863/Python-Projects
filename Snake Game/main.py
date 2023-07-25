from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()                         # Event listeners not needed in loop
screen.onkey(key="Up", fun=snake.up)    #higher order function. hence while passing function name, () paranthesis is not needed
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    

    


screen.exitonclick()
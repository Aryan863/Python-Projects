from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

X_END = 282
Y_END = 282

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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
    
# Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

# Detect collision with walls
    if snake.head.xcor() >X_END or snake.head.xcor() < -X_END or snake.head.ycor() >Y_END or snake.head.ycor() < -Y_END:
        scoreboard.reset()
        snake.reset()

# detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
    


screen.exitonclick()
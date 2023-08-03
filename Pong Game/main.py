from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboeard = ScoreBoard()

screen.listen()                              # Event listeners not needed in loop
screen.onkey(key="Up", fun=r_paddle.up)      # Higher order function. hence while passing function name, () not needed
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)   
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() >320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # Detecting collision with right wall
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboeard.l_point()
        time.sleep(0.5)

    # Detecting collision with left wall    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboeard.r_point()
        time.sleep(0.5)

screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()                       
screen.onkey(key="Up", fun=player.up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create new car
    cars.new_car()

    #move all cars
    cars.move()
        
    # check collision with cars
    for car in cars.car_list:
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on = False
    
    # Reached the end and level up
    if player.is_at_finish():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
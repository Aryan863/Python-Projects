from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
  
    
    def new_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            x_cor = 300
            y_cor = random.randint(-250, 250)
            car.goto(x_cor, y_cor)
            self.car_list.append(car)
    
    def move(self):
        for cars in self.car_list:
            cars.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

        


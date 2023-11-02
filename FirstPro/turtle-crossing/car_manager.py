import random
from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = MOVE_INCREMENT

    def car_creator(self):
        random_choice = randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.speed += MOVE_INCREMENT

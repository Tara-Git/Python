import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_1 = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.car_creator()
    cars.move_forward()

    # detect collision with car
    for car in cars.all_cars:
        if player_1.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.game_over()

    # detect if the game is finished and go for the next level
    if player_1.is_game_finished():
        player_1.go_to_start()
        cars.level_up()
        scoreboard.increases_level()





screen.exitonclick()


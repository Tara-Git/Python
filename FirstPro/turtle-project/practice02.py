from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

"""
for _ in range(4):
    tim.forward(100)
    tim.left(90)


for _ in range(15):
    tim.forward(5)
    tim.up()
    tim.forward(5)
    tim.down()
"""

my_tuple = (1, 2, 3)  # you cannot change it that means ---> my_tuple[2] = 12 # is not allowed
print(my_tuple[2])

list(my_tuple)  # but you can convert it to list



screen.colormode(255)
tim.pensize(10)
tim.speed("fastest")

directions = [0, 90, 180, 270]


def draw_line_random_direction():
    tim.forward(20)
    tim.setheading(random.choice(directions))


for _ in range(200):
    tim.pencolor(random.randrange(255), random.randrange(255), random.randrange(255))
    draw_line_random_direction()

screen.exitonclick()

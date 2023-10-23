from turtle import Turtle, Screen
from random import random, randrange

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
screen.colormode(255)

tim.up()
tim.left(270)
tim.forward(100)
tim.left(90)
tim.down()


def draw_shape(num_sides):
    angel = 360 / num_sides
    for x in range(num_sides):
        tim.forward(100)
        tim.left(angel)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    tim.pencolor(randrange(255), randrange(255), randrange(255))





screen.exitonclick()
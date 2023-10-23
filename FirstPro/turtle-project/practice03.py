from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.pensize(2)
tim.speed("fastest")


def random_color():
    return (random.randrange(255), random.randrange(255), random.randrange(255))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

screen.exitonclick()

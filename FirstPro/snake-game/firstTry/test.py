from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.tracer(0)


segments = []
for position in STARTING_POSITIONS:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()

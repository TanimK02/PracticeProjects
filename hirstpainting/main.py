from turtle import Turtle, Screen, colormode
from random import choice

screen = Screen()
tim = Turtle()
colormode(255)
tim.pensize(15)
tim.penup()
tim.speed('fastest')
tim.hideturtle()
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84)]


def make_painting():
    height = -250
    count = 10
    for i in range(count):
        tim.goto(-250, height)
        for i in range(count):
            tim.penup()
            tim.color(choice(color_list))
            tim.dot()
            tim.forward(50)
        height += 50

make_painting()
screen.exitonclick()





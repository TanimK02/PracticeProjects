from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.increment = STARTING_MOVE_DISTANCE
        self.start = (300, randint(-280, 280))
        self.make_cars()


    def move(self):
        self.back(self.increment)

    def increase_speed(self):
        self.increment += MOVE_INCREMENT

    def make_cars(self):
        self.penup()
        self.color(choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.setpos(self.start)


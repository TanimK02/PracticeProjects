from turtle import Turtle
from random import choice,randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager():
    def __init__(self):
        super().__init__()
        self.increment = STARTING_MOVE_DISTANCE
        self.amount_car = 0
        self.list = []
        self.amount_of_cars()

    def increase_speed(self):
        self.increment += MOVE_INCREMENT


    def make_cars(self):
        cars = 0
        while cars < self.amount_car:
            car = Turtle()
            car.limit = -300
            car.setheading(90)
            car.penup()
            car.color(choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=2,stretch_len=1)
            car.setpos(CarManager.position_setting())
            car.y = car.ycor()
            car.x = car.xcor()
            self.list.append(car)
            cars += 1

    def move_car(self):
        for car in self.list:
            car.x -= self.increment
            car.goto(car.x,car.y)


    def destroy_car(self):
        for car in self.list:
            if car.xcor() <= -300:
                car.setpos(CarManager.reset_position())
                car.y = car.ycor()
                car.x = car.xcor()

    @staticmethod
    def position_setting():
        start = (randint(-270, 300), randint(-240, 280))
        return start

    @staticmethod
    def reset_position():
        start = (randint(300, 450), randint(-240, 280))
        return start

    def amount_of_cars(self):
        self.amount_car = 0
        for car in self.list:
                car.hideturtle()
                car.clear()
        self.amount_car = randint(6,10)


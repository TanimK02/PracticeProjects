import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
max_cars = randint(5,25)
car_list = []
score = Scoreboard()
screen.onkey(fun=player.move_up, key='w')
screen.onkey(fun=player.move_down, key='s')
screen.onkey(fun=player.move_right, key='d')
screen.onkey(fun=player.move_left, key='a')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    while len(car_list) < max_cars:
        for car in range(max_cars):
            cars = CarManager()
            car_list.insert(car, cars)

    if player.finish() is True:
        score.add_score()



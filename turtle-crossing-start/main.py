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
car_manager = CarManager()
max_cars = randint(5,25)

score = Scoreboard()
screen.onkey(fun=player.move_up, key='w')
screen.onkey(fun=player.move_down, key='s')
screen.onkey(fun=player.move_right, key='d')
screen.onkey(fun=player.move_left, key='a')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if len(car_manager.list) < car_manager.amount_car:
        car_manager.make_cars()
    if player.ycor() > -270:
        car_manager.move_car()
    for car in car_manager.list:
        if player.distance(car) <= 20:
            score.lose()
            game_is_on = False
    if player.finish() is True:
        score.add_score()
        car_manager.amount_of_cars()
        car_manager.increase_speed()
    car_manager.destroy_car()
screen.exitonclick()



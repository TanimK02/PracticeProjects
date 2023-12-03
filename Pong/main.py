from turtle import Turtle, Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
r_coords = (350,0)
l_coords = (-350,0)

l_paddle = Paddle(l_coords)

r_paddle = Paddle(r_coords)

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=l_paddle.move_up, key='w')
screen.onkey(fun=l_paddle.move_down, key='s')
screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')


game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.increase_speed()
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.increase_speed()
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.r_point()
        ball.reset_pos()

    if ball.xcor() < -400:
        scoreboard.l_point()
        ball.reset_pos()

screen.exitonclick()

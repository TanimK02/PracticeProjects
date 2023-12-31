from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='d', fun=snake.right)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='s', fun=snake.down)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()




















screen.exitonclick()
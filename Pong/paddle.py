from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,coordinates):
        super().__init__()
        self.goto(coordinates[0],coordinates[1])
        self.penup()
        self.setheading(90)
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_len=5)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


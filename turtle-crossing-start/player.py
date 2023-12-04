from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.color('green')
        self.x_move = STARTING_POSITION[0]
        self.y_move = STARTING_POSITION[1]

    def move_up(self):
        self.y_move += MOVE_DISTANCE
        self.goto(self.x_move,self.y_move)

    def move_down(self):
        self.y_move -= MOVE_DISTANCE
        self.goto(self.x_move,self.y_move)

    def move_right(self):
        self.x_move += MOVE_DISTANCE
        self.goto(self.x_move, self.y_move)

    def move_left(self):
        self.x_move -= MOVE_DISTANCE
        self.goto(self.x_move, self.y_move)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.hideturtle()
            self.goto(STARTING_POSITION)
            self.x_move = STARTING_POSITION[0]
            self.y_move = STARTING_POSITION[1]
            self.showturtle()
            return True






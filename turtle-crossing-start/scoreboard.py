from turtle import Turtle

POSITION = (0, 265)
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.setpos(POSITION)
        self.write(arg=f"Score: {self.score}", align='center', font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
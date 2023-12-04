from turtle import Turtle

POSITION = (-280, 265)
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
        self.write(arg=f"Level: {self.score}", align='left', font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def lose(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.setpos(0,0)
        self.write(arg=f"YOU LOST", align='center', font=("Courier", 48, "normal"))
        self.setpos(0,-48)
        self.write(arg=f"FINAL LEVEL:{self.score}", align='center', font=("Courier", 48, "normal"))

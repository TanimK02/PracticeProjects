from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("courier", 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setpos(0,270)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.count}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.count += 1
        self.update_score()

    def game_over(self):
        self.setpos(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)




from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("courier", 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = 0
        with open('data.txt','r') as data:
            self.high_score = int(data.read())
        self.setpos(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.count} High Score:{self.high_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.count += 1
        self.update_score()

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open('data.txt', 'w') as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_score()




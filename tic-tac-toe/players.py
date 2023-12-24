from random import randint

class Player:
    def __init__(self,letter):
        self.letter = letter
    
    def get_move(self,game):
        pass

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            try:
                move = int(input("pick board num from 1-9: ")) - 1
                if move >= 0 and move <9:
                    if game[move] != "X" and game[move] != "O":
                        game[move] = self.letter
                        return game
                else:
                    print("1-9 only and can't already be picked")
            except ValueError:
                print("it has to be a number")
                pass
            
        
class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            move = randint(0,8)
            if game[move] != "X" and game[move] != "O":
                game[move] = self.letter
                return game
            else:
                pass
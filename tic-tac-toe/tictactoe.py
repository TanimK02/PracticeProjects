import players
import os

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
        self.winner = None
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def check_horiz(self,letter):
        for row in range(0,9,3):
            if all(element == letter for element in self.board[row:row+3]):
                return False
            return True
        
    def check_vert(self, letter):
        for col in range(3):
            # Count the number of occurrences of `letter` in the column
            count = sum(1 for row in range(3) if self.board[row * 3 + col] == letter)

            # If all three cells in a column contain the letter, return True
            if count == 3:
                return False

        # If no column contains three of the letter, return False
        return True
    
    def check_diag(self,letter):
        # x = 0
        diagonal = [self.board[0],self.board[4],self.board[8]]
        if all(element == letter for element in diagonal):
            return False
        diagonal2 = [self.board[2], self.board[4], self.board[6]]
        if all(element == letter for element in diagonal2):
            return False
        return True
  
    def check_winner(self,letter):
        decision = True
        decision = self.check_horiz(letter)
        if decision == False:
            self.winner = letter
            return decision
        decision = self.check_vert(letter)
        if decision == False:
            self.winner = letter
            return decision
        decision = self.check_diag(letter)
        if decision == False:
            self.winner = letter
            return decision
        return decision
    
    def check_full(self):
        blank = " " in self.board
        if blank:
            return True
        else:
            return False
    
game = TicTacToe()
letter = input("Do you want to go first? yes or no ")
x = "X"
o = "O"
if letter == "yes":
    player = players.Human(x)
    computer = players.Computer(o)
    game.print_board()
    game_going = True
    full = True
    while game_going is True and full is True:
        player.get_move(game.board)
        os.system('clear')
        game.print_board()
        game_going = game.check_winner(x)
        full = game.check_full()
        if game_going is True and full is True:
            computer.get_move(game.board)
            os.system('clear')
            game.print_board()
            game_going = game.check_winner(o)
            full = game.check_full()
else:
    player = players.Human(o)
    computer = players.Computer(x)
    game.print_board()
    game_going = True
    full = True
    while game_going is True and full is True:
        computer.get_move(game.board)
        os.system('clear')
        game.print_board()
        game_going = game.check_winner(x)
        full = game.check_full()
        if game_going is True and full is True:
            player.get_move(game.board)
            os.system('clear')
            game.print_board()
            game_going = game.check_winner(o)
            full = game.check_full()

os.system('clear')
if game.winner is None:
    print(f"{game.winner} Wins!")
else:
    print(f"{game.winner} Wins!")
game.print_board()




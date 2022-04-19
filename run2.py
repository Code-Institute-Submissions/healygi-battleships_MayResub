from random import randint

greeting = "Welcome to Battleships- play against the computer and be the first to sink all 5 of your opponent's ships."
print(greeting)

#ask for players name

name = input("What is your name Comrade? " )
print("Hello " + name )
print("lets set out to sea and destroy the computers ships!!")

class Board(object):
    size_x = 8
    size_y = 8
    ships_number = 5
    empty_symbol = "*"
    ship_symbol = "0"
    values = []
    label = ""
    hit = "X"
   # guesses = []

    def __init__(self, label):
        self.values = []
        self.label = label

    def generate(self):
        for row in range(0, self.size_y):
            columns = []
            for column in range(0, self.size_x):
                columns.append(self.empty_symbol)
            self.values.append(columns)
    
    def print(self, hidden=True):
        print("    " + self.label + " Board")
        print("=====================")
        for row in self.values:
            formated_row = " ".join(row)
            formated_row = "== " + formated_row + " =="
            if hidden:
                formated_row = formated_row.replace(self.ship_symbol, self.empty_symbol) 
            print(formated_row)
        print("=====================")

    def place_ships_auto(self):
        ships_placed = 0
        while ships_placed < self.ships_number:
            random_x = randint(0, self.size_x - 1)
            random_y = randint(0, self.size_y - 1)
            # TODO validate space is empty
            self.values[random_x][random_y] = self.ship_symbol
            ships_placed = ships_placed + 1

    def guess_is_valid(self, guess_x, guess_y):
        try:
            x = int(guess_x)
            y = int(guess_y)
            if (x <= self.size_x and y <= self.size_y) and (x>0 and y>0):
                return True
            else:
                print('Coordinates outside the board, please enter again')
                return False
        except:
            print('Please enter a integer number')
            return False

    def user_guess(self, pc_board):
        input_valid = False
        while input_valid is False:
            x = input(f'Row [0 - {self.size_x}]: ')
            y = input(f'Column [0 - {self.size_y}]: ')
            input_valid = self.guess_is_valid(x, y)
        self.attack_board(int(x), int(y), pc_board)

    def attack_board(self, x, y, opponent_board):
        print(f'Attacking {opponent_board.values[x][y]}')

    def pc_guess(self, user_board):
        input_valid = False
        while input_valid is False:
            x = randint(0,8)
            y = randint(0,8)
            input_valid = self.guess_is_valid(x, y)
        print("Computers turn to attack")
        print("Shots fired....")
        self.attack_board(int(x), int(y), user_board)
        print(f'computer guess:[ {int(x)} , {int(y)} ]')

    def continue_game(self):
        input(f'Both you and the pc missed- do you want to continue? y/n?' )
        if 'y':
            user_guess()
            pc_guess()
        else:
            print('GAME OVER!')


if __name__ == "__main__":
    pc_board = Board("PC")
    pc_board.generate()
    pc_board.place_ships_auto()
    pc_board.print(False)
    user_board = Board(name.capitalize() + "'s")
    user_board.generate()
    user_board.place_ships_auto()
    user_board.print(False)
    pc_board.user_guess(pc_board)
    user_board.pc_guess(user_board)
    user_board.continue_game()
    pc_board.continue_game()




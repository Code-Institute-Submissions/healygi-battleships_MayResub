from random import randint
# greeting function for user


def start_game():
    greeting = "Welcome to Battleships"
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(greeting.upper())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    name = input("What is your name Comrade?")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Hello " + name)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("lets set out to sea and destroy the pc ships!!")
    print("Instructions: Board size 7x7.")
    print("Number of ships - 5. Top left corner")
    print("is [row:0, column:0]")
    print("Play against the computer")
    print("be the first to sink all 5 ships.")
    print("You have 15 turns to win")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("LETS PLAY!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return name

# model a board for user and pc


class Board(object):
    size_x = 8
    size_y = 8
    ships_number = 5
    empty_symbol = "*"
    ship_symbol = "0"
    values = []
    label = ""
    hit = "X"
    miss = "-"
    hits_counter = 0

    def __init__(self, label):
        self.values = []
        self.label = label

# generate board

    def generate(self):
        for row in range(0, self.size_y):
            columns = []
            for column in range(0, self.size_x):
                columns.append(self.empty_symbol)
            self.values.append(columns)
# print board

    def print(self, hidden=True):
        print("    " + self.label + " Board")
        print("=====================")
        for row in self.values:
            formated_row = " ".join(row)
            formated_row = "== " + formated_row + " =="
            if hidden:
                formated_row = formated_row.replace(
                    self.ship_symbol, self.empty_symbol)
            print(formated_row)
        print("=====================")

# randomly places ships on boards
    def place_ships_auto(self):
        ships_placed = 0
        while ships_placed < self.ships_number:
            random_x = randint(0, self.size_x - 1)
            random_y = randint(0, self.size_y - 1)
            self.values[random_x][random_y] = self.ship_symbol
            ships_placed = ships_placed + 1

# validates guesses
    def guess_is_valid(self, guess_x, guess_y):
        try:
            x_target = int(guess_x)
            y_target = int(guess_y)
            if (x_target < self.size_x and y_target < self.size_y) and (
             x_target >= 0 and y_target >= 0):
                return True
            else:
                print('Coordinates outside the board, please enter again')
                return False
        except ValueError:
            print('Please enter a integer number')
            return False

# allows for user input to take guess at pc board
    def user_guess(self):
        input_valid = False
        while input_valid is False:
            print(f"Guess a Row and Column between [0-{self.size_x - 1}]")
            x_shot = input(f'Row [0 - {self.size_x - 1}]: ')
            y_shot = input(f'Column [0 - {self.size_y - 1}]: ')
            input_valid = self.guess_is_valid(x_shot, y_shot)
        self.attack_board(int(x_shot), int(y_shot), pc_board)
        print(f"you have sank {self.hits_counter} of pc's battleships!")
        if self.hits_counter == self.ships_number:
            print("YOU HAVE HIT ALL PC SHIPS!")

        """
        if statment to check if guess is a hit or not. Attack
        method for computer and user to attack board
        """
    def attack_board(self, x_hit, y_hit, opponent):
        print(f'{opponent.label} battleships prepare for incoming fire....')
        if opponent.values[x_hit][y_hit] == self.ship_symbol:
            print("HIT!")
            self.hits_counter = self.hits_counter + 1

            opponent.values[x_hit][y_hit] = self.hit
            if self.label == 'PC':
                self.print(True)
            else:
                self.print(False)
            return

        elif opponent.values[x_hit][y_hit] == self.empty_symbol:
            print("MISS!")

            opponent.values[x_hit][y_hit] = self.miss
            if self.label == 'PC':
                self.print(True)
            else:
                self.print(False)
            return

        else:
            print("You guessed that one already!")
            print("Please guess again")
            self.user_guess()
            self.pc_guess()
            return

    # allows for pc to take guess at user board
    def pc_guess(self):
        input_valid = False
        while input_valid is False:
            x_guess = randint(0, self.size_x - 1)
            y_guess = randint(0, self.size_y - 1)
            input_valid = self.guess_is_valid(x_guess, y_guess)
        print("Computers turn to attack")
        print("Shots fired....")
        self.attack_board(int(x_guess), int(y_guess), user_board)
        print(f'computer guess:[{int(x_guess)} , {int(y_guess)}]')
        if self.hits_counter == self.ships_number:
            print("ALL OF USERS BATTLESHIPS ARE DESTORYED")


"""loops through turns and alerts user
    or pc if they have won or if game is over."""


def run_game(pc_board, user_board):
    turns = 12
    while turns > 0:
        user_board.user_guess()
        pc_board.pc_guess()
        turns -= 1
        if user_board.hits_counter == pc_board.ships_number:
            print(' User WINS!!!!')
            turns = 0
        if pc_board.hits_counter == user_board.ships_number:
            print(' PC WINS!!!!')
            turns = 0
        if turns <= 5:
            print(f"You have {turns} turns remaining")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("GAME OVER!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    again = input("Play again? Type yes or press any key to quit?")
    print(again)
    if (again == "yes") or (again == "Yes") or (
                again == "YES") or (again == "y"):
        print("Please press 'RUN PROGRAM' to restart game")
    else:
        print(f"Thank you {name.capitalize()} for playing battleships!")


if __name__ == "__main__":
    name = start_game()
    pc_board = Board("PC")
    pc_board.generate()
    pc_board.place_ships_auto()
    pc_board.print(True)
    user_board = Board(name.capitalize() + "'s")
    user_board.generate()
    user_board.place_ships_auto()
    user_board.print(False)
    run_game(pc_board, user_board)

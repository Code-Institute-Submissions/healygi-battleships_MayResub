from random import randint

def start_game():
    greeting = "Welcome to Battleships"
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(greeting.upper())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #ask for players name
    name = input("What is your name Comrade?")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Hello " + name)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("lets set out to sea and destroy the pc ships!!")
    print("Instructions: Board size 7x7. Number of ships- 5. Top left corner is (row:0, column:0). Play against the computer and be the first to sink all 5 of your opponent's ships. You have 15 turns to win")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("LETS PLAY!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return name

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
            self.values[random_x][random_y] = self.ship_symbol
            ships_placed = ships_placed + 1

    def guess_is_valid(self, guess_x, guess_y):
        try:
            x = int(guess_x)
            y = int(guess_y)
            if (x < self.size_x and y < self.size_y) and (x >= 0 and y >= 0):
                return True
            else:
                print('Coordinates outside the board, please enter again')
                return False
        except:
            print('Please enter a integer number')
            return False

    def user_guess(self):
       # self.print(False)
        input_valid = False
        while input_valid is False:
            print(f"Guess a Row and Column between [0-{self.size_x - 1}]")
            x = input(f'Row [0 - {self.size_x - 1}]: ')
            y = input(f'Column [0 - {self.size_y - 1}]: ')
            input_valid = self.guess_is_valid(x, y)
        self.attack_board(int(x), int(y), pc_board)
        print(f"you have sank {self.hits_counter} of pc's battleships!")
        if self.hits_counter == self.ships_number:
            print("YOU HAVE HIT ALL PC SHIPS!")

        """
        if statment to check if guess is a hit or not. Attack
        method for computer and user to attack board
        """
    
    def attack_board(self, x, y, opponent):
        print(f'{opponent.label} battleships prepare for incoming fire....')
        if opponent.values[x][y] == self.ship_symbol:
            print("HIT!")
            self.hits_counter = self.hits_counter + 1

            opponent.values[x][y] = self.hit
            if self.label == 'PC':
                self.print(True)
            else:
                self.print(False)
            return

        elif opponent.values[x][y] == self.empty_symbol:
            print("MISS!")

            opponent.values[x][y] = self.miss
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
             
    def pc_guess(self):
        input_valid = False
        while input_valid is False:
            x = randint(0, self.size_x -1)
            y = randint(0, self.size_y -1)
            input_valid = self.guess_is_valid(x, y)
        print("Computers turn to attack")
        print("Shots fired....")
        self.attack_board(int(x), int(y), user_board)
        print(f'computer guess:[{int(x)} , {int(y)}]')
        if self.hits_counter == self.ships_number:
            print(f"ALL OF USERS BATTLESHIPS ARE DESTORYED")

def run_game(pc_board, user_board):
    turns = 15
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
        if turns <= 5 :
            print(f"You have {turns} turns remaining")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("GAME OVER!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    again = input("Do you want to play again, type yes or press any key to quit?")
    print(again)
    if (again == "yes") or (again == "Yes") or (again == "YES") or (again == "y"):
        pc_board = Board("PC")
        pc_board.generate()
        pc_board.place_ships_auto()
        pc_board.print(True)
        user_board = Board(name.capitalize() + "'s")
        user_board.generate()
        user_board.place_ships_auto()
        user_board.print(False)
        run_game(pc_board, user_board)
    else:
        print(f"Thank you {name.capitalize()} for playing battleships! Come back soon!")

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
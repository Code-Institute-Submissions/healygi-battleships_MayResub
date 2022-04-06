from random import randint

scores = {"computer": 0, "player": 0}
#Create greeting message for player

greeting = "Welcome to battlships- play against the computer and be the first to sink all 5 of your opponent's ships."
print(greeting)

#Ask for players name

name = input("What is your name Comrade? " )
print("Hello " + name )
print("lets set out to sea and destroy the computers ships!!")

# Instructions on how to play

#Create variable to make board and store ships
board = [[" "] * 4 for x in range(8)]
#Create variable to display misses and hits
hidden_board =  [[" "] * 4 for i in range(8)]
print(board)

class Board:

    def __init__(self, size, ships, name, type):
        #Initialize board
        self.size = size
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)]
        self.name = name 
        self.type = type 
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row)
            
    def guess(self, x, y):
        self.guess.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "&"

    def random_point(size):
        """
        Helper function to return a random integer between 0 and size
        """
        return randint(0, size - 1)

def valid_coordinates(x, y, board):

def populate_board():

def make-guess(board):

def start_game(computer_board, player_board):

def start_game():
    """
    Starts a new game. Sets the board size and number of ships
    resets the scores and initialises the boards.
    """
    size = 5
    num_ship = 4
    scores["computer"] = 0
    scores["player"] = 0
    print ("-" * 35)
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)


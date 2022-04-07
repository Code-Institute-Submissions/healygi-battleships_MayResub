from random import randint

scores = {"computer": 0, "player": 0}
#Create greeting message for player

greeting = "Welcome to battleships- play against the computer and be the first to sink all 5 of your opponent's ships."
print(greeting)

#ask for players name

name = input("What is your name Comrade? " )
print("Hello " + name )
print("lets set out to sea and destroy the computers ships!!")

# Instructions on how to play
"""
#Create variable to make board and store ships
board = [[" "] * 4 for x in range(8)]
#Create variable to display misses and hits
hidden_board =  [[" "] * 4 for i in range(8)]
print(board)
"""

class Board:

    def __init__(self, size, num_ships, name, type):
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
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
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
"""
def valid_coordinates(x, y, board):
    #valid dates coorendates input to make sure if they have 
    already been guessed or not outside the coordinates of our board

"""
def populate_board(board):
         self.board = [["." for x in range(size)] for y in range(size)]
         populate_board()



"""
def make_guess(board):
    #processes the guesses- if it is a computer guess does exactly
    the same thing it did when it populated the board 
    choose for random row and random column. If it is a player
    guess input requirded. 

def play_game(computer_board, player_board):
    #deploys game board and starts game

"""

def start_game():

    """
    Starts a new game. Sets the board size and number of ships
    resets the scores and initialises the boards.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    #Create two class instances- intialising it with number of ships, player name and board type

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    """
    for loop creates random placement of ships on player board 
    and computer board. 
    """

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    
  #  play_game(computer_board, player_board)

#start_game()
   


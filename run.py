from random import randint

"""
#Create variable to make board and store ships
board = [[" "] * 4 for x in range(8)]
#Create variable to display misses and hits
hidden_board =  [[" "] * 4 for i in range(8)]
print(board)
"""

class Board:

    def __init__(self, size, ships, name, type):
        """Initialize board attrubutes"""
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
            
    def guesses.append((x, y))
        self.guesses.append((x, y))
        self.board[x][y] = "x"





from random import randint

greeting = "Welcome to battleships- play against the computer and be the first to sink all 5 of your opponent's ships."
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

    def user_guess(self):
    # Subtract 1 to adjust for python 0-based indexing
        x = int(input('Row: ')) - 1 
        y = int(input('Col: ')) - 1
        x_column = int(x, self.size_x - 1)
        y_row = int(y, self.size_y - 1)
        if self.values[x_column][y_row] <= -1:
            return "miss, cannot guess outside the board"
        elif self.values[x_column][y_row] == '0': 
            return "HIT"
        else:
            return "miss"
            

 
            


"""
shot_x = input('Row: ') 
        shot_y = input('Col: ')
       
        if (shot_x, shot_y) in self.empty_symbol:
             self.empty_symbol[shot_x][shot_y] = self.hit
             return "HIT!"
        elif int(shot_x > 8) or int(shot_y > 8):  
            print("Error: you cannot guess outside the board!")
        else:
            return "Miss"

if (x, y) in self.values:
            self.values[x][y] = "X"
            return "Hit"
        else:
            return "Miss! Try again"

 if row and col in self.ship_symbol:
                self.values[row][col] = "X"
                return "HIT!"

            x = int(input('Row: ')) - 1 
            y = int(input('Col: ')) - 1

        for row in self.values:
            row = int(input('Row: ')) - 1 
            col = int(input('Col: ')) - 1


        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

            if row > 8 or col > 8:
                 print("Error: you cannot guess outside the board!")
            else: 
                 self.values[row][col] = self.hit
                 print("HIT!")

"""
            
    


pc_board = Board("PC")
pc_board.generate()
pc_board.place_ships_auto()
pc_board.print(False)
user_board = Board(name.capitalize() + "'s")
user_board.generate()
user_board.print()
pc_board.user_guess()




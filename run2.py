from random import randint


class Board(object):
    size_x = 8
    size_y = 8
    ships_number = 5
    empty_symbol = "*"
    ship_symbol = "0"
    values = []
    label = ""

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


pc_board = Board("PC")
pc_board.generate()
pc_board.place_ships_auto()
pc_board.print(False)
user_board = Board("User")
user_board.generate()
user_board.print()


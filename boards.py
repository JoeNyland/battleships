from random import choice as random_choice
from errors import ShipOffBoardError, CollisionError
from ships import random_orientation as random_ship_orientation


class Board:
    def __init__(self):
        self.shape = (10, 10)
        self.width, self.height = self.shape
        self.contents = [  # TODO: Build from shape
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        self.hits = []
        self.hit_points = 0

    def print(self):
        print('   A B C D E F G H I J')
        print('  +-------------------+')
        for i, row in enumerate(self.contents):
            print('{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(*([str(i + 1).rjust(2)] + row + [str(i + 1).rjust(2)])))
        print('  +-------------------+')
        print('   A B C D E F G H I J')

    def random_coords(self):
        row_index = random_choice(range(len(self.contents)))
        row = self.contents[row_index]
        column_index = random_choice(range(len(row)))
        return row_index, column_index

    def randomly_place_ship(self, ship):
        try:
            # Randomly choose where to start placing ship and its orientation
            (start_row_index, start_column_index) = self.random_coords()
            orientation = random_ship_orientation()
            ship_coords = [(start_column_index, start_row_index)]
            current_row_index, current_column_index = (start_row_index, start_column_index)
            for _ in ['s'] * (ship.size - 1):
                if orientation == 'north-south':
                    current_column_index += 1
                else:
                    current_row_index += 1

                # Make sure that the next co-ord for the ship does not fall off the board
                if (current_column_index < (self.width - 1)) and (current_row_index < (self.height - 1)):
                    # Current co-ord is on the board, so continue
                    ship_coords.append((current_column_index, current_row_index))
                else:
                    # Current co-ord is off the board, so we need to start again
                    raise ShipOffBoardError(
                        "Current co-ord ({},{}) is OFF the board! We need to try again.".format(current_column_index,
                                                                                                current_row_index))

            for (x, y) in ship_coords:
                if self.contents[x][y] == 's':
                    raise CollisionError("There's already a ship at ({},{})".format(x, y))

            # If there were no collisions above, we can now place the ship
            for (x, y) in ship_coords:
                self.contents[x][y] = 's'  # Place this co-ord for the ship

            self.hit_points += ship.size

        except (ShipOffBoardError, CollisionError):
            self.randomly_place_ship(ship)  # Try placing again

    def mark_hit(self, coords):
        x, y = coords
        self.contents[y][x] = 'X'
        self.hits.append((x, y))

    def get_coords(self, coords):
        x, y = coords
        return self.contents[y][x]

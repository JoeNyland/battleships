import random

class Ship:
  def __init__(self):
    self.size = Null

  def __str__(self):
    return '<' + ('=' * (self.size - 1))

  def random_orientation():
    return random.choice(['north-south', 'east-west'])

class Carrier(Ship):
  def __init__(self):
    self.size = 5


class Battleship(Ship):
  def __init__(self):
    self.size = 4


class Destroyer(Ship):
  def __init__(self):
    self.size = 3


class Submarine(Ship):
  def __init__(self):
    self.size = 3


class PatrolBoat(Ship):
  def __init__(self):
    self.size = 2


class Board():
  def __init__(self):
    self.shape = (10,10)
    self.width, self.height = self.shape
    self.contents = [ # TODO: Build from shape
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
      [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ]

  def print(self):
    print('   A B C D E F G H I J')
    print('  +-------------------+')
    for i, row in enumerate(self.contents):
      print('{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*([str(i+1).rjust(2)] + row)))
    print('  +-------------------+')

  def random_coord(self):
    row_index = random.choice(range(len(self.contents)))
    row = self.contents[row_index]
    column_index = random.choice(range(len(row)))
    return (row_index, row, column_index)

  def place_ship(self, ship):
    print('placing size: {0.size}'.format(ship)) # TODO: Remove
    placed = False
    while not placed:
      # Randomly choose where to start placing ship
      (start_row_index, start_row, start_column_index) = self.random_coord()
      print("Start co-ord ({},{}) is on the board, so continue".format(start_column_index, start_row_index)) # TODO: Remove
      # TODO: Support other orientations. Currently only north-south is supported.

      ship_coords = [(start_column_index, start_row_index)]

      current_row_index, current_column_index = (start_row_index, start_column_index)
      for x in ['s'] * (ship.size - 1):
        current_column_index  = current_column_index
        current_row_index    += 1

        # Make sure that the next co-ord for the ship does not fall off the board
        if (current_column_index < (self.width - 1)) and (current_row_index < (self.height - 1)):
          # Current co-ord is on the board, so continue
          print("Current co-ord ({},{}) is on the board, so continue".format(current_column_index, current_row_index))
          ship_coords.append((current_column_index, current_row_index))
          continue
        else:
          # Current co-ord is off the board, so we need to start again
          print("Current co-ord ({},{}) is OFF the board! We need to try again".format(current_column_index, current_row_index))
          break # NOTE -> This needs to skip the while, but it's skipping the for ... in

      placed = True
      print("The ship can be placed. Co-ords: {}".format(ship_coords))

      # TODO: Actually place the ship in ship_coords
      # if self.contents[row_index][column_index] != 's':
      #   # Can place here
      # else:
      #   # Cannot place here
      #   continue


cpu_board = Board()
cpu_ships = [
  Carrier(),
  Battleship(),
  Destroyer(),
  Submarine(), Submarine(),
  PatrolBoat(), PatrolBoat(),
]

def place_ships(board, ships):
  # TODO: Work out how to place ships on the board without collisions
  for ship in ships:
    board.place_ship(ship)

def print_ships(ships):
  for ship in ships:
      print(ship)

if __name__ == "__main__":
  # cpu_board.print()
  # player_board.print()
  # print_ships(cpu_ships)

  place_ships(cpu_board, cpu_ships)
import random

# TODO: Remove print()s

class ShipOffBoardError(Exception):
  pass


class CollisionError(Exception):
  pass


class InvalidInputError(Exception):
  pass


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
      print('{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(*([str(i+1).rjust(2)] + row + [str(i+1).rjust(2)])))
    print('  +-------------------+')
    print('   A B C D E F G H I J')

  def random_coord(self):
    row_index = random.choice(range(len(self.contents)))
    row = self.contents[row_index]
    column_index = random.choice(range(len(row)))
    return (row_index, row, column_index)

  def randomly_place_ship(self, ship):
    try:
      # Randomly choose where to start placing ship and its orientation
      (start_row_index, start_row, start_column_index) = self.random_coord()
      orientation = Ship.random_orientation()
      ship_coords = [(start_column_index, start_row_index)]
      current_row_index, current_column_index = (start_row_index, start_column_index)
      for x in ['s'] * (ship.size - 1):
        if orientation == 'north-south':
          current_column_index += 1
        else:
          current_row_index    += 1

        # Make sure that the next co-ord for the ship does not fall off the board
        if (current_column_index < (self.width - 1)) and (current_row_index < (self.height - 1)):
          # Current co-ord is on the board, so continue
          ship_coords.append((current_column_index, current_row_index))
        else:
          # Current co-ord is off the board, so we need to start again
          raise ShipOffBoardError("Current co-ord ({},{}) is OFF the board! We need to try again.".format(current_column_index, current_row_index))

      for coord in ship_coords:
        x, y = coord
        if self.contents[x][y] == 's':
          raise CollisionError("There's already a ship at ({},{})".format(x,y))
        self.contents[x][y] = 's' # Place this co-ord for the ship

    except (ShipOffBoardError, CollisionError) as e:
      self.randomly_place_ship(ship) # Try placing again

  def mark_hit(self, coords):
    x, y = coords
    self.contents[y][x] = 'X'

  def get_coords(self, coords):
    x, y = coords
    return self.contents[y][x]

class Battleships:
  def col_to_index(self, col):
    return "ABCDEFGHIJ".find(col)

  def validate_aim(self, aim):
    if len(aim) != 2:
      raise InvalidInputError()
    x, y = self.aim_to_coords(aim)
    if not ((x >= 0 and x <= 9) and (y >= 0 and y <= 9)):
      raise InvalidInputError()

  def aim_to_coords(self, aim):
    x, y = list(aim)
    x = self.col_to_index(x)
    y = int(y) - 1
    return (x, y)

  def request_aim_coords(self):
    try:
      aim = input("Please enter co-ordinates where to fire: ").upper()
      self.validate_aim(aim)
      return self.aim_to_coords(aim)
    except InvalidInputError:
      print('Please enter valid co-ordinates')
      return self.request_aim_coords()

  def fire(self, board, coords):
    if board.get_coords(coords) == 's':
      return 'hit'
    elif board.get_coords(coords) == 'X':
      return 'already hit'
    else:
      return 'miss'

  def play():
    game = Battleships()

    cpu_board = Board()
    cpu_ships = [
      Carrier(),
      Battleship(),
      Destroyer(),
      Submarine(), Submarine(),
      PatrolBoat(), PatrolBoat(),
    ]
    for ship in cpu_ships:
      cpu_board.randomly_place_ship(ship)

    print("CPU board:")
    cpu_board.print()

    print("\nReady to play!")

    ships_remaining = True

    while ships_remaining:
      aim_coords = game.request_aim_coords()
      shot_result = game.fire(cpu_board, aim_coords)
      if shot_result == 'hit':
        print("It's a hit!")
        cpu_board.mark_hit(aim_coords)
      elif shot_result == 'already hit':
        print("You've already hit there.")
      else:
        print("You missed.")
      print('\n')

      print("CPU board:")
      cpu_board.print()
      print("\n")


if __name__ == "__main__":
  Battleships.play()

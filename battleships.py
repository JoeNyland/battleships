from ships import Battleship, Carrier, Destroyer, PatrolBoat, Submarine
from errors import InvalidInputError
from boards import Board


class Battleships:
    @staticmethod
    def col_to_index(col):
        return "ABCDEFGHIJ".find(col)

    @staticmethod
    def index_to_col(index):
        return "ABCDEFGHIJ"[index]

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
        return x, y

    def coords_to_aim(self, coords):
        x, y = coords
        col = self.index_to_col(x)
        row = y + 1
        return "{}{}".format(col, row)

    def request_aim_coords(self):
        try:
            aim = input("Please enter co-ordinates where to fire: ").upper()
            self.validate_aim(aim)
            return self.aim_to_coords(aim)
        except InvalidInputError:
            print('Please enter valid co-ordinates')
            return self.request_aim_coords()

    @staticmethod
    def fire(board, coords):
        if board.get_coords(coords) == 's':
            return 'hit'
        elif board.get_coords(coords) == 'X':
            return 'already hit'
        else:
            return 'miss'

    @staticmethod
    def play():
        game = Battleships()

        cpu_board = Board()
        cpu_ships = [
            Carrier(),  # 5 long
            Battleship(),  # 4 long
            Destroyer(),  # 3 long
            Submarine(), Submarine(),  # 3 long
            PatrolBoat(), PatrolBoat(),  # 2 long
        ]
        for ship in cpu_ships:
            cpu_board.randomly_place_ship(ship)

        player_board = Board()
        player_ships = [
            Carrier(),  # 5 long
            Battleship(),  # 4 long
            Destroyer(),  # 3 long
            Submarine(), Submarine(),  # 3 long
            PatrolBoat(), PatrolBoat(),  # 2 long
        ]
        for ship in player_ships:
            player_board.randomly_place_ship(ship)

        print("Your board:")
        player_board.print()

        print("Ready to play!")

        ships_remaining = True
        next_turn = 'player'

        while ships_remaining:
            if next_turn == 'player':
                aim_coords = game.request_aim_coords()
                shot_result = game.fire(cpu_board, aim_coords)
                print('\n')
                if shot_result == 'hit':
                    print("It's a hit!")
                    cpu_board.mark_hit(aim_coords)
                elif shot_result == 'already hit':
                    print("You've already hit there.")
                else:
                    print("You missed.")
                next_turn = 'cpu'

                if cpu_board.hit_points == 0:
                    print('You won!')
                    ships_remaining = False
                print('\n')
            else:
                aim_coords = player_board.random_coords()
                print("CPU fires at {}!".format(game.coords_to_aim(aim_coords)))
                shot_result = game.fire(player_board, aim_coords)
                print('\n')
                if shot_result == 'hit':
                    print("The CPU hit one of your ships!")
                    player_board.mark_hit(aim_coords)
                else:
                    print("The CPU missed.")
                next_turn = 'player'

                if player_board.hit_points == 0:
                    print('You lost!')
                    ships_remaining = False
                else:
                    print('\n')
                    print("Player board:")
                    player_board.print()
                print('\n')
        print('GAME OVER')


if __name__ == "__main__":
    Battleships.play()

from random import choice as random_choice


def random_orientation():
    return random_choice(['north-south', 'east-west'])


class Ship:
    def __str__(self):
        if hasattr(self, 'size'):
            return '<' + ('=' * (self.size - 1))


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

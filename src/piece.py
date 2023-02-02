import math


class Piece:

    def __init__ (self, name, color, value, icon=None, icon_rect = None):
        self.name = name
        self.color = color

        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.icon = icon
        self.set_icon()
        self.icon_rect = icon_rect

    def set_icon(self):
        pass

class Pawn(Piece):

    def __init__(self, color):

        if color == 'white':
                self.dir = -1
        else:
                self.dir = 1

        super().__init__('pawn', color, 1.0)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, math.inf)
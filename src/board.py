from const import *
from square import Square

class Board:

    def __init__ (self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for file in range (FILE)]

        self._create()

    def _create (self):
        for rank in range(RANK):
            for file in range(FILE):
                self.squares[rank][file] = Square(rank, file)

    def _add_pieces (self, color):
        pass

import pygame
from piece import Piece

class Pawn(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Pawn'
        self.location = location
        self.has_moved = False
        if self.color == 'white':
            self.direction = -1
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_pawn.png')
            
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_pawn.png')
            self.direction = 1
        self.setPosition(location)

    # def hasMoved(self):
    #     self.has_moved = True

    #calculate if move is valid
    def get_valid_moves(self, start, board):
        valid_moves = []

        if self.color == "black":
            if start[0] > 0:
                if start[0] < 6:
                    self.has_moved = True
                # move one up
                if board[start[0] - 1][start[1]].getPiece() is None:
                    valid_moves.append((start[0] - 1, start[1]))
                # move two up on first move
                if not self.has_moved and board[start[0] - 1][start[1]].getPiece() is None and board[start[0] - 2][start[1]].getPiece() is None:
                    valid_moves.append((start[0] - 2, start[1]))
                # capture diagonally to the left
                if start[1] > 0 and board[start[0] - 1][start[1] - 1].getPiece() is not None and board[start[0] - 1][start[1] - 1].getPiece().color == "white":
                    valid_moves.append((start[0] - 1, start[1] - 1))
                # capture diagonally to the right
                if start[1] < 7 and board[start[0] - 1][start[1] + 1].getPiece() is not None and board[start[0] - 1][start[1] + 1].getPiece().color == "white":
                    valid_moves.append((start[0] - 1, start[1] + 1))

        elif self.color == "white":
            if start[0] < 7:
                if start[0] > 1:
                    self.has_moved = True
                # move one down
                if board[start[0] + 1][start[1]].getPiece() is None:
                    valid_moves.append((start[0] + 1, start[1]))
                # move two down on first move
                if not self.has_moved and board[start[0] + 1][start[1]].getPiece() is None and board[start[0] + 2][start[1]].getPiece() is None:
                    valid_moves.append((start[0] + 2, start[1]))
                # capture diagonally to the left
                if start[1] > 0 and board[start[0] + 1][start[1] - 1].getPiece() is not None and board[start[0] + 1][start[1] - 1].getPiece().color == "black":
                    valid_moves.append((start[0] + 1, start[1] - 1))
                # capture diagonally to the right
                if start[1] < 7 and board[start[0] + 1][start[1] + 1].getPiece() is not None and board[start[0] + 1][start[1] + 1].getPiece().color == "black":
                    valid_moves.append((start[0] + 1, start[1] + 1))

        return valid_moves
        
    # def isValidMove(self, move, valid_moves):
    #     valid_move = False
    #     for valid_move in valid_moves:
    #         if move == valid_move:
    #             valid_move = True
    #             return valid_move


class Rook(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Rook'
        self.location = location
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_rook.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_rook.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        pass

class Knight(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Knight'
        self.location = location
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_knight.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_knight.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        pass

class Bishop(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Bishop'
        self.location = location
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_bishop.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_bishop.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        pass

class King(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'King'
        self.location = location
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_king.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_king.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        pass

class Queen(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Queen'
        self.location = location
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_queen.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_queen.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        pass
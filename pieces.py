import pygame
from piece import Piece
from constants import *
import math


class Pawn(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Pawn'
        self.location = location
        self.has_moved = False
        self.value = 1
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_pawn.png')
            
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_pawn.png')
        self.setPosition(location)

    #calculate if move is valid, checks side and self color
    
    def get_valid_moves(self, start, board, side):
        valid_moves = []

        if self.color == "black" and side == "black":
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

        elif self.color == "black" and side == "white":
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
                if start[1] > 0 and board[start[0] + 1][start[1] - 1].getPiece() is not None and board[start[0] + 1][start[1] - 1].getPiece().color == "white":
                    valid_moves.append((start[0] + 1, start[1] - 1))
                # capture diagonally to the right
                if start[1] < 7 and board[start[0] + 1][start[1] + 1].getPiece() is not None and board[start[0] + 1][start[1] + 1].getPiece().color == "white":
                    valid_moves.append((start[0] + 1, start[1] + 1))

        elif self.color == "white" and side == "white":
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
                if start[1] > 0 and board[start[0] - 1][start[1] - 1].getPiece() is not None and board[start[0] - 1][start[1] - 1].getPiece().color == "black":
                    valid_moves.append((start[0] - 1, start[1] - 1))
                # capture diagonally to the right
                if start[1] < 7 and board[start[0] - 1][start[1] + 1].getPiece() is not None and board[start[0] - 1][start[1] + 1].getPiece().color == "black":
                    valid_moves.append((start[0] - 1, start[1] + 1))

        elif self.color == "white" and side == "black":
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
        


class Rook(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Rook'
        self.has_moved = False
        self.location = location
        self.value = 5.1
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_rook.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_rook.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        valid_moves = []

        if self.color == "black":

            #loop to check up movement
            for row in range(start[0] -1, -1, -1):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "white":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for down movement
            for row in range(start[0] +1, 8):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "white":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for left movement
            for col in range(start[1] -1, -1, -1):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "white":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            #loop for left movement
            for col in range(start[1] +1, 8):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "white":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))


        if self.color == "white":

            #loop to check up movement
            for row in range(start[0] -1, -1, -1):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "black":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for down movement
            for row in range(start[0] +1, 8):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "black":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for left movement
            for col in range(start[1] -1, -1, -1):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "black":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            #loop for left movement
            for col in range(start[1] +1, 8):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "black":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

        return valid_moves

class Knight(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Knight'
        self.location = location
        self.value = 3.2
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_knight.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_knight.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        valid_moves = []
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        if self.color == "white":

            for direction in directions:
                row = start[0] + direction[0]
                col = start[1] + direction[1]
                if 0 <= row < 8 and 0 <= col < 8:
                    if board[row][col].getPiece() is None:
                        valid_moves.append((row, col))
                    elif board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
        
        if self.color == "black":
            
            for direction in directions:
                row = start[0] + direction[0]
                col = start[1] + direction[1]
                if 0 <= row < 8 and 0 <= col < 8:
                    if board[row][col].getPiece() is None:
                        valid_moves.append((row, col))
                    elif board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))

        return valid_moves

class Bishop(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Bishop'
        self.location = location
        self.value = 3.33
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_bishop.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_bishop.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        valid_moves = []

        if self.color == "black":

            # loop to check up left
            row, col = start[0] - 1, start[1] - 1
            while row >= 0 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col -= 1

            # loop to check up right
            row, col = start[0] - 1, start[1] + 1
            while row >= 0 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col += 1

            # loop to check down left
            row, col = start[0] + 1, start[1] - 1
            while row < 8 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col -= 1

            # loop to check down right
            row, col = start[0] + 1, start[1] + 1 #maybe make +1?
            while row < 8 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col += 1

        if self.color == "white":

            # loop to check up left
            row, col = start[0] - 1, start[1] - 1
            while row >= 0 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col -= 1

            # loop to check up right
            row, col = start[0] - 1, start[1] + 1
            while row >= 0 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col += 1

            # loop to check down left
            row, col = start[0] + 1, start[1] - 1
            while row < 8 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col -= 1

            # loop to check down right
            row, col = start[0] + 1, start[1] + 1 #yes definitely +1?
            while row < 8 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col += 1

        return valid_moves

class King(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'King'
        self.has_moved = False
        self.location = location
        self.value = math.inf
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_king.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_king.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        valid_moves = []
        
        if self.color == "black":

            #loop to check up down left right
            for row in range(start[0] - 1, start[0] + 2):
                for col in range(start[1] - 1, start[1] + 2):
                    if (row >= 0 and row <= 7 and col >= 0 and col <= 7 and
                            (row, col) != start and
                            (board[row][col].getPiece() is None or
                            board[row][col].getPiece().color == "white")):
                        valid_moves.append((row, col))

        if self.color == "white":

            #loop to check up down left right
            for row in range(start[0] - 1, start[0] + 2):
                for col in range(start[1] - 1, start[1] + 2):
                    if (row >= 0 and row <= 7 and col >= 0 and col <= 7 and
                            (row, col) != start and
                            (board[row][col].getPiece() is None or
                            board[row][col].getPiece().color == "black")):
                        valid_moves.append((row, col))

        return valid_moves
            

class Queen(Piece):
    def __init__(self, color, location):
        super().__init__(color, location)
        self.color = color
        self.image = None
        self.type = 'Queen'
        self.location = location
        self.value = 8.8
        if self.color == 'white':
            self.image = pygame.image.load('assets\\images\\imgs-80px\\white_queen.png')
        else:
            self.image = pygame.image.load('assets\\images\\imgs-80px\\black_queen.png')
        self.setPosition(location)

    def get_valid_moves(self, start, board):
        valid_moves = []

        if self.color == "black":

            #loop to check up movement
            for row in range(start[0] -1, -1, -1):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "white":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for down movement
            for row in range(start[0] +1, 8):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "white":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for left movement
            for col in range(start[1] -1, -1, -1):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "white":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            #loop for left movement
            for col in range(start[1] +1, 8):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "white":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            # loop to check up left
            row, col = start[0] - 1, start[1] - 1
            while row >= 0 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col -= 1

            # loop to check up right
            row, col = start[0] - 1, start[1] + 1
            while row >= 0 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col += 1

            # loop to check down left
            row, col = start[0] + 1, start[1] - 1
            while row < 8 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col -= 1

            # loop to check down right
            row, col = start[0] + 1, start[1] + 1 #maybe make +1?
            while row < 8 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "white":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col += 1


        if self.color == "white":

            #loop to check up movement
            for row in range(start[0] -1, -1, -1):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "black":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for down movement
            for row in range(start[0] +1, 8):
                if board[row][start[1]].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[row][start[1]].getPiece().color == "black":
                        valid_moves.append((row, start[1]))
                    break
                valid_moves.append((row, start[1]))

            #loop for left movement
            for col in range(start[1] -1, -1, -1):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "black":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            #loop for left movement
            for col in range(start[1] +1, 8):
                if board[start[0]][col].getPiece() is not None:
                    #if enemy allow for valid and block
                    if board[start[0]][col].getPiece().color == "black":
                        valid_moves.append((start[0], col))
                    break
                valid_moves.append((start[0], col))

            # loop to check up left
            row, col = start[0] - 1, start[1] - 1
            while row >= 0 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col -= 1

            # loop to check up right
            row, col = start[0] - 1, start[1] + 1
            while row >= 0 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row -= 1
                col += 1

            # loop to check down left
            row, col = start[0] + 1, start[1] - 1
            while row < 8 and col >= 0:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col -= 1

            # loop to check down right
            row, col = start[0] + 1, start[1] + 1 #yes definitely +1?
            while row < 8 and col < 8:
                if board[row][col].getPiece() is not None:
                    if board[row][col].getPiece().color == "black":
                        valid_moves.append((row, col))
                    break
                valid_moves.append((row, col))
                row += 1
                col += 1

        return valid_moves
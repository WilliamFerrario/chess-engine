import pygame
from constants import *

class Squares:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.rect = pygame.Rect(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

    def __repr__(self):
        return f"({self.row}, {self.col})"
    
    def isEmpty(self):
        return self.piece is None
    
    def setPiece(self, piece):
        self.piece = piece

    def getPiece(self):
        return self.piece
    
    def removePiece(self):
        self.piece = None

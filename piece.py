import sys
import pygame
import math

class Piece:
    
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.rect = None
        self.square = None

    def __repr__(self):
        return self.color + ' ' + self.type

    def get_valid_moves(self, board):
        pass

    def setPosition(self, pos):
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos

    
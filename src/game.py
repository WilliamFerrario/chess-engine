import pygame
from const import *

class Game:
    
    def __init__(self):
        pass

    def show_board(self, surface):
        for rank in range(RANK):
            for file in range(FILE):
                if (rank + file) % 2 == 0:
                    color = (238, 238, 210) #green
                else:
                    color = (118, 150, 86) #white

                rectangle = (rank * SQUARE_SIZE, file * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(surface, color, rectangle)
import pygame
import sys

from constants import *
from board import Board
from piece import *

class Main:

    #Initialize Pygame
    pygame.init()

    #Window 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    #Loop 
    running = True

    #Paint board
    square_color1 = (173,189,143)
    square_color2 = (111,143,114)

    board = Board()
    board.blitBoard(screen)
    


    while running:

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                board.handleEvent(event)
        #update display
        board.blitBoard(screen)
        pygame.display.update()

    pygame.quit()
    
main = Main()

import pygame

from constants import *
from board import *
import engine as eng
from piece import *
from squares import *

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

    #instantiate board obj
    board = Board()
    board.blitBoard(screen)

    #set depth
    depth = board.depth
    
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

        if not (board.isCheckMate("white")) and not (board.isCheckMate("black")):

            if (board.engineColor == "white" and board.player == "white"):
                print("thinking")
                engine = eng.Engine(board, depth, "white")
                bestmove = engine.getBestMove()
                board.move(bestmove[0], bestmove[1])
                board.player = "black"
                
            elif (board.engineColor == "black" and board.player == "black"):
                print("thinking")
                engine = eng.Engine(board, depth, "black")
                bestmove = engine.getBestMove()
                board.move(bestmove[0], bestmove[1])
                board.player = "white" 

    pygame.quit()
    
main = Main()

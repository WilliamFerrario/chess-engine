import pygame
import sys

from constants import *

class Main:

    #Initialize Pygame
    pygame.init()

    #Window Initialize
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    #Loop while running
    running = True

    #Paint board
    square_color1 = (173,189,143)
    square_color2 = (111,143,114)

    for row in range (ROWS):
        for col in range (COLS):
            if (row + col) % 2 == 0:
                color = (square_color1)
            else:
                color = (square_color2)

            rect = pygame.Rect(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(screen, color, rect)


    while running:

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #update display
        pygame.display.update()

    pygame.quit()
    
main = Main()

import pygame

#Screen Dimensions
WIDTH = 800
HEIGHT = 800

#Board Dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS

#Paint Board
SQUARE_COLOR1 = (173,189,143)
SQUARE_COLOR2 = (111,143,114)

#Piece Icons
piece_icons = {
    'whitePawn': pygame.image.load('assets\\images\\imgs-80px\\white_pawn.png'),
    'whiteKnight': pygame.image.load('assets\\images\\imgs-80px\\white_knight.png'),
    'whiteBishop': pygame.image.load('assets\\images\\imgs-80px\\white_bishop.png'),
    'whiteRook': pygame.image.load('assets\\images\\imgs-80px\\white_rook.png'),
    'whiteQueen': pygame.image.load('assets\\images\\imgs-80px\\white_queen.png'),
    'whiteKing': pygame.image.load('assets\\images\\imgs-80px\\white_king.png'),
    'blackPawn': pygame.image.load('assets\\images\\imgs-80px\\black_pawn.png'),
    'blackKnight': pygame.image.load('assets\\images\\imgs-80px\\black_knight.png'),
    'blackBishop': pygame.image.load('assets\\images\\imgs-80px\\black_bishop.png'),
    'blackRook': pygame.image.load('assets\\images\\imgs-80px\\black_rook.png'),
    'blackQueen': pygame.image.load('assets\\images\\imgs-80px\\black_queen.png'),
    'blackKing': pygame.image.load('assets\\images\\imgs-80px\\black_king.png')
}
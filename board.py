import pygame
from pieces import *
from constants import *
import sys
from squares import *

class Board:
    def __init__(self):
        self.board = [[Squares(row, col) for col in range(COLS)] for row in range(ROWS)]

        self.makePiece()
        self.selectedPiece = None
        self.dragging = False
        self.square = None
        self.valid_moves = []

    #dragging methods
    def getSquare(self, pos):

        if pos[0] < 0 or pos[0] > WIDTH or pos[1] < 0 or pos[1] > HEIGHT:
            return None

        col = pos[0] // SQSIZE
        row = pos[1] // SQSIZE
        return (row, col)
    
    #offset for icon appearing in middle of square
    def getSquareCenter(self, square):
        x = (square[1] * SQSIZE) + SQSIZE // 2
        y = (square[0] * SQSIZE) + SQSIZE // 2
        return (x, y)
    

    def isValidMove(self, move, valid_moves):
        valid_move = False
        for valid_move in valid_moves:
            if move == valid_move:
                valid_move = True
                return valid_move
    
    #event handling
    def handleEvent(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #clicking / dragging event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            square = self.getSquare(mousePos)

            start_piece = self.board[square[0]][square[1]].getPiece()
            #maybe get piece instead or isempty

            if start_piece is not None:
                piece = self.board[square[0]][square[1]].getPiece()
                if piece is not None:
                    self.selectedPiece = start_piece
                    self.startPiecePos = mousePos
                    self.dragging = True
                    self.valid_moves = piece.get_valid_moves(square, self.board)
                    print(self.valid_moves)



        #when mouse button released
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging:
                mousePos1 = pygame.mouse.get_pos()
                square = self.getSquare(self.startPiecePos)
                square1 = self.getSquare(mousePos1)
                self.end_piece = self.board[square1[0]][square1[1]].getPiece()

                #self.move_piece(square, square1, mousePos1)
                print(square1)

                if self.end_piece is None or self.end_piece.color != self.selectedPiece.color:
                    if self.isValidMove(square1, self.valid_moves):
                        self.move_piece(square, square1, mousePos1)

                self.selectedPiece = None
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mousePos = pygame.mouse.get_pos()
            self.selectedPiecePos = mousePos

    def move_piece(self, start_square, end_square, end_pos):
        
        print(start_square, end_square)
        start_piece = self.board[start_square[0]][start_square[1]].getPiece() #maybe change to getrow n col or just sqyare
        end_piece = self.board[end_square[0]][end_square[1]].getPiece()
        
        if start_piece is None or (end_piece is not None and hasattr(end_piece, 'color') and end_piece.color == start_piece.color):
            return


        if end_piece is not None and end_piece.color != start_piece.color:
            self.board[end_square[0]][end_square[1]].setPiece(None)



        self.board[end_square[0]][end_square[1]].setPiece(start_piece)
        self.board[start_square[0]][start_square[1]].setPiece(None)
        self.selectedPiecePos = end_pos
        self.selectedPiece.rect.center = end_pos


    def makePiece(self):
        #white starting pieces
        self.board[0][0].setPiece(Rook("white", (0, 0)))
        self.board[0][1].setPiece(Knight("white", (0, 1)))
        self.board[0][2].setPiece(Bishop("white", (0, 2)))
        self.board[0][3].setPiece(Queen("white", (0, 3)))
        self.board[0][4].setPiece(King("white", (0, 4)))
        self.board[0][5].setPiece(Bishop("white", (0, 5)))
        self.board[0][6].setPiece(Knight("white", (0, 6)))
        self.board[0][7].setPiece(Rook("white", (0, 7)))

        for col in range(COLS):
            self.board[1][col].setPiece(Pawn("white", (1, col)))

        #black starting pieces
        self.board[7][0].setPiece(Rook("black", (7, 0)))
        self.board[7][1].setPiece(Knight("black", (7, 1)))
        self.board[7][2].setPiece(Bishop("black", (7, 2)))
        self.board[7][3].setPiece(Queen("black", (7, 3)))
        self.board[7][4].setPiece(King("black", (7, 4)))
        self.board[7][5].setPiece(Bishop("black", (7, 5)))
        self.board[7][6].setPiece(Knight("black", (7, 6)))
        self.board[7][7].setPiece(Rook("black", (7, 7)))

        for col in range(COLS):
            self.board[6][col].setPiece(Pawn("black", (6, col)))
            

    #draw board
    def blitBoard(self, screen):
        for row in range(ROWS):
            for col in range (COLS):
                if (row + col) % 2 == 0:
                    color = SQUARE_COLOR1
                else:
                    color = SQUARE_COLOR2
                
                rect = pygame.Rect(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(screen, color, rect)

                #blit stagnant pieces and not moving piece
                piece = self.board[row][col]
                if piece is not None and piece.getPiece() is not None and not (self.dragging and piece.getPiece() == self.selectedPiece):
                    img = piece_icons[piece.getPiece().color + piece.getPiece().type]
                    icon_size = img.get_size()
                    x_pos = rect.centerx - icon_size[0] / 2
                    y_pos = rect.centery - icon_size[1] / 2
                    screen.blit(img, (x_pos, y_pos))

        
        if self.selectedPiece and self.dragging:
            mousePos = pygame.mouse.get_pos()
            img = piece_icons[self.selectedPiece.color + self.selectedPiece.type]
            icon_size = img.get_size()
            x_pos = mousePos[0] - icon_size[0] / 2
            y_pos = mousePos[1] - icon_size[1] / 2
            screen.blit(img, (x_pos, y_pos))

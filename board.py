import pygame
from pieces import *
from constants import *
import sys
from squares import *
#import engine as eng

class Board:
    def __init__(self):
        self.board = [[Squares(row, col) for col in range(COLS)] for row in range(ROWS)]

        self.makePiece2()
        self.selectedPiece = None
        self.dragging = False
        self.square = None
        self.valid_moves = []
        self.legal_moves = []
        self.player = "white"
        self.side = "white"
        self.engineColor = "black"
        self.movesNum = 0
        self.boardList = []
        
        self.depth = 3

    def getMovesNum(self):
        return self.movesNum

    #dragging methods
    def getSquare(self, pos):

        if pos[0] < 0 or pos[0] > WIDTH or pos[1] < 0 or pos[1] > HEIGHT:
            return None

        col = pos[0] // SQSIZE
        row = pos[1] // SQSIZE
        return (row, col)
    
    def getSquareFromCoord(self, row, col):
        square = self.board[row][col]
        return square

    def getSquareObj(self, row, col):
        square = self.board[row][col]
        piece = square.getPiece()
        return piece
    
    #offset for icon appearing in middle of square
    def getSquareCenter(self, square):
        x = (square[1] * SQSIZE) + SQSIZE // 2
        y = (square[0] * SQSIZE) + SQSIZE // 2
        return (x, y)
    
    #check move list from get_valid_moves
    def isValidMove(self, move, valid_moves):
        valid_move = False
        for valid_move in valid_moves:
            if move == valid_move:
                valid_move = True
                return valid_move
            
    def getAllMoves(self, color):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board[row][col]
                piece = square.getPiece()

                if isinstance(piece, Pawn) and piece is not None and piece.color == color:
                    valid_moves = piece.get_valid_moves((row, col), self.board, self.side)
                    for move in valid_moves:
                        if not self.isCheckAfterMove((row, col), move):
                            moves.append(((row, col), move))

                elif piece is not None and piece.color == color:
                    valid_moves = piece.get_valid_moves((row, col), self.board)
                    for move in valid_moves:
                        if not self.isCheckAfterMove((row, col), move):
                            moves.append(((row, col), move))
        return moves


    #is player in check
    def isCheck(self, player):
        for row in self.board:
            for square in row:
                piece = square.getPiece()
                if isinstance(piece, King) and piece.color == player:
                    king_square = square.getPos()

        if player == "black":
            enemy = "white"
        else:
            enemy = "black"
        
        for row in self.board:
            for square in row:
                piece = square.getPiece()
                if piece is not None and piece.color == enemy and not isinstance(piece, Pawn):
                    valid_moves = piece.get_valid_moves(square.getPos(), self.board)
                    if king_square in valid_moves:
                        return True
                #if pawn add side to VM funct
                if piece is not None and piece.color == enemy and isinstance(piece, Pawn):
                    valid_moves = piece.get_valid_moves(square.getPos(), self.board, self.side)
                    if king_square in valid_moves:
                        return True
        return False
    
    def isCheckAfterMove(self, start_square, end_square):
        # move the piece
        start_piece = self.board[start_square[0]][start_square[1]].getPiece()
        end_piece = self.board[end_square[0]][end_square[1]].getPiece()

        if start_piece is None:
            return False

        self.board[end_square[0]][end_square[1]].setPiece(start_piece)
        self.board[start_square[0]][start_square[1]].setPiece(None)

        # check if the move puts the player in check
        result = self.isCheck(start_piece.color)

        # undo the move
        self.board[start_square[0]][start_square[1]].setPiece(start_piece)
        self.board[end_square[0]][end_square[1]].setPiece(end_piece)

        return result

    #is player in mate
    def isCheckMate(self, player):
        if not self.isCheck(player):
            return False
        
        king_square = None
        # find king
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col].getPiece()
                if isinstance(piece, King) and piece.color == player:
                    king_square = (row, col)
                    break
            if king_square is not None:
                break

        if king_square is None:
            # no king
            return True

        # check if move -> get out of check
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col].getPiece()
                if piece is not None and piece.color == player:
                    if isinstance(piece, Pawn):
                        valid_moves = piece.get_valid_moves((row, col), self.board, self.side)
                    else:
                        valid_moves = piece.get_valid_moves((row, col), self.board)
                    
                    for move in valid_moves:
                        if not self.isCheckAfterMove((row, col), move):
                            # move that can get king out of check
                            return False
                        
        # no move found to get out of check, game over
        return True

    
    #event handling
    def handleEvent(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                self.depth = 1

            if event.key == pygame.K_2:
                self.depth = 2
            
            if event.key == pygame.K_3:
                self.depth = 3
            
            if event.key == pygame.K_4:
                self.depth = 4

            print ("Depth is set to ", self.depth)

            if event.key == pygame.K_r:
                self.reset()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:

                if self.side == "black":
                    self.side = "white"
                    self.engineColor = "black"
                else:
                    self.side = "black"
                    self.engineColor = "white"

                self.reset()
                if self.side == "white":
                    self.makePiece2()
                if self.side == "black":
                    self.makePiece()

        #clicking / dragging event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePos = pygame.mouse.get_pos()
            square = self.getSquare(mousePos)

            start_piece = self.board[square[0]][square[1]].getPiece()
            #maybe get piece instead or isempty

            if start_piece is not None and start_piece.color == self.player:
                piece = self.board[square[0]][square[1]].getPiece()
                if piece is not None:
                    self.selectedPiece = start_piece
                    self.startPiecePos = mousePos
                    self.dragging = True
                    if isinstance(piece, Pawn):
                        self.valid_moves = piece.get_valid_moves(square, self.board, self.side)
                        return
                    self.valid_moves = piece.get_valid_moves(square, self.board)
                    #print(self.valid_moves)
                    



        #when mouse button released
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging:
                mousePos1 = pygame.mouse.get_pos()
                square = self.getSquare(self.startPiecePos)
                square1 = self.getSquare(mousePos1)
                self.end_piece = self.board[square1[0]][square1[1]].getPiece()

                if self.end_piece is None or self.end_piece.color != self.selectedPiece.color:
                    if self.isValidMove(square1, self.valid_moves) and not self.isCheckAfterMove(square, square1):
                        self.move_piece(square, square1, mousePos1)

                self.selectedPiece = None
                self.dragging = False

                # if self.isValidMove(square1, self.valid_moves) and not self.isCheckAfterMove(square, square1):
                #     self.move_piece(square, square1, mousePos1)
                #     #self.engine.makeMove()
                #     #allow engine to move after human

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mousePos = pygame.mouse.get_pos()
            self.selectedPiecePos = mousePos
            

    def move_piece(self, start_square, end_square, end_pos):
        
        #print(start_square, end_square)
        start_piece = self.board[start_square[0]][start_square[1]].getPiece() #maybe change to getrow n col or just sqyare
        end_piece = self.board[end_square[0]][end_square[1]].getPiece()
        
        if start_piece is None or (end_piece is not None and hasattr(end_piece, 'color') and end_piece.color == start_piece.color):
            return

        if end_piece is not None and end_piece.color != start_piece.color:
            self.board[end_square[0]][end_square[1]].setPiece(None)

        if isinstance(start_piece, Pawn) and (end_square[0] == 0 or end_square[0] == 7):
            #promotion
            self.board[end_square[0]][end_square[1]].setPiece(Queen(start_piece.color, end_square))
        else:
            self.board[end_square[0]][end_square[1]].setPiece(start_piece)
        
        self.board[start_square[0]][start_square[1]].setPiece(None)
        self.selectedPiecePos = end_pos
        self.selectedPiece.rect.center = end_pos

        self.movesNum += 1

        # Switch the player
        if self.player == "white":
            self.player = "black"
        else:
            self.player = "white"

        if self.isCheck(self.player):
            print(f"{self.player} is in check!")

        if self.isCheckMate(self.player):
            print(f"{self.player} is in checkmate!")

    #this move method is for AI only
    def move(self, start_square, end_square):

        start_piece = self.board[start_square[0]][start_square[1]].getPiece()
        end_piece = self.board[end_square[0]][end_square[1]].getPiece()
        self.board[end_square[0]][end_square[1]].setPiece(start_piece)
        self.board[start_square[0]][start_square[1]].setPiece(None)

        self.movesNum += 1

        # Switch the player
        # if self.player == "white":
        #     self.player = "black"
        # else:
        #     self.player = "white"




    def reset(self):
            for row in range(ROWS):
                for col in range(COLS):
                    self.board[row][col].setPiece(None)
            self.makePiece2()
            self.player = "white"
            self.boardList = []

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

    def makePiece2(self):
        #white starting pieces
        self.board[0][0].setPiece(Rook("black", (0, 0)))
        self.board[0][1].setPiece(Knight("black", (0, 1)))
        self.board[0][2].setPiece(Bishop("black", (0, 2)))
        self.board[0][3].setPiece(Queen("black", (0, 3)))
        self.board[0][4].setPiece(King("black", (0, 4)))
        self.board[0][5].setPiece(Bishop("black", (0, 5)))
        self.board[0][6].setPiece(Knight("black", (0, 6)))
        self.board[0][7].setPiece(Rook("black", (0, 7)))

        for col in range(COLS):
            self.board[1][col].setPiece(Pawn("black", (1, col)))

        #black starting pieces
        self.board[7][0].setPiece(Rook("white", (7, 0)))
        self.board[7][1].setPiece(Knight("white", (7, 1)))
        self.board[7][2].setPiece(Bishop("white", (7, 2)))
        self.board[7][3].setPiece(Queen("white", (7, 3)))
        self.board[7][4].setPiece(King("white", (7, 4)))
        self.board[7][5].setPiece(Bishop("white", (7, 5)))
        self.board[7][6].setPiece(Knight("white", (7, 6)))
        self.board[7][7].setPiece(Rook("white", (7, 7)))

        for col in range(COLS):
            self.board[6][col].setPiece(Pawn("white", (6, col)))
            

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

            #blit circle before piece
            if self.valid_moves:
                for move in self.valid_moves:
                    row, col = move
                    if row == move[0] and col == move[1]:
                        center = self.getSquareCenter(move)
                        pygame.draw.circle(screen, (128, 128, 128, 128), center, 15)

            screen.blit(img, (x_pos, y_pos))
            
            
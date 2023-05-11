from board import *
from squares import *
import math
import random as rand
from piece import Piece

class Engine:

    def __init__(self, board, maxDepth, color):
        
        self.board = board
        self.maxDepth = maxDepth
        self.color = color
        self.boardList = []

    def evaluation(self):
        count = 0
        for i in range(8):
            for o in range(8):
                count += self.squarePoints(i, o)
        count += self.potentialMate() + self.opening() + 0.001 * rand.random()
        # random FLOAT between 0 and 1 is better for AB pruning... dont ask why
        return count

    def getBestMove(self):
        return self.engine(None, 1)

    #building eval function
    def potentialMate(self):
        #if no legal moves
        if (len(self.board.getAllMoves(self.board.engineColor)) == 0):
            if (self.board.engineColor == self.color):
                #engine is mated
                return -math.inf
            else:
                #engine beats human :(
                return math.inf
        else:
            return 0
        

    def opening(self):
        #number of full moves since the start of game
        if (self.board.getMovesNum() < 15):
            if (self.board.engineColor == self.color):
                return 1/30 * len(self.board.getAllMoves(self.board.engineColor))
            else:
                return -1/30 * len(self.board.getAllMoves(self.board.engineColor))
        else:
            return 0

    #takes a square as input and returns the hb's
    #system value of its resident
    def squarePoints(self, row, col):

        pieceValue = 0
        piece = self.board.getSquareObj(row, col)
        if isinstance(piece, Pawn):
            pieceValue = 1
        if isinstance(piece, Knight):
            pieceValue = 3.2
        if isinstance(piece, Bishop):
            pieceValue = 3.33
        if isinstance(piece, Rook):
            pieceValue = 5.1
        if isinstance(piece, Queen):
            pieceValue = 8.8

        if piece and piece.color != self.color:
            return -pieceValue
        else:
            return pieceValue

    #recursion function for the engine
    def engine(self, candidate, depth):
        
        #if reach 0 legal moves then end in decision tree
        if (depth == self.maxDepth or len(self.board.getAllMoves(self.board.engineColor)) == 0):
            return self.evaluation() #evaluates and returns val
        
        else:
            #get legal moves from current pos
            moveList = list(self.board.getAllMoves(self.board.engineColor))

            #init new candidate
            possibleCandidate = None

            #recursive param to give info on where best candidate is while minimaxing for children nodes
            if (depth % 2 != 0):
                possibleCandidate = float(-math.inf)
            else:
                possibleCandidate = float(math.inf)

            for i in moveList:
                #play the move i
                self.boardList.append(i)

                #get the value of move i
                value = self.engine(possibleCandidate, depth + 1)

                #if maximizing (engine's turn)
                #if maximizing we change candidate to neighboring nodes
                if(value > possibleCandidate and depth % 2 != 0):
                    #change candidate
                    possibleCandidate = value
                    if (depth == 1):
                        move = i
                    possibleCandidate = value
                
                #if minimizing (human turn)
                #inverse of maximizing func... obviously
                elif(value < possibleCandidate and depth % 2 == 0):
                    #change candidate
                    possibleCandidate = value
                    #not saving move since players turn

                #AB pruning deletions case I
                #if prev move was made by engine)
                if (candidate != None and value < candidate and depth % 2 == 0):
                    self.boardList.pop() #remove last move on board
                    break

                #AB pruning deletions case II
                #if prev move was human )
                elif (candidate != None and value > candidate and depth % 2 != 0):
                    self.boardList.pop() #remove last move on board
                    break
                    
                #undo last move again
                self.boardList.pop()

        if (depth > 1):
            #return value of the node in the tree
            return possibleCandidate
        else:
            #return the move itself
            #print (move)
            return move
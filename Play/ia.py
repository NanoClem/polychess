# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:52:38 2018

@author: dupouyj
"""

import chess
import chess.polyglot
import chess.svg
from IPython.display import SVG,display
import random




class IA:
    def __init__(self, board):
        self.board=board
        
    def legal_moves(self):
        return self.board.legal_moves
    
    def best_move(self):
        moves=[]
        #access the Polyglot book
        with chess.polyglot.open_reader("bookfish.bin") as reader:
            for entry in reader.find_all(self.board):
                moves.append([entry.move(), entry.weight])
        
        if moves ==[]:
            return False
        #find the maximum weight
        j=0
        weight=0
        for i in range(len(moves)):
            if moves[i][1] > weight :
                weight=moves[i][1]
                j=i
        return moves[j][0]


    def do_the_best_move(self):
        book = chess.polyglot.open_reader("bookfish.bin")
        main_entry = book.find(self.board)
        move=main_entry.move()
    
        #display the move
        #print(move)
    
        #do the move
        self.board.push(move)
    
        #display the board
        print(self.board)
        board
    
        #do we have a winner?
        if (self.board.is_game_over()):
            print("The game is over")
            print(self.board.result())
        
        return move
    
    def move_weight(self):
        book = chess.polyglot.open_reader("bookfish.bin")
        board = self.board
        main_entry = book.find(board)
        #print(main_entry.move())
        book.close()
        return main_entry.weight

        


    def play(self):
        display(SVG(chess.svg.board(board=self.board)))

        while not(self.board.is_game_over()):
            #moves = self.legal_moves()
    
            if self.best_move()==False:
                moves=[]
                for move in self.legal_moves():
                    moves.append(move)
                #choose a move        
                rand_int = random.randint(0,len(moves)-1)
                #line.append(moves[rand_int])
                self.board.push(moves[rand_int])
                display(SVG(chess.svg.board(board=self.board, lastmove = moves[rand_int])))            
                print(moves[rand_int],"\n")

            else:
                moveToPlay = self.best_move()
                #line.append(moveToPlay)
                self.board.push(moveToPlay)
                display(SVG(chess.svg.board(board=self.board, lastmove = moveToPlay)))            
                print(moveToPlay,"\n")
    
     
        #Now the game is over, show the results
        print("The game is over")
        print(self.board.result())
        #game.headers["Result"]=board.result()
    
    

# =============================================================================
# Tests
# =============================================================================

if __name__ == "__main__" :
    board=chess.Board()
    game=IA(board)
    print(game.play())

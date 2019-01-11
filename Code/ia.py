# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:52:38 2018

@author: dupouyj
"""

import chess
import chess.polyglot

class IA:
    def __init__(self, board):
        self.board=board
        
    def legal_moves(self):
        return self.board.legal_moves
    
    def best_moves(self):
        pass
        #access the Polyglot book
        with chess.polyglot.open_reader("bookfish.bin") as reader:
            for entry in reader.find_all(self.board):
                return entry.move()



    def do_the_best_move(self):
        book = chess.polyglot.open_reader("bookfish.bin")
        main_entry = book.find(self.board)
        move=main_entry.move()
    
        #display the move
        print(move)
    
        #do the move
        self.board.push(move)
    
        #display the board
        print(self.board)
        board
    
        #do we have a winner?
        if (self.board.is_game_over()):
            print("The game is over")
            print(self.board.result())
        


    def play(self):
        while self.board.is_game_over==False:
            self.do_the_best_move()
# =============================================================================
# Tests
# =============================================================================

board=chess.Board()
game=IA(board)

game.do_the_best_move()

game.do_the_best_move()

#print("\n legal moves", game.legal_moves(),"\n")
#print("best move",game.best_moves())

# -*- coding: utf-8 -*-

"""

Created on Fri Jan 11 08:23:02 2019



@author: nasric

"""



import chess
import chess.svg
import chess.pgn
from IPython.display import SVG,display
import chess.polyglot




#
#board = chess.Board()
#squares = board.attacks(chess.E4)
#
#
#line = []
#game=chess.pgn.Game()
#SVG(chess.svg.board(board = board, squares = squares, coordinates=True, size = 400))

class PvP:
    def __init__(self, board):
        self.board=board
        
    def best_move(self):
        coups=[]
        with chess.polyglot.open_reader("bookfish.bin") as reader:
            for entry in reader.find_all(self.board):
                coups.append([entry.move(), entry.weight, entry.learn])
    
            p = 0
            i = 0
            for i in range (len(coups)):
                if coups[i][1] > p :
                    i = i
                    p = coups[i][1]
            if coups ==[]:
                return "Nothing"
            else:
                return coups[i][0]
    
    def playPvP (self):
        display(SVG(chess.svg.board(board=self.board)))
        
        while (self.board.is_game_over() == False):
                moves = self.board.legal_moves
                p_move =chess.Move.from_uci(input("Move: "))
                            
                if p_move in moves :
                    self.board.push(p_move)
                    #line.append(p_move)
                    display(SVG(chess.svg.board(board=self.board, lastmove = p_move)))            
    
                else:
                    while p_move not in moves :
                        print("Mouvement impossible, choisir un autre")
                        print("Liste des mouvements possibles")
                        for move in self.board.legal_moves:
                            print(move)
                        p_move =chess.Move.from_uci(input("Move : "))
                    self.board.push(p_move)
                    #line.append(p_move)
                    display(SVG(chess.svg.board(board=self.board, lastmove = p_move)))                            
    
    
    
        print("The game is over")
        print(self.board.result())
        #game.headers["Result"]=board.result()

        

#### Lancement de la partie ####
if __name__ == "__main__" :
    board = chess.Board()
    game=PvP(board)
    print(game.playPvP())

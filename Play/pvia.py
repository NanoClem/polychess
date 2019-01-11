# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:05:20 2019

@author: nasric
"""

import chess
import chess.svg
import chess.pgn
from IPython.display import SVG,display
import chess.polyglot
import random

#def game_tag_info ():
#    game.headers["Event"]=input("Event : ")
#    game.headers["Site"]=input("Site : ")
#    game.headers["Date"]=datetime.datetime.now()
#    game.headers["Round"]=input("Rounde : ")
#    game.headers["White"]=input("Player 1 : WHITE : ")
#    game.headers["Black"]=input("Player 2 : BLACK : ")
#    
#board = chess.Board()
#squares = board.attacks(chess.E4)
#
#line = []
#game=chess.pgn.Game()
#
#SVG(chess.svg.board(board = board, squares = squares, coordinates=True, size = 400))
#
#


class PvE:
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
    
    
    
    
    def playPvE (self):

        display(SVG(chess.svg.board(board=self.board)))
        
        while (self.board.is_game_over() == False):
                moves = self.board.legal_moves
                
                p_move =chess.Move.from_uci(input("Move : "))
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
                        p_move =chess.Move.from_uci(input("départ arrivée : "))
                    self.board.push(p_move)
                    game.add_vard5dtion(p_move)
                    display(SVG(chess.svg.board(board=self.board, lastmove = p_move)))            
                        
                #Test if game is over
                if self.board.is_game_over():
                    game.headers["Result"]=self.board.result()
                    print("The game is over")
                    return self.board.result()                
                    
                    
                #IA turn
                moves = self.board.legal_moves
                if self.best_move() == "Nothing" :
                    list_move=[]
                    for move in moves:
                            list_move.append(move)        
                    rand_int = random.randint(0,len(list_move)-1)
                    #line.append(list_move[rand_int])
                    self.board.push(list_move[rand_int])
                    display(SVG(chess.svg.board(board=self.board, lastmove = list_move[rand_int])))            
                    print("")
                elif self.best_move() in moves:
                    moveToPush = self.best_move()
                    #♠line.append(moveToPush)
                    self.board.push(moveToPush)
                    display(SVG(chess.svg.board(board=self.board, lastmove = moveToPush)))            
                    print("")      
                    

        print("The game is over")
        return board.result()
                

            
     
        
#### Lancement de la partie ####
if __name__ == "__main__" :
    board = chess.Board()
    game=PvE(board)
    print(game.playPvE())
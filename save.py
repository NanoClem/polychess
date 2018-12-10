# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:41:21 2018

@author: dupouyj
"""

import chess
import chess.pgn

class Save:
    def __init__(self, board):
        self.game=chess.pgn.Game()
        self.board=board
    
    def get_headers(self):
        return self.game.headers
    
    def fill_headers(self, values=[None,None,None,None,None,None,None]) :
        '''
            la fonction modifie les headers
            :param values: 'Nom du tournoi', 'Lieu', 'Date', 'Round', 'Nom des blancs', 'Nom des noirs', 'Resultat'
        '''
        labels = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        i=0
        for header in labels :
            if values[i]!=None:
                self.get_headers()[header] = values[i]
            i=i+1







# =============================================================================
# Tests
# =============================================================================

board=chess.Board()
jeu=Save(board)
print("Type du header :", type(jeu.get_headers()))
jeu.fill_headers()
#print(jeu.get_headers())
print(jeu.game)
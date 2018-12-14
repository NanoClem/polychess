# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:41:21 2018

@author: dupouyj
"""

import chess
import chess.pgn

class Save:
    """
    Cette classe permet la sauvegarde des parties
    sous format PGN et aussi l'ecriture dans un fichier txt
    """
    
    

    def __init__(self, board):
        """
        Constructeur
        :param board: tableau contenant la partie en cours
        """
        self.game  = chess.pgn.Game()
        self.board = board
    
    
    
    def get_headers(self):
        """
        Retourne les headers de la partie
        :return: liste des headers de la partie
        """
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

    def save_the_game(self):
        '''
            La fonction enregistre une partie sous format pgn dans un fichier texte
            :param: game
        '''
        new_pgn=open("games_saved.txt","w",encoding="utf-8")
        exporter=chess.pgn.FileExporter(new_pgn)
        self.game.accept(exporter)
        





# =============================================================================
# Tests
# =============================================================================

board=chess.Board()
jeu=Save(board)
print("Type du header :", type(jeu.get_headers()))
jeu.fill_headers(["Tournoi test",None,None,None,None,None,None])
#print(jeu.get_headers())
print(jeu.game)
jeu.save_the_game()
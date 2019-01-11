# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:41:21 2018

@author: dupouyj decoopman
"""

import chess
import chess.pgn


class Save:
    """
    Cette classe permet la sauvegarde dans un fichier txt :
        - des parties sous format PGN
        - des postions du tableau sous format FEN
    """
    
    

    def __init__(self, board):
        """
        Constructeur
        :param board: tableau contenant la partie en cours
        """
        self.game  = chess.pgn.Game()   #partie sous format PGN
        self.fen   = board.fen()        #positions du tableau sous format FEN
        self.board = board
    
    
    
    def getHeaders(self):
        """
        Retourne les headers de la partie
        :return: liste des headers de la partie
        """
        return self.game.headers
    
    
    
    def getFEN(self) :
        """
        Retourne les positions du tableau
        sous format FEN
        """
        return self.fen
    
    
    
    def fill_headers(self, values=[None,None,None,None,None,None,None]) :
        '''
        la fonction modifie les headers
        :param values: 'Nom du tournoi', 'Lieu', 'Date', 'Round', 'Nom des blancs', 'Nom des noirs', 'Resultat'
        '''
        labels = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        i=0
        for header in labels :
            if values[i] != None:
                self.getHeaders()[header] = values[i]
            i=i+1



    def save_the_game(self):
        '''
        La fonction enregistre une partie sous format pgn dans un fichier texte
        :param: game
        '''
        new_pgn  = open("games_saved.txt","w",encoding="utf-8")
        exporter = chess.pgn.FileExporter(new_pgn)
        self.game.accept(exporter)
        new_pgn.close()
        
        
        
    def save_fen(self) :
        """
        Enregistre dans un fichier les positions 
        courrante du tableau sous format FEN \n
        Les positions seront alignées
        """
        filename = "fen_save.txt"
        fen_file = open(filename, "a")      # ouverture du fichier en mode "append"
        fen_file.write(self.fen + "\n")     # ecriture du FEN courrant dans le fichier txt
        fen_file.close()                    # fermeture du fichier txt
        
        





# =============================================================================
# Tests
# =============================================================================
if __name__ == "__main__" :
    
    board = chess.Board()
    jeu = Save(board)
    jeu.fill_headers(["Tournoi test",None,None,None,None,None,None])
    
    print("Affichage de la partie PGN :")
    print(jeu.game)
    print("Affichage des positions FEN :")
    print(jeu.getFEN())
    
    jeu.save_the_game()
    jeu.save_fen()
    
    
    
    
    
    
    
    
    
    
    
    
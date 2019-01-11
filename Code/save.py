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
        
    Elle permet egalement de produire un board depuis une FEN enregistree dans un fichier
    """
    
    

    def __init__(self):
        """
        Constructeur
        :param board: tableau contenant la partie en cours
        """
        self.board = None       # tableau de jeu
        self.game  = None       # partie sous format PGN
        self.fen   = None       # positions du tableau sous format FEN
        
        
        
    def setBoard(self, new_board) :
        """
        Setter du tableau de jeu
        :param new_board: nouveau tableau de jeu
        """
        self.board = new_board
        self.game  = chess.pgn.Game()   
        self.fen   = board.fen()
        
        
    
    def setFEN(self, new_fen) :
        """
        Setter de FEN
        :param new_fen: nouveau FEN
        """
        self.fen = new_fen
        
    
    
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



    def save_the_game(self, filename):
        '''
        La fonction enregistre une partie sous format pgn dans un fichier texte
        :param: game
        '''
        new_pgn  = open(filename,"w",encoding="utf-8")
        exporter = chess.pgn.FileExporter(new_pgn)
        self.game.accept(exporter)
        new_pgn.close()
        
        
        
    def save_fen(self, filename) :
        """
        Enregistre dans un fichier les positions 
        courrante du tableau sous format FEN \n
        Les positions seront alignées
        """
        with open(filename, "a") as f :      # ouverture du fichier en mode "append"
            f.write(self.fen + "\n")         # ecriture du FEN courrant dans le fichier txt
            
    
    
    def read_fen(self, filename) :
        """
        Recupere la derniere FEN de la partie depuis le fichier de sauvegare 
        et retourne le tableau correspondant
        :param filename: nom du fichier de sauvegarde
        :return: tableau de jeu correspondant
        """
        fen = ""
        with open(filename, "r") as f :
            for line in f :
                fen = line
                
        return chess.Board(fen)
                
        


# =============================================================================
# Tests
# =============================================================================
if __name__ == "__main__" :
    
    # FICHIERS
    fen_file  = "fen_save.txt"
    game_file = "games_saved.txt"
    
    # BOARD
    board = chess.Board()
    jeu = Save()
    jeu.setBoard(board)
    jeu.fill_headers(["Tournoi test",None,None,None,None,None,None])
    
    # AFFICHAGES
    print("Affichage de la partie PGN :")
    print(jeu.game)
    print("Affichage des positions FEN :")
    print(jeu.getFEN())
    
    # SAUVEGARDE / LECTURE
    jeu.save_the_game(game_file)
    jeu.save_fen(fen_file)
    print(jeu.read_fen(fen_file))
    
    
    
    
    
    
    
    
    
    
    
    
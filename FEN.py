# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:37:21 2018

@author: Clément
"""

import chess


class FEN :
    """
    Cette classe permet l'evaluation et l'affichage
    d'une FEN pour un tableau donne
    """
    
    def __init__(self, board) :
        """
        Constructeur
        :param board: 
        """
        self.fen   = board.fen()
        self.board = board
        
        
        
    def evaluate(self):
        """
        Verifie depuis le FEN : 
            - les positions des pion
            - la prise en passant
            - le roque
        """
        pass
        
    
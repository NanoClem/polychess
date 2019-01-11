# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:02:47 2019

@author: dupouyj
"""

from ia import IA
from pvp import PvP
from pvia import PvE
from save import Save
import datetime
import chess
import chess.polyglot
import chess.svg





if __name__ == "__main__" :
    board=chess.Board()
    #choix du mode de jeu
    a=eval(input("Choose your game mode (1 : IA, 2 : PlayerVSPlayer, 3 : PlayerVSIA) :"))
    
    #info sur la partie
    jeu = Save(board)
    jeu.fill_headers([str(input("Event : ")),str(input("Site : ")),datetime.datetime.now(),str(input("Round : ")),str(input("White : ")),str(input("Black : ")),None])

    
    #IA
    if a==1:
        game=IA(board)
        print(game.play())
    
    #Player VS Player
    elif a==2:
        game=PvP(board)
        print(game.playPvP())
    
    #Player VS IA
    elif a==3:
        game=PvE(board)
        print(game.playPvE())
    
    else:
        print("Choose an other game mode")
    
    if board.is_game_over():
        jeu.fill_headers([None,None,None,None,None,None,board.result()])
        jeu.save_the_game()
    
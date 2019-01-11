# PolyChess

PolyChess (named polychess as Git repository) is a Chess engine written in Python. 

Polychess is able to :

* Play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess


## New techniques/skills/terms to get acquainted with

* Chess (maybe)
* Universal Chess Interface (UCI) (http://wbec-ridderkerk.nl/html/UCIProtocol.html)
* Portable General Notation (PGN)
* Board representation (bitboards, 0x88, 120-square representation, 64-square representation)
* MinMax (Negamax)
* Alpha-Beta pruning
* Chess rules (five fold repetition, seventy-five moves)
* Opening book (Polyglot)
* Forsyth-Edwards Notation (FEN) (https://www.chessprogramming.org/Forsyth-Edwards_Notation)
* Piece-Square table
* Move ordering
* Position evaluation
* Transposition table


## DevTeam

Project Manager : Clement DECOOPMAN.
Developpers     : Chiheb NASRI, Juliette DUPOUY, Mohamed COUIBALY.


## How to use it


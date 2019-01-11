#python-chess import
#https://github.com/niklasf/python-chess
import chess
import chess.svg
from IPython.display import SVG
import chess.polyglot
from save import Save



def save_current(save, filename, board) :
    """
    Sauvegarde des donnees du tableau courrant (FEN)
    """
    save.setBoard(board)
    save.save_fen(board.fen())




#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()
squares = board.attacks(chess.E4)


# print the board on the console
print(board)



#NOMS DE FICHIERS SAUVEGARDE
fen_file  = "fen_save.txt"
game_file = "games_saved.txt"

# SAUVEGARDE TABLEAU INITIAL
current_save = Save()                  #Sauvegarde courrante
save_current(current_save, fen_file, board)


#SVG render for the board is possible in Jupyter Notebook
#board
SVG(chess.svg.board(board = board, squares = squares, coordinates=True, size = 400))

#get all the legal moves for the current position
moves = board.legal_moves
print(moves)


#how many moves are available?
print(moves.count())




##iterate over all the moves
for move in moves: 
    book = chess.polyglot.open_reader("bookfish.bin")
    
    main_entry = book.find(board)
    a=main_entry.move()
    
    #display the move
    print("move",a)
    
    #do the move
    board.push(a)
    
    
    #save the current position
    current_board = board
    save_current(current_save, fen_file, current_board)
    
    #new fen and board
    print(current_board.fen())       # fen representation
    print(current_save.readFEN())    # new board
    
    
    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))
    
    
    
    #undo the move
    #board.pop()
    
    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
#        current_save.fill_headers()
#        current_save.save_the_game(game_file)
    



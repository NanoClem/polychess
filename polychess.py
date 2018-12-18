#python-chess import
#https://github.com/niklasf/python-chess
import chess
import chess.svg
from IPython.display import SVG
import chess.polyglot

#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()
squares = board.attacks(chess.E4)


#print the board on the console
print(board)

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
    
    #save the current position
    current_board = board
    
    #do the move
    board.push(a)
    
    #display the board
    print(board)
    
    
    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))
    
    #fen representation
    print(board.fen())
    
    #undo the move
    #board.pop()
    
    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
    



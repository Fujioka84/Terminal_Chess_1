import chess_board

red = "\033[1;31m"
blue = "\033[1;34m"
no_color = "\033[0m"

#class for pawns
#first move
#capture
#to queen
#en passante
class Pawn:
    def __init__(self, move):
        self.move = move

    def __repr__(self) -> str:
        return f"{blue}p{no_color}"

    def select_method(self):
        #checks which method to use based on move input
        if len(self.move) == 2:
            if self.move[0] + #call first move or move
            pass


    def first_move(self):
        if self.move == "white_pawn":
            origin = move[0] + str(2)
            destination = move
            if chess_board.current_board[chess_board.alphanum_key[origin]] != f"{blue}p{no_color}":
                return input("Not a legal move. Please enter a different move: ")
            else:
                chess_board.current_board[chess_board.alphanum_key[origin]] = chess_board.empty_square
                chess_board.current_board[chess_board.alphanum_key[destination]] = f"{blue}p{no_color}"
        else:
            origin = move[0] + str(7)
            destination = move
            if chess_board.current_board[chess_board.alphanum_key[origin]] != f"{red}p{no_color}":
                return input("Not a legal move. Please enter a different move: ")
            else:
                chess_board.current_board[chess_board.alphanum_key[origin]] = chess_board.empty_square
                chess_board.current_board[chess_board.alphanum_key[destination]] = f"{red}p{no_color}"

    def move(self, move):
        if self.pawn == "white_pawn":
            origin = move[0] + str(int(move[-1]) - 1)
            destination = move
            chess_board.current_board[chess_board.alphanum_key[origin]] = chess_board.empty_square
            chess_board.current_board[chess_board.alphanum_key[destination]] = f"{blue}p{no_color}"
        else:
            origin = move[0] + str(int(move[-1]) + 1) 
            destination = move
            chess_board.current_board[chess_board.alphanum_key[origin]] = chess_board.empty_square
            chess_board.current_board[chess_board.alphanum_key[destination]] = f"{red}p{no_color}"
    
    def check_legal(self, move):
        pass
import chess_board

red = "\033[1;31m"
blue = "\033[1;34m"
no_color = "\033[0m"

def request_blue():
    p1_input = input(f"{blue}BLUE MOVE: {no_color}")
    p1_move(p1_input)

def request_red():
    p2_input = input(f"{red}RED MOVE: {no_color}")
    p2_move(p2_input)

pawn_check = ["a", "b", "c", "d", "e", "f", "g", "h", "x"]

def p1_move(p1_input):
    if p1_input[0] in pawn_check:
        #code block for pawns
        pass
    elif p1_input[0] == "R":
        #code block for rook
        pass
    elif p1_input[0] == "B":
        #code block for bishop
        pass
    elif p1_input[0] == "N":
        #code block for night
        pass
    elif p1_input[0] == "Q":
        #code block for queen
        pass
    elif p1_input == "0-0":
        #code block for kingside castle
        pass
    elif p1_input == "0-0-0":
        #code block for queenside castle
        pass
    elif p1_input[0] == "K":
        #code block for king
        pass
    elif p1_input == "forfeit":
        #code block to end game
        pass
    else:
        print("Please enter proper chess notation")
        #code block to ask for move input
    #generate updated board
    #code block to check if game end
    #request_red()

def p2_move(p2_input):
    if p2_input[0] in pawn_check:
        #code block for pawns
        pass
    elif p2_input[0] == "R":
        #code block for rook
        pass
    elif p2_input[0] == "B":
        #code block for bishop
        pass
    elif p2_input[0] == "N":
        #code block for night
        pass
    elif p2_input[0] == "Q":
        #code block for queen
        pass
    elif p2_input == "0-0":
        #code block for kingside castle
        pass
    elif p2_input == "0-0-0":
        #code block for queenside castle
        pass
    elif p2_input[0] == "K":
        #code block for king
        pass
    elif p2_input == "forfeit":
        #code block to end game
        pass
    else:
        print("Please enter proper chess notation")
        #code block to ask for move input
    #code block to check if game end
    #request_blue()


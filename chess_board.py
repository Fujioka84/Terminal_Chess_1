# generate new board from player inputs

red = "\033[1;31m"
blue = "\033[1;34m"
green = '\033[92m'
no_color = "\033[0m"

def display(piece, color):
  return f"{color}{piece}{no_color}"

# white pieces
white_rook_1 = display("R", blue)
white_rook_2 = display("R", blue)
white_knight_1 = display("N", blue)
white_knight_2 = display("N", blue)
white_bishop_1 = display("B", blue)
white_bishop_2 = display("B", blue)
white_queen = display("Q", blue)
white_king = display("K", blue)
white_pawn = display("p", blue)

# black pieces
black_rook_1 = display("R", red)
black_rook_2 = display("R", red)
black_knight_1 = f"{red}N{no_color}"
black_knight_2 = f"{red}N{no_color}"
black_bishop_1 = f"{red}B{no_color}"
black_bishop_2 = f"{red}B{no_color}"
black_queen = f"{red}Q{no_color}"
black_king = f"{red}K{no_color}"
black_pawn = f"{red}p{no_color}"

# empty squares
empty_square = "x"

white_position = {1: white_rook_1, 2: white_knight_1, 3: white_bishop_1, 4: white_queen, 
                     5: white_king, 6: white_bishop_2, 7: white_knight_2, 8: white_rook_2,
                     9: white_pawn, 10: white_pawn, 11: white_pawn, 12: white_pawn,
                     13: white_pawn, 14: white_pawn, 15: white_pawn, 16: white_pawn}

empty_positions = {}
for i in range(32):
  empty_positions[i + 17] = empty_square

black_positions = {49: black_pawn, 50: black_pawn, 51: black_pawn, 52: black_pawn,
                     53: black_pawn, 54: black_pawn, 55: black_pawn, 56: black_pawn,
                     57: black_rook_1, 58: black_knight_1, 59: black_bishop_1, 60: black_queen,
                     61: black_king, 62: black_bishop_2, 63: black_knight_2, 64: black_rook_2}

current_board = {**white_position, **empty_positions, **black_positions}

alphanum_key = {"a1": 1, "b1": 2, "c1": 3, "d1": 4, "e1": 5, "f1": 6, "g1": 7, "h1": 8,
                "a2": 9, "b2": 10, "c2": 11, "d2": 12, "e2": 13, "f2": 14, "g2": 15, "h2": 16,
                "a3": 17, "b3": 18, "c3": 19, "d3": 20, "e3": 21, "f3": 22, "g3": 23, "h3": 24,
                "a4": 25, "b4": 26, "c4": 27, "d4": 28, "e4": 29, "f4": 30, "g4": 31, "h4": 32,
                "a5": 33, "b5": 34, "c5": 35, "d5": 36, "e5": 37, "f5": 38, "g5": 39, "h5": 40,
                "a6": 41, "b6": 42, "c6": 43, "d6": 44, "e6": 45, "f6": 46, "g6": 47, "h6": 48,
                "a7": 49, "b7": 50, "c7": 51, "d7": 52, "e7": 53, "f7": 54, "g7": 55, "h7": 56,
                "a8": 57, "b8": 58, "c8": 59, "d8": 60, "e8": 61, "f8": 62, "g8": 63, "h8": 64,}

alphanum_key_2 = {}
alpha_char = ["a", "b", "c", "d", "e", "f", "g", "h"]
for count in range(8):
  count_key = count + 1  
  for char in alpha_char:
    #num = alpha_char.index(char) + 1
    key = char + str(num)
    alphanum_key_2[key] = alpha_char.index(char) + 1

print(alphanum_key_2)

def generate_board():
    print(f"{green}   a b c d e f g h   {no_color}")                
    print("8  " + current_board[57] + " " + current_board[58] + " " + current_board[59] + " " + current_board[60] + " "
      + current_board[61] + " " + current_board[62] + " " + current_board[63] + " " + current_board[64] + "  8")
    print("7  " + current_board[49] + " " + current_board[50] + " " + current_board[51] + " " + current_board[52] + " "
      + current_board[53] + " " + current_board[54] + " " + current_board[55] + " " + current_board[56] + "  7")
    print("6  " + current_board[41] + " " + current_board[42] + " " + current_board[43] + " " + current_board[44] + " "
      + current_board[45] + " " + current_board[46] + " " + current_board[47] + " " + current_board[48] + "  6")
    print("5  " + current_board[33] + " " + current_board[34] + " " + current_board[35] + " " + current_board[36] + " "
      + current_board[37] + " " + current_board[38] + " " + current_board[39] + " " + current_board[40] + "  5")
    print("4  " + current_board[25] + " " + current_board[26] + " " + current_board[27] + " " + current_board[28] + " "
      + current_board[29] + " " + current_board[30] + " " + current_board[31] + " " + current_board[32] + "  4")
    print("3  " + current_board[17] + " " + current_board[18] + " " + current_board[19] + " " + current_board[20] + " "
      + current_board[21] + " " + current_board[22] + " " + current_board[23] + " " + current_board[24] + "  3")
    print("2  " + current_board[9] + " " + current_board[10] + " " + current_board[11] + " " + current_board[12] + " "
      + current_board[13] + " " + current_board[14] + " " + current_board[15] + " " + current_board[16] + "  2")
    print("1  " + current_board[1] + " " + current_board[2] + " " + current_board[3] + " " + current_board[4] + " "
      + current_board[5] + " " + current_board[6] + " " + current_board[7] + " " + current_board[8] + "  1")
    print(f"{green}   a b c d e f g h   {no_color}")

# def move_piece(p1_move):
#     if len(p1_move) == 2:
#         piece = white_pawn
#         destination = p1_move[-2:]
#     current_board[alphanum_key[destination]] = piece
#     #if int(p1_move[-1]) == 
#     current_board[alphanum_key[destination] - 8] = empty_square
#     generate_board()

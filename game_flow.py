import chess_board
import move_logic

# start game by assigning Player 1 and Player 2
print("Welcome to terminal chess. May the best player win.")
player_1 = input("Player 1: ")
player_2 = input("Player 2: ")
print("{player_1} will play as BLUE.\n{player_2} will play as RED.".format(player_1=player_1, player_2=player_2))

# generate board
chess_board.generate_board()

# player move input
move_logic.request_blue()

#comment
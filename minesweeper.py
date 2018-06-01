
from mine_classes import *

print("Select difficulty: ")
print("1) Easy")
print("2) Medium")
print("3) Hard")
print("Press <enter> to exit.")
difficulty = input(": ")
size = 0

if difficulty == "1":
    size = 5
elif difficulty == "2":
    size = 7
elif difficulty == "3":
    size = 10
else:
    exit()

board = Board(size)
print(board)

while True:
    if board.player_turn():
        print(board)

    else:
        print(board)
        break


#Create a game of Minesweeper
#Actors: Node, Board

#Node: Each Node is a position on the board.  Can be a mine, otherwise show number of mines next to itself.
#       Should keep track of how many mines next to itself.

#Board: Creates and displays the board.  Accepts and applies input from player.

import random

#Start of Node class
class Node:
    def __init__(self):
        self.is_mine = 0 #0 means not a mine, 1 means a mine
        self.adj_mines = 0
        self.is_showing = False

    def make_mine(self):
        self.is_mine = 1

    def make_showing(self):
        self.is_showing = True

    def __repr__(self):
        if self.is_showing:
            if self.is_mine == 1:
                return "M"
            else:
                return str(self.adj_mines)
        else:
            return "X"

#Start Board class
class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = []

        for row in range(self.size):
            row = []
            for col in range(self.size):
                new_node = Node()
                if random.random() > .80: #20% chance of node being a mine
                    new_node.make_mine()
                row.append(new_node)
            self.board.append(row)

        #Need to give all nodes how many adj mines
        board_size = self.size - 1

        for r_idx, row in enumerate(self.board):
            for c_idx, col in enumerate(row):
                right = (row[c_idx + 1]).is_mine if c_idx < board_size else 0
                left = (row[c_idx - 1]).is_mine if c_idx > 0 else 0
                above = (self.board[r_idx - 1][c_idx]).is_mine if r_idx > 0 else 0
                below = (self.board[r_idx + 1][c_idx]).is_mine if r_idx < board_size else 0

                top_left = (self.board[r_idx -1][c_idx - 1]).is_mine if r_idx > 0 and c_idx > 0 else 0
                top_right = (self.board[r_idx -1][c_idx + 1]).is_mine if r_idx > 0 and c_idx < board_size else 0
                bottom_left = (self.board[r_idx + 1][c_idx - 1]).is_mine if r_idx < board_size and c_idx > 0 else 0
                bottom_right = (self.board[r_idx + 1][c_idx + 1]).is_mine if r_idx < board_size and c_idx < board_size else 0

                count = right + left + above + below + top_left + top_right + bottom_left + bottom_right
                col.adj_mines = count

    def player_turn(self):
        while True:
            player_input = input("Please enter the row and column number you would like to select, separated by a space: ")
            player_input = player_input.split()
            row = int(player_input[0])
            col = int(player_input[1])
            if row >= 0 and row < self.size:
                if col >= 0 and col < self.size:
                    break
                else:
                    print("Invalid column number")
            else:
                print("Invalid row number")

        self.board[row][col].make_showing()

    def __str__(self):
        r_count = 0
        c_count = 0
        print("  ", end = "")

        for row in self.board:
            print(" " + str(c_count), end = "")
            c_count += 1

        print("")
        print("  ", end = "")

        for row in self.board:
            print("__", end = "")

        print("")

        for row in self.board:
            print(str(r_count) + "| ", end = "")
            for col in row:
                print(col, end = " ")
            print("")
            r_count += 1
        return ""

#Testing ======================

board = Board(5)
print(board)
board.player_turn()
print(board)


#Create a game of Minesweeper
#Actors: Node, Board

#Node: Each Node is a position on the board.  Can be a mine, otherwise show number of mines next to itself.
#       Should keep track of how many mines next to itself.

#Board: Creates and displays the board.  Accepts and applies input from player.

import random

#Start of Node class
class Node:
    def __init__(self):
        self.is_mine = False
        self.adj_mines = 0

    def make_mine(self):
        self.is_mine = True

    #Need way to count number of adjacent mines
    def count_adj_mines(self):
        pass

    def __repr__(self):
        if self.is_mine:
            return "X"
        else:
            return str(self.adj_mines)

#Start Board class
class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = []

        for row in range(self.size):
            row = []
            for col in range(self.size):
                new_node = Node()
                if random.random() > .80:
                    new_node.make_mine()
                row.append(new_node)
            self.board.append(row)

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
"""
    def __str__(self):
        for row in self.board:
            for col in row:
                print(col, end = " ")
            print("")
        return ""
"""
#Testing ======================

board = Board(5)
print(board)

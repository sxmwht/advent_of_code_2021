#!/usr/bin/env python3
import re

input_data = open("input.txt").read().splitlines()

called_numbers = input_data[0].split(",")

def transpose_grid(rows):
    columns = []
    for column in range(len(rows[0])):
        columns.append([])
        for row in range(len(rows)):
            columns[-1].append(rows[row][column])
    return columns


class bingo_board:
    def __init__(self, rows):
        self.rows = rows
        self.columns = transpose_grid(rows)

bingo_boards = []

temp_board = []
for line in input_data[2:]:
    if not line == "":
        print(line)

        new_line = re.sub(" (\d)[ $]", r"0\1 ", line)
        print(new_line)
        temp_board.append(new_line.split(" "))
        print(temp_board)

    else:
        bingo_boards.append(bingo_board(temp_board))
        temp_board = []

print(bingo_boards[0].rows)
print(bingo_boards[0].columns)

test_string = " 3"
print(re.sub(" \d$", "x", test_string))


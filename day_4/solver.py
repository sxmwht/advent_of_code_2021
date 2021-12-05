#!/usr/bin/env python3
import re

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
        self.mask = []
        for i in range(len(self.rows)):
            self.mask.append([1]*len(self.rows[0]))

def check_winner(board):
    for row in board.mask:
        if row == [0]*len(row):
            return True
    for col in transpose_grid(board.mask):
        if col == [0]*len(col):
            return True
    return False

def play_bingo(bingo_boards, called_numbers):
    for call in called_numbers:
        for board in bingo_boards:
            for row in board.rows:
                if call in row:
                    board.mask[board.rows.index(row)][row.index(call)] = 0
            if check_winner(board):
                winning_board = board
                return (winning_board, call)

def list_remove_and_return(list_, target):
    list_.remove(target)
    return list_

def main():
    input_data     = open("input.txt").read().splitlines()
    called_numbers = [int(i) for i in input_data[0].split(",")]
    bingo_boards   = []
    temp_board     = []

    for line in input_data[2:]:
        if not line == "":
            new_line = re.sub("  ", " ", line)
            new_line = re.sub("^ ", "0", new_line)
            temp_board.append([int(i) for i in new_line.split(" ")])
        else:
            bingo_boards.append(bingo_board(temp_board))
            temp_board = []

    # get the score of the first winning board
    result                = play_bingo(bingo_boards, called_numbers)
    winning_board         = result[0]
    winning_board_numbers = [n for row in winning_board.rows  for n in row ]
    winning_board_mask    = [m for mrow in winning_board.mask for m in mrow]
    last_called_number    = result[1]
    print(last_called_number * sum([winning_board_numbers[i] * winning_board_mask[i] for i in range(len(winning_board_numbers))]))

    # get the score of the last winning board (to let the squid win)
    while len(bingo_boards)>1:
        result = play_bingo(list_remove_and_return(bingo_boards, result[0]), called_numbers[called_numbers.index(result[1]):])
    winning_board         = result[0]
    winning_board_numbers = [n for row in winning_board.rows  for n in row ]
    winning_board_mask    = [m for mrow in winning_board.mask for m in mrow]
    last_called_number    = result[1]
    print(last_called_number * sum([winning_board_numbers[i] * winning_board_mask[i] for i in range(len(winning_board_numbers))]))

if __name__ == "__main__":
    main()

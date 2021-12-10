#!/usr/bin/env python

def transpose_grid(rows):
    columns = []
    for column in range(len(rows[0])):
        columns.append([])
        for row in range(len(rows)):
            columns[-1].append(rows[row][column])
    return columns

input_lines = open("input.txt").read().splitlines()
input_ = [list(map(int, list(l))) for l in input_lines]

min_points_h = []
for row, line in enumerate(input_):
    for i, point in enumerate(line):
        adjacent_points = list(set([*range(len(line))]).intersection([i-1, i+1]))
        if all([point < line[ap] for ap in adjacent_points]):
            min_points_h.append((row,i))

input_t = transpose_grid(input_)

min_points_v = []
for row, line in enumerate(input_t):
    for i, point in enumerate(line):
        adjacent_points = list(set([*range(len(line))]).intersection([i-1, i+1]))
        if all([point < line[ap] for ap in adjacent_points]):
            min_points_v.append((i,row))

# print the sum of all the (low points + 1)
print(sum([input_[row][col]+1 for row,col in 
    list(set(min_points_h).intersection(min_points_v))]))



#!/usr/bin/env python

def expand_line(line):
    line = [int(p) for v in line for p in v]
    x1,y1,x2,y2 = line
    x_range = [*range(x1,x2+1 if x2>x1 else x2-1, 1 if x2>x1 else -1)]
    y_range = [*range(y1,y2+1 if y2>y1 else y2-1, 1 if y2>y1 else -1)]
    if len(x_range) == 1:
        x_range = [x_range[0]]*len(y_range)
    if len(y_range) == 1:
        y_range = [y_range[0]]*len(x_range)
    return x_range, y_range

# parse input
lines = [tuple(([tuple((vertex.split(","))) for vertex in line.split(" -> ")])) 
        for line in open("input.txt").read().splitlines()]

# define size of grid
max_x = max([int(vertex[0]) for line in lines for vertex in line])+1
max_y = max([int(vertex[1]) for line in lines for vertex in line])+1

# create grid
grid = []
for i in range(max_y):
    grid.append([0]*max_x)

# find horz/vert lines
hv_lines = [line for line in lines if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1])]

# find diagonal lines
dg_lines = [line for line in lines if abs(int(line[0][0]) - int(line[1][0])) == abs(int(line[0][1]) - int(line[1][1]))]

# plot lines
for line in hv_lines:
    for x,y in zip(*expand_line(line)):
        grid[y][x] += 1

print(len([p for row in grid for p in row if p >= 2]))

for line in dg_lines:
    for x,y in zip(*expand_line(line)):
        grid[y][x] += 1

print(len([p for row in grid for p in row if p >= 2]))

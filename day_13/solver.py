#!/usr/bin/env python

def fold_y(lines, fold_line):
    for y in range(fold_line):
        print(len(lines))
        print(paper_w)
        lines[y] = [lines[y][x] | lines[-1][x] for x in range(len(lines[0]))]
        lines.pop()
    lines.pop()

def fold_x(lines, fold_line):
    for y in range(len(lines)):
        for x in range(fold_line):
            lines[y][x] = lines[y][x] | lines[y][-1]
            lines[y].pop()
        lines[y].pop()

def print_op(lines):
    for l in lines:
        print("".join(["█" if x else " " for x in l]))

points = [tuple(map(int,tuple(l.split(',')))) for l in open("input.txt").read().splitlines() if "fold" not in l and l != ""]
folds  = [l.split()[2].split('=') for l in open("input.txt").read().splitlines() if "fold" in l]

paper_w = max([p[0] for p in points])+1
paper_h = max([p[1] for p in points])+1

lines = []
for i in range(paper_h):
    lines.append([False]*paper_w)

for p in points:
    lines[p[1]][p[0]] = True

print_op(lines)

for f in folds:
    print(f)
    if f[0] == "x":
        fold_x(lines, int(f[1]))
    else:
        fold_y(lines, int(f[1]))

    print(len(lines), len(lines[0]))

print_op(lines)

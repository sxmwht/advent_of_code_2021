#!/usr/bin/env python

commands = [f.split(" ") for f in open("input.txt").read().splitlines()]

horizontal_total = 0
vertical_total   = 0
aim              = 0

for c in commands:
    if "forward" in c:
        horizontal_total += int(c[1])
        vertical_total += aim*int(c[1])
    elif "up" in c:
        aim -= int(c[1])
    elif "down" in c:
        aim += int(c[1])

print(aim)
print(vertical_total)
print(horizontal_total)
print(vertical_total*horizontal_total)

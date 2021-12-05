#!/usr/bin/env python

with open("input.txt") as data:
    depths = [int(i) for i in data.read().splitlines()]

count = 0
previous_moving_average = (depths[0] + depths[1] + depths[2])/3

for i in range(3, len(depths)):
    moving_average = (depths[i] + depths[i-1] + depths[i-2])/3
    if moving_average > previous_moving_average:
        count += 1
    previous_moving_average = moving_average

print(count)

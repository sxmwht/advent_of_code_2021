#!/usr/bin/env python

from aocd import numbers

data = open("input.txt").read().strip("\n")
data = list(map(int, data.split(",")))

fuel_per_position_simple   = []
fuel_per_position_advanced = []
for i in range(min(data), max(data)+1):
    fuel_used_simple   = 0
    fuel_used_advanced = 0
    for crab in data:
        fuel_used_simple   += abs(crab-i)
        fuel_used_advanced += abs(crab-i) * (abs(crab-i)+1)/2
    fuel_per_position_simple.append(fuel_used_simple)
    fuel_per_position_advanced.append(fuel_used_advanced)

print(min(fuel_per_position_simple))
print(min(fuel_per_position_advanced))

#!/usr/bin/env python

fish = list(map(int, [f for f in open("input.txt").read().split(",")]))

def calc_growth(fish, days):
    day_fish = []
    for f in range(9):
        day_fish.append(fish.count(f))
    for i in range(days):
        next_day_fish = day_fish[1:] + day_fish[:1]
        next_day_fish[6] += day_fish[0]
        day_fish = next_day_fish
    return sum(day_fish)

print(calc_growth(fish, 80))
print(calc_growth(fish, 256))

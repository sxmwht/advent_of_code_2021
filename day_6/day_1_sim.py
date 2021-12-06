#!/usr/bin/env python

fish = list(map(int, [f for f in open("input.txt").read().split(",")]))

def calc_growth(fish, days):
    for i in range(days):
        for f in range(fish.count(0)):
            fish.append(9)
        fish = list(map(lambda f : 6 if f == 0 else f - 1, fish))
    return len(fish)

print(calc_growth(fish, 80))
print(calc_growth(fish, 256))

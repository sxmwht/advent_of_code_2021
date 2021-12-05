#!/usr/bin/env python

g = int("".join(["1" if j >= 0 else "0" for j in [sum([1 if d[i] == "1" else -1 for d in [d for d in open("input.txt").read().splitlines()]]) for i in range(len([d for d in open("input.txt").read().splitlines()][0]))]]),2)
e = 0xfff ^ g
print(g*e)

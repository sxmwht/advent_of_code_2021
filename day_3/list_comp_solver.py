#!/usr/bin/env python

f = open("input.txt")
data = [d for d in f.read().splitlines()]

num_bits = len(data[0])
num_words = len(data)

g = int("".join([str(int(sum([int(d[i]) for d in data]) // (num_words/2))) for i in range(num_bits)]), 2)
e = 0xfff ^ g

print(g*e)

f.close()

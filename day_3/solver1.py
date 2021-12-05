#!/usr/bin/env python

f = open("input.txt")
data = [d for d in f.read().splitlines()]

g = 0

counts = [0]*12

for d in data:
    for i in range(len(d)):
        if d[i] == "0":
            counts[i] -= 1
        else:
            counts[i] += 1

print(counts)

g=int("".join([str(int(i>1)) for i in counts]),2)
print(g)
e = 0xfff ^ g

print(g*e)

f.close()

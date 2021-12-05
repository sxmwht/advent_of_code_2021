#!/usr/bin/env python

f = open("input.txt")
orig = [d for d in f.read().splitlines()]

def get_special_number(mode="oxygen"):
    data = orig.copy()
    bit = 0
    while len(data) > 1:
        counts=0

        for d in data:
            if d[bit] == "0":
                counts -= 1
            else:
                counts += 1

        if (counts >= 0):
            target = '1'
        else:
            target = '0'

        if (mode == "oxygen"):
            for i in range(len(data)):
                if data[i][bit] != target:
                    data[i] = "x"
        else:
            for i in range(len(data)):
                if data[i][bit] == target:
                    data[i] = "x"


        while "x" in data:
            data.remove("x")

        bit += 1

    return int(data[0], 2)

oxygen = get_special_number("oxygen")
co2    = get_special_number("co2")

print(oxygen)
print(co2)
print(oxygen * co2)

f.close()

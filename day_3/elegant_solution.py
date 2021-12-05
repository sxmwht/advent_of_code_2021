#!/usr/bin/env python3

def get_most_common_bit_at_index(list_, bits):
    num_words = len(list_)
    return [int(sum([int(d[i]) for d in list_]) // (num_words/2)) for i in bits]

def recursive_remove(list_, index, keep_most_common_bit):
    if len(list_) == 1:
        return list_
    else:
        b = get_most_common_bit_at_index(list_, [index])[0]
        new_list = [x for x in list_ if (x[index] == str(b)) ^ keep_most_common_bit]
        
        return recursive_remove(new_list, index+1, keep_most_common_bit)

with open("input.txt") as f:
    data = [d for d in f.read().splitlines()]

g = int("".join([str(x) for x in get_most_common_bit_at_index(data, [*range(len(data[0]))])]), 2)
e = 0xfff ^ g

print(g*e)

o = int(recursive_remove(data.copy(), 0, True)[0], 2)
c = int(recursive_remove(data.copy(), 0, False)[0], 2)
print(o*c)

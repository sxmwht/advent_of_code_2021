#!/usr/bin/env python

from collections import Counter

def count_all_pairs(string):
    list_of_pairs = []
    for i in range(len(string)-1):
        list_of_pairs.append(string[i]+string[i+1])
    c = Counter(list_of_pairs)
    return c

def part2_step(ctr, elem_ctr):
    c = ctr.copy()
    ec = elem_ctr.copy()
    for pair in ctr:
        poly_op = polymerisation[pair]
        c[pair] -= ctr[pair]
        c[pair[0]+poly_op] += ctr[pair]
        c[poly_op+pair[1]] += ctr[pair]
        ec[poly_op] += ctr[pair]

    return c, ec

def naive_loop(string):
    new_string = string.copy()
    chars_inserted = 0
    for i in range(len(string)-1):
        new_string.insert(i+1+chars_inserted, polymerisation[string[i]+string[i+1]])
        chars_inserted += 1
        # insert in the string at index = i+1 the result from looking up in the dict
    return new_string


if __name__ == "__main__":
    with open("input.txt") as ifile:
        polymerisation = dict([[l.split("->")[0].rstrip(), l.split("->")[1].lstrip()] for l in ifile.read().splitlines() if "->" in l])

        ifile.seek(0)
        string = list(ifile.read().splitlines()[0])

    p1_string = string.copy()
    p2_string = string.copy()

    # naive solution - actually run the loop (part 1)
    for s in range(10):
        p1_string = naive_loop(p1_string)

    cntr = Counter(p1_string)
    print(cntr.most_common()[0][1] - cntr.most_common()[-1][1])

    # part 2
    element_counter = Counter(p2_string)
    cntr = count_all_pairs(p2_string)
    for step in range(40):
        cntr, element_counter = part2_step(cntr, element_counter)

    print(element_counter.most_common()[0][1] - element_counter.most_common()[-1][1])


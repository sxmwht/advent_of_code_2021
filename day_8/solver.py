#!/usr/bin/env python

data          = open("input.txt").read().splitlines()
input_digits  = [d.split("|")[0].split() for d in data]
output_values = [d.split("|")[1].split() for d in data]

# how many 1s, 4s, 7s and 8s
print(len([d for line in output_values for d in line if len(d) in [2,3,4,7]]))

segments_for_each_digit = [0]*10

# what follows is the logic used to deduce each digit...
#
# a 1 is the only digit to have only 2 segments lit
# a 4 is the only digit to have only 4 segments lit
# a 7 is the only digit to have only 3 segments lit
# an 8 is the only digit to have all 7 segments lit
#
# there are 3 segments that have 5 segments lit (2, 3 and 5):
# - a 3 is the only digit that has 5 segments lit AND contains all the segments
#   that make up a 1. This leaves 5 and 2...
# - a 5 contains the segments that are in a 4 but not a 1
# - a 2 must be the remaining one
#
# there are 3 segments that have 6 segments lit (6, 9 and 0):
# - a 0 does NOT contain all the segments that are make up a 5 (6 and 9 do)
# - a 9 contains all the segments that make up a 4 (6 does not)
# - 6 must be left over
# 
# if we sort all the inputs and the outputs, we can do a straight compare to
# work out which digits are in the output

output = 0
for i, line in enumerate(input_digits):
    inputs = list(map(list, [d for d in line]))
    for d in inputs:
        d.sort()
    for digit in inputs:
        if len(digit) == 2:
            segments_for_each_digit[1] = digit
        if len(digit) == 3:
            segments_for_each_digit[7] = digit
        if len(digit) == 4:
            segments_for_each_digit[4] = digit
        if len(digit) == 7:
            segments_for_each_digit[8] = digit

    diff_4_to_1 = [seg for seg in segments_for_each_digit[4] if seg not in segments_for_each_digit[1]]
    for digit in [d for d in inputs if len(d) == 5]:
        if set(segments_for_each_digit[1]).issubset(set(digit)):
            segments_for_each_digit[3] = digit
        elif set(diff_4_to_1).issubset(set(digit)):
            segments_for_each_digit[5] = digit
        else:
            segments_for_each_digit[2] = digit
    for digit in [d for d in inputs if len(d) == 6]:
        if not set(segments_for_each_digit[5]).issubset(set(digit)):
            segments_for_each_digit[0] = digit
        elif set(segments_for_each_digit[4]).issubset(set(digit)):
            segments_for_each_digit[9] = digit
        else:
            segments_for_each_digit[6]  = digit

    outputs = list(map(list, [d for d in output_values[i]]))
    output_list = []
    for o in outputs:
        o.sort()
        output_list.append(segments_for_each_digit.index(o))
    output += int("".join(list(map(str, output_list))))

print(output)



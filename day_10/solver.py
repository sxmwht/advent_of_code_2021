#!/usr/bin/env python

data = open("input.txt").read().splitlines()

char_pairs = {
    '[':']',
    '<':'>',
    '{':'}',
    '(':')'
    }

corrupt_points = {
    ']':57,
    '>':25137,
    '}':1197,
    ')':3
    }

complete_points = {
        ')':1,
        ']':2,
        '}':3,
        '>':4
    }

class line:
    def __init__(self, content):
        self.content = content
        self.corrupt = False
        self.closing_chars = []

lines = []
score = 0
for l in data:
    lines.append(line(l))

for l in lines:
    for i, char in enumerate(l.content):
        if char in char_pairs.keys():
            l.closing_chars.append(char_pairs[char])
        elif char in char_pairs.values():
            if char != l.closing_chars[-1]:
                ##debug
                #print("Corrupt")
                #print(l.content, i)
                #marker = [' ']*len(l.content)
                #marker[i] = '^'
                #print("".join(marker))
                l.corrupt = True
                score += corrupt_points[char]
                break
            else:
                l.closing_chars.pop()

autocomplete_scores = []
for l in lines:
    autocomplete_score = 0
    if not l.corrupt:
        l.closing_chars.reverse()
        print(l.closing_chars)
        for char in l.closing_chars:
            autocomplete_score *= 5
            autocomplete_score += complete_points[char]
        autocomplete_scores.append(autocomplete_score)

autocomplete_scores.sort()

print(score)
print(autocomplete_scores[(len(autocomplete_scores)-1)//2])


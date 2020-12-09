
# --- Day 9: Encoding Error ---
#
#   Part 1: Find a number which is not possible as the sum of a moving window of 25 numbers
#   Part 2: Find a range of x prior numbers which can sum to that number
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(mode='int')

mydata = a.array

sample =\
"""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

lines = [int(x) for x in sample.split("\n") if x]

def part1(lines):
    index = 25
    alive = True
    while alive:
        preamble = lines[index-25:index]
        pmin = preamble.pop(preamble.index(min(preamble)))
        pmin2 = preamble.pop(preamble.index(min(preamble)))
        pmax = preamble.pop(preamble.index(max(preamble)))
        pmax2 = preamble.pop(preamble.index(max(preamble)))
        preamble = lines[index-25:index]
        if lines[index] > pmax + pmax2 or lines[index] < pmin + pmin2:
            print("Easy:", lines[index])
            alive = False
        index += 1


def part2(lines):
    index = 25
    alive = True
    processed = lines[index-25:index]
    invalid = -1
    while alive:
        preamble = lines[index-25:index]
        pmin = preamble.pop(preamble.index(min(preamble)))
        pmin2 = preamble.pop(preamble.index(min(preamble)))
        pmax = preamble.pop(preamble.index(max(preamble)))
        pmax2 = preamble.pop(preamble.index(max(preamble)))
        preamble = lines[index-25:index]
        if lines[index] > pmax + pmax2 or lines[index] < pmin + pmin2:
            print("Easy:", lines[index])
            invalid = lines[index]
            alive = False
            continue

        processed.append(lines[index])
        index += 1

    procindex = 0
    print(processed)
    found = False
    while not found:
        sum = 0
        weakness = []
        procoffset = 0
        while sum < invalid:
            try:
                sum += processed[procindex + procoffset]
                weakness.append(processed[procindex + procoffset])
                procoffset += 1
            except IndexError:
                break

        if sum == invalid:
            found = True
            print(min(weakness) + max(weakness))

        procindex += 1



part2(mydata)
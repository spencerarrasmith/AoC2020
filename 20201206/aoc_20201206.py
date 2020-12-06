
# --- Day 6: Custom Customs ---
#
#   Part 1: Count number of distinct answers per group
#   Part 2: Count number of distinct 'yes' answers from everyone in group
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(delimiter="\n\n")

mydata = a.array



sample =\
"""
abc

a
b
c

ab
ac

a
a
a
a

b
"""

def part1():
    groups = sample.split("\n\n")

    sum = 0
    for group in mydata:
        singleline = "".join(group.split("\n"))
        distinctletters = set()

        for ch in singleline:
            distinctletters.add(ch)

        sum += len(distinctletters)

    print("Answers: ", sum)


def part2():
    groups = sample.split("\n\n")

    sum = 0
    for group in mydata:
        grouplen = len([x for x in group.split("\n") if x])
        singleline = "".join(group.split("\n"))
        distinctletters = {}

        for ch in singleline:
            if ch in distinctletters.keys():
                distinctletters[ch] += 1
            else:
                distinctletters[ch] = 1

        for key in distinctletters.keys():
            if distinctletters[key] == grouplen:
                sum += 1

    print("Yes: ", sum)

part2()
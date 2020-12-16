
# --- Day 16: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(delimiter="\n\n")

mydata = a.array

sample =\
"""
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

sample2 =\
"""
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""

sample = [x for x in sample.split("\n\n") if x]

sample2 = [x for x in sample2.split("\n\n") if x]

def part1(lines):
    print("Error Rate:",sum([item for sublist in [[int(x) for x in y.split(',')] for y in lines[2].split("\n")[1:] if y] for item in sublist if item not in [item for sublist in {entry.split(":")[0]:[value for range in [[y for y in range(int(x.split('-')[0]),int(x.split('-')[1])+1)] for x in entry.split(":")[1].strip().split(" or ")] for value in range] for entry in [x for x in lines[0].split("\n")[1:] if x]}.values() for item in sublist]]))

def part2(lines):
    fields = {entry.split(":")[0]:[value for range in [[y for y in range(int(x.split('-')[0]),int(x.split('-')[1])+1)] for x in entry.split(":")[1].strip().split(" or ")] for value in range] for entry in [x for x in lines[0].split("\n")[1:] if x]}
    myticket = [int(x) for x in lines[1].split("\n")[1].split(',') if x]
    nearby = [[int(x) for x in y.split(',')] for y in lines[2].split("\n")[1:] if y]

    #print(fields)
    #print(myticket)
    print(len(nearby))

    for i in range(len(nearby)-1,-1,-1):

        for value in nearby[i]:
            found = False
            for key in fields:
                if value in fields[key]:
                    found = True
            if not found:
                nearby.pop(i)

    print(len(nearby))

    possibilities = {i:[x for x in fields.keys()] for i in myticket}
    #print(possibilities)
    for ticket in nearby:
        for i in range(len(ticket)):
            for key in fields:
                if ticket[i] not in fields[key]:
                    if key in possibilities[[x for x in possibilities.keys()][i]]:
                        possibilities[[x for x in possibilities.keys()][i]].remove(key)

    print(possibilities)

    found = []

    while len([item for sublist in [x for x in possibilities.values()] for item in sublist]) > len(possibilities.keys()):
        for key in possibilities:
            if len(possibilities[key]) == 1:
                if possibilities[key][0] not in found:
                    found.append(possibilities[key][0])
                    print(found)
            else:
                for entry in found:
                    if entry in possibilities[key]:
                        possibilities[key].remove(entry)

    print(possibilities)

    mult = []
    for key in possibilities:
        if "departure" in possibilities[key][0]:
            mult.append(key)

    print(mult)
    prod = 1
    for val in mult:
        prod *= val

    print(prod)

part2(mydata)
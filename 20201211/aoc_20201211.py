
# --- Day 11: Seating System ---
#
#   Part 1: Count empty seats after nobody is sitting next to 4 or more
#   Part 2: Count empty seats after nobody can see 5 or more
#

import sys
sys.path.append("..")

import copy

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array
mydata = [[char for char in x] for x in mydata]

sample =\
"""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

sample = [x for x in sample.split("\n") if x]
sample = [[char for char in x] for x in sample]

def part1(lines):
    stable = False
    unoccupied = [".", "L"]
    occupied = "#"
    filled = 0
    while not stable:
        newlines = copy.deepcopy(lines)
        changes = 0
        for i,row in enumerate(lines):
            for j,seat in enumerate(row):
                if seat == "L" or seat == "#":
                    neighbors = 0
                    if j > 0:
                        neighbors += (lines[i][j-1] == occupied)
                        if i > 0:
                            neighbors += (lines[i-1][j-1] == occupied)
                    if i > 0:
                        neighbors += (lines[i-1][j] == occupied)
                        if j < len(row)-1:
                            neighbors += (lines[i-1][j+1] == occupied)
                    if j < len(row)-1:
                        neighbors += (lines[i][j+1] == occupied)
                        if i < len(lines)-1:
                            neighbors += (lines[i+1][j+1] == occupied)
                    if i < len(lines)-1:
                        neighbors += (lines[i+1][j] == occupied)
                        if j > 0:
                            neighbors += (lines[i+1][j-1] == occupied)
                    if neighbors == 0 and seat == "L":
                        newlines[i][j] = "#"
                        changes += 1
                        filled += 1

                    if neighbors >= 4 and seat == "#":
                        newlines[i][j] = "L"
                        changes += 1
                        filled -= 1

        lines = copy.deepcopy(newlines)

        if not changes:
            stable = True


    print("\n".join(["".join(line) for line in lines]))
    print("Filled",filled)


def part2(lines):
    stable = False
    unoccupied = [".", "L"]
    occupied = "#"
    seats = ["#", "L"]
    filled = 0
    while not stable:
        newlines = copy.deepcopy(lines)
        changes = 0
        for i, row in enumerate(lines):
            for j, seat in enumerate(row):
                if seat == "L" or seat == "#":
                    neighbors = 0
                    if j > 0:
                        x = 1
                        while (j-x >= 0):
                            if lines[i][j-x] in seats:
                                neighbors += (lines[i][j-x] == occupied)
                                x = j+1
                            else:
                                x += 1
                        if i > 0:
                            x = 1
                            y = 1
                            while (j-x >= 0) and (i-y >= 0):
                                if lines[i-y][j-x] in seats:
                                    neighbors += (lines[i-y][j-x] == occupied)
                                    x = j+1
                                else:
                                    x += 1
                                    y += 1

                    if i > 0:
                        y = 1
                        while (i-y >= 0):
                            if lines[i-y][j] in seats:
                                neighbors += (lines[i-y][j] == occupied)
                                y = i+1
                            else:
                                y += 1
                        if j < len(row)-1:
                            x = 1
                            y = 1
                            while (j+x < len(row)) and (i-y >= 0):
                                if lines[i-y][j+x] in seats:
                                    neighbors += (lines[i-y][j+x] == occupied)
                                    x = len(row)
                                else:
                                    x += 1
                                    y += 1

                    if j < len(row)-1:
                        x = 1
                        while (j+x < len(row)):
                            if lines[i][j+x] in seats:
                                neighbors += (lines[i][j+x] == occupied)
                                x = len(row)
                            else:
                                x += 1
                        if i < len(lines)-1:
                            x = 1
                            y = 1
                            while (j+x < len(row)) and (i+y < len(lines)):
                                if lines[i+y][j+x] in seats:
                                    neighbors += (lines[i+y][j+x] == occupied)
                                    x = len(row)
                                else:
                                    x += 1
                                    y += 1

                    if i < len(lines)-1:
                        y = 1
                        while (i+y < len(lines)):
                            if lines[i+y][j] in seats:
                                neighbors += (lines[i+y][j] == occupied)
                                y = len(lines)
                            else:
                                y += 1
                        if j > 0:
                            x = 1
                            y = 1
                            while (j-x >= 0) and (i+y < len(lines)):
                                if lines[i+y][j-x] in seats:
                                    neighbors += (lines[i+y][j-x] == occupied)
                                    y = len(lines)
                                else:
                                    x += 1
                                    y += 1

                    if neighbors == 0 and seat == "L":
                        newlines[i][j] = "#"
                        changes += 1
                        filled += 1

                    if neighbors >= 5 and seat == "#":
                        newlines[i][j] = "L"
                        changes += 1
                        filled -= 1

        lines = copy.deepcopy(newlines)

        if not changes:
            stable = True

    print("\n".join(["".join(line) for line in lines]))
    print("Filled", filled)


part2(mydata)
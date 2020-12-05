
# --- Day 3: ####### ---
#
#   Part 1: Count trees hit down path through tiled hillside
#   Part 2: Count trees hit down multiple paths
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

testinput =\
"""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

treerows = testinput.split('\n')
treerows = [x for x in treerows if x]

treecoords = []

def part1():

    for i,row in enumerate(mydata):
        for j in range(len(row)):
            if row[j] == "#":
                treecoords.append((i,j))

    mylocation = [0,0]

    print(treecoords)

    width = len(mydata[0])
    hits = 0

    for i in range(len(mydata)):
        mylocation[0] += 1
        mylocation[1] += 3
        if (mylocation[0], mylocation[1]%width) in treecoords:
            hits += 1

    print(hits)

def part2():
    for i, row in enumerate(mydata):
        for j in range(len(row)):
            if row[j] == "#":
                treecoords.append((i, j))

    width = len(mydata[0])
    paths = [[1,1],[1,3],[1,5],[1,7],[2,1]]
    hits = [0 for x in paths]

    for i,path in enumerate(paths):
        mylocation = [0, 0]
        while mylocation[0] < len(mydata):
            mylocation[0] += path[0]
            mylocation[1] += path[1]
            if (mylocation[0], mylocation[1] % width) in treecoords:
                hits[i] += 1

    print(hits[0]*hits[1]*hits[2]*hits[3]*hits[4])


part2()
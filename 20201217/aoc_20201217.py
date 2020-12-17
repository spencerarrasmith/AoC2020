
# --- Day 17: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

sample =\
"""
.#.
..#
###
"""

lines = [x for x in sample.split("\n") if x]


def countneighbors(loc, cubes):
    count = 0-cubes[loc]
    for z in range(loc[2]-1, loc[2]+2):
        for y in range(loc[1]-1, loc[1]+2):
            for x in range(loc[0]-1, loc[0]+2):
                if (x,y,z) in cubes:
                    if cubes[(x,y,z)]:
                        count += 1
    return count

def countneighbors4d(loc, cubes):
    count = 0-cubes[loc]
    for w in range(loc[3]-1, loc[3]+2):
        for z in range(loc[2]-1, loc[2]+2):
            for y in range(loc[1]-1, loc[1]+2):
                for x in range(loc[0]-1, loc[0]+2):
                    if (x,y,z,w) in cubes:
                        if cubes[(x,y,z,w)]:
                            count += 1
    return count


def part1(lines, steps):
    cubes = {}

    for j in range(len(lines)):
        for i in range(len(lines[j])):
            cubes[(i, j, 0)] = (lines[j][i] == "#")

    currentstep = 0
    while currentstep < steps:
        for y in range(-currentstep-1, len(lines)+currentstep+1):
            for z in range(-currentstep-1, currentstep+2):
                cubes[(-currentstep-1,y,z)] = False
                cubes[(len(lines[0])+currentstep, y, z)] = False

        for x in range(-currentstep-1, len(lines[0])+currentstep+1):
            for z in range(-currentstep-1, currentstep+2):
                cubes[(x, -currentstep-1, z)] = False
                cubes[(x, len(lines)+currentstep, z)] = False

        for x in range(-currentstep-1, len(lines[0])+currentstep+1):
            for y in range(-currentstep-1, len(lines)+currentstep+1):
                cubes[(x, y, -currentstep-1)] = False
                cubes[(x, y, 1+currentstep)] = False

        dying = []
        creating = []
        for cube in cubes:
            n = countneighbors(cube, cubes)
            if n not in [2, 3]:
                if cubes[cube]:
                    dying.append(cube)

            if n == 3:
                if not cubes[cube]:
                    creating.append(cube)

        for cube in dying:
            cubes[cube] = False
        for cube in creating:
            cubes[cube] = True

        currentstep += 1

    print(sum(cubes.values()))



def part2(lines, steps):
    cubes = {}

    for j in range(len(lines)):
        for i in range(len(lines[j])):
            cubes[(i, j, 0, 0)] = (lines[j][i] == "#")

    currentstep = 0
    while currentstep < steps:

        for y in range(-currentstep-1, len(lines)+currentstep+1):
            for z in range(-currentstep-1, currentstep+2):
                for w in range(-currentstep - 1, currentstep + 2):
                    cubes[(-currentstep-1,y,z,w)] = False
                    cubes[(len(lines[0])+currentstep, y, z,w)] = False

        for x in range(-currentstep-1, len(lines[0])+currentstep+1):
            for z in range(-currentstep-1, currentstep+2):
                for w in range(-currentstep - 1, currentstep + 2):
                    cubes[(x, -currentstep-1, z, w)] = False
                    cubes[(x, len(lines)+currentstep, z, w)] = False

        for x in range(-currentstep-1, len(lines[0])+currentstep+1):
            for y in range(-currentstep-1, len(lines)+currentstep+1):
                for w in range(-currentstep - 1, currentstep + 2):
                    cubes[(x, y, -currentstep-1, w)] = False
                    cubes[(x, y, 1+currentstep, w)] = False

        for x in range(-currentstep-1, len(lines[0])+currentstep+1):
            for y in range(-currentstep-1, len(lines)+currentstep+1):
                for z in range(-currentstep - 1, currentstep + 2):
                    cubes[(x, y, z, -currentstep-1)] = False
                    cubes[(x, y, z, 1+currentstep)] = False

        dying = []
        creating = []
        for cube in cubes:
            n = countneighbors4d(cube, cubes)
            if n not in [2, 3]:
                if cubes[cube]:
                    dying.append(cube)

            if n == 3:
                if not cubes[cube]:
                    creating.append(cube)

        for cube in dying:
            cubes[cube] = False
        for cube in creating:
            cubes[cube] = True

        currentstep += 1


    print(sum(cubes.values()))

part2(mydata,6)



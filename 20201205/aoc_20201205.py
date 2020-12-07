
# --- Day 5: Binary Boarding ---
#
#   Part 1: Find seat id from binary space partitioned seat string
#   Part 2: Find the only empty seat
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

example = "BFFFBBFRRR"

def part1():
    maxid = 0
    for seat in mydata:
        row = seat[0:7]
        row = row.replace('B','1').replace('F','0')

        column = seat[7:]
        column = column.replace('R','1').replace('L','0')

        row = int(row,2)
        column = int(column,2)

        if row * 8 + column > maxid:
            maxid = row * 8 + column

    print("Max SeatID: ", maxid)


def part2():
    plane = [[0 for x in range(8)] for y in range(128)]
    for seat in mydata:
        row = seat[0:7]
        row = row.replace('B','1').replace('F','0')

        column = seat[7:]
        column = column.replace('R','1').replace('L','0')

        row = int(row,2)
        column = int(column,2)
        plane[row][column] += 1

    for i,seats in enumerate(plane):
        print(i,seats)

    for i, seats in enumerate(plane):
        if 0 in seats and seats.count(0) == 1:
            print("SeatID: ", i*8+seats.index(0))
        if seats.count(0) > 1:                          # for a case like [0,0,0,1,1,0,1,1]
            if 1 in seats:
                if(seats[::-1].index(1) < seats[::-1].index(0)):
                    print("SeatID: ", i * 8 + (len(seats)-seats[::-1].index(0)))

part2()


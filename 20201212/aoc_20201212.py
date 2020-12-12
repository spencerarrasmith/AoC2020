
# --- Day 12: Rain Risk ---
#
#   Part 1: Navigate ferry with steering commands
#   Part 2: Navigate ferry with steering commands relative to waypoint
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

sample =\
"""
F10
N3
F7
R90
F11
"""

test = [x for x in sample.split("\n") if x]

class Ferry():
    def __init__(self, heading='E'):
        self.heading = heading
        self.xloc = 0
        self.yloc = 0

        self.xmult = 1
        self.ymult = 0


    def turn(self, dir):
        if dir == 'R':
            if self.heading == 'N':
                print("Turn E")
                self.heading = 'E'
                self.xmult = 1
                self.ymult = 0
            elif self.heading == 'E':
                print("Turn S")
                self.heading = 'S'
                self.xmult = 0
                self.ymult = -1
            elif self.heading == 'S':
                print("Turn W")
                self.heading = 'W'
                self.xmult = -1
                self.ymult = 0
            elif self.heading == 'W':
                print("Turn N")
                self.heading = 'N'
                self.xmult = 0
                self.ymult = 1
        if dir == 'L':
            if self.heading == 'N':
                print("Turn W")
                self.heading = 'W'
                self.xmult = -1
                self.ymult = 0
            elif self.heading == 'W':
                print("Turn S")
                self.heading = 'S'
                self.xmult = 0
                self.ymult = -1
            elif self.heading == 'S':
                print("Turn E")
                self.heading = 'E'
                self.xmult = 1
                self.ymult = 0
            elif self.heading == 'E':
                print("Turn N")
                self.heading = 'N'
                self.xmult = 0
                self.ymult = 1

    def move(self, dir, value):
        if dir == 'F':
            self.xloc += self.xmult * value
            self.yloc += self.ymult * value
        if dir == 'B':
            self.xloc -= self.xmult * value
            self.yloc -= self.ymult * value
        if dir == 'N':
            self.yloc += value
        if dir == 'S':
            self.yloc -= value
        if dir == 'E':
            self.xloc += value
        if dir == 'W':
            self.xloc -= value

    def waymove(self, dir, value, waypoint):
        if dir == 'F':
            xrel = waypoint.xloc - self.xloc
            yrel = waypoint.yloc - self.yloc
            self.xloc += xrel * value
            self.yloc += yrel * value
            waypoint.xloc += xrel * value
            waypoint.yloc += yrel * value
        if dir == 'B':
            xrel = waypoint.xloc - self.xloc
            yrel = waypoint.yloc - self.yloc
            self.xloc -= xrel * value
            self.yloc -= yrel * value
            waypoint.xloc -= xrel * value
            waypoint.yloc -= yrel * value


class Waypoint():
    def __init__(self):
        self.xloc = 10
        self.yloc = 1

    def rotate(self, dir, ferry):
        self.xloc -= ferry.xloc
        self.yloc -= ferry.yloc
        if dir == 'R':
            x = self.xloc
            y = self.yloc
            self.yloc = -x
            self.xloc = y
        if dir == 'L':
            x = self.xloc
            y = self.yloc
            self.yloc = x
            self.xloc = -y
        self.xloc += ferry.xloc
        self.yloc += ferry.yloc

    def move(self, dir, value):
        if dir == 'N':
            self.yloc += value
        if dir == 'S':
            self.yloc -= value
        if dir == 'E':
            self.xloc += value
        if dir == 'W':
            self.xloc -= value


def part1():
    myboat = Ferry()

    for line in mydata:
        command = line[0]
        value = int(line[1:])
        if command in ['R','L']:
            for i in range(int(value/90)):
                myboat.turn(command)
        else:
            myboat.move(command, value)
            print(myboat.xloc, myboat.yloc)

    print("Distance:",abs(myboat.xloc) + abs(myboat.yloc))


def part2():
    myboat = Ferry()
    myway = Waypoint()

    for line in mydata:
        command = line[0]
        value = int(line[1:])
        if command in ['R','L']:
            for i in range(int(value/90)):
                myway.rotate(command, myboat)
                print('way',myway.xloc, myway.yloc)
        elif command in ['F','B']:
            myboat.waymove(command, value, myway)
            print('boat',myboat.xloc, myboat.yloc)
        else:
            myway.move(command, value)
            print('way',myway.xloc, myway.yloc)

    print("Distance:", abs(myboat.xloc) + abs(myboat.yloc))


part2()
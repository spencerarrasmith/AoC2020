
# --- Day 15: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

sample = "0,13,1,16,6,17"

mydata = "0,13,1,16,6,17"

def part1(lines):
    lines = [int(x) for x in sample.split(',')]
    say = {}
    count = 0
    nums = len(lines)
    prev = 0

    outputs = []

    for i,line in enumerate(lines):
        if line not in say:
            say[line] = [1,i,0]
            count += 1
            outputs.append(line)
            prev = line

    for i in range(nums,30000000):
        if say[prev][0] == 1:
            if 0 not in say:
                say[0] = [1, i, 0]
            else:
                say[0][0] += 1
                say[0][2] = say[0][1]
                say[0][1] = i
            outputs.append(0)
            prev = 0
        else:
            repeat = say[prev][1]-say[prev][2]
            outputs.append(repeat)
            if repeat not in say:
                say[repeat] = [1,i,0]
            else:
                say[repeat][0] += 1
                say[repeat][2] = say[repeat][1]
                say[repeat][1] = i
            prev = repeat

    print(outputs[30000000-1])


part1(sample)
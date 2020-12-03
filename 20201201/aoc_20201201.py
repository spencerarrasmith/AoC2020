# --- Day 1: Report Repair ---
#
#   Part 1: Match two numbers to add to 2020
#   Part 2: Match three numbers to add to 2020
#

#import bpy
import os

os.chdir('D:\\Projects\\AdventOfCode2020')
os.chdir('20201201')

target = 2020
testinput = [1721, 979, 366, 299, 675, 1456]

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(mode='int')

rawdata = a.array

def part1():
    smaller = []
    larger = []

    for i,entry in enumerate(rawdata):
        #bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(i*2, 0, entry/2), scale=(1, 1, entry))

        
        if entry < target/2:
            smaller.append(entry)
        else:
            larger.append(entry)

    for entry in larger:
        for entry2 in smaller:
            if entry + entry2 == target:
                print(entry*entry2)

def part2():
    found = False

    while not found:
        current = rawdata.pop(0)
        newtarget = target - current

        smaller = []
        larger = []

        for entry in rawdata:
            if entry < newtarget / 2:
                smaller.append(entry)
            else:
                larger.append(entry)

        for entry in larger:
            for entry2 in smaller:
                if entry + entry2 == newtarget:
                    found = True
                    print(current * entry * entry2)

part1()
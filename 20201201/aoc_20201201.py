# --- Day 1: Balls ---
#
#   Part 1: Expand IntCode computer with in/out and parameter modes
#   Part 2: Add jumps and comparisons
#

target = 2020
testinput = [1721, 979, 366, 299, 675, 1456]

f = open("input.txt", 'r')
rawdata = f.read().split('\n')
f.close()

rawdata = rawdata[:-1]

rawdata = [int(x) for x in rawdata]

def part1():
    smaller = []
    larger = []

    for entry in rawdata:
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
                    print(current * entry * entry2)

part2()
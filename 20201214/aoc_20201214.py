
# --- Day 14: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

import copy

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array


sample =\
"""
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

sample = [x for x in sample.split("\n") if x]

sample2 =\
"""
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

sample2 = [x for x in sample2.split("\n") if x]


def part1(lines):
    memory = {}
    for line in lines:
        if line[0:4] == "mask":
            myma = line.split('=')[1].strip()
        else:
            command = (int(line.split('=')[0].strip()[4:line.split('=')[0].strip().index(']')]), int(line.split('=')[1].strip()))

            if command[0] not in memory:
                memory[command[0]] = 0

            mybits = bitlify(command[1])
            newval = ""

            for i,char in enumerate(myma):
                if char == 'X':
                    newval += mybits[i]
                else:
                    newval += char
            memory[command[0]] = newval

    #print(memory.values())
    values = [int(x,2) for x in memory.values()]
    print(memory)
    print(sum(values))


def bitlify(num):
    remaining = copy.deepcopy(num)
    digit = 35
    output = ""
    while digit >= 0:
        if remaining >= 2**digit:
            remaining -= 2**digit
            output += '1'
        else:
            output += '0'
        digit -= 1

    while len(output) < 36:
        output = "0" + output
    return output


def part2(lines):
    memory = {}
    for line in lines:
        if line[0:4] == "mask":
            myma = line.split('=')[1].strip()
            print(myma.count('X'))
        else:
            command = (int(line.split('=')[0].strip()[4:line.split('=')[0].strip().index(']')]), int(line.split('=')[1].strip()))

            mybits = bitlify(command[0])
            newval = ""

            addresses = [""]

            for i,char in enumerate(myma):
                if char == 'X':
                    addrcount = len(addresses)
                    for i in range(addrcount):
                        newaddr = copy.deepcopy(addresses[i])
                        addresses.append(newaddr)
                    for j,address in enumerate(addresses[0:int(len(addresses)/2)]):
                        address += '1'
                        addresses[j] = address
                    for j,address in enumerate(addresses[int(len(addresses)/2):]):
                        address += '0'
                        addresses[j+int(len(addresses)/2)] = address
                if char == "0":
                    for j,address in enumerate(addresses):
                        address += mybits[i]
                        addresses[j] = address
                if char == "1":
                    for j,address in enumerate(addresses):
                        address += "1"
                        addresses[j] = address

            for address in addresses:
                memory[int(address,2)] = command[1]


    #print(memory.values())
    values = [int(x) for x in memory.values()]
    print(memory)
    print(sum(values))


part2(mydata)

#print(bitlify(12960), 100000001000000010101000101101100110)
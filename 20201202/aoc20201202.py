# --- Day 2: Password Philosophy---
#
#   Part 1: Count passwords that obey character count rules
#   Part 2: Count passwords that obey character location rules
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

testinput = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

def part1():
    #lows = []
    #highs = []
    #letters = []
    #passwords = []
    #counts = []
    numvalid = 0
    for row in mydata:
        low = int(row.split('-')[0])
        high = int(row.split(' ')[0].split('-')[1])
        letter = row.split(' ')[1][0]
        password = row.split(' ')[2]

        count = 0
        while password.find(letter) >= 0:
            password = password[password.find(letter)+1:]
            count += 1

        if count >= low and count <= high:
            numvalid += 1

    print(numvalid)

def part2():
    numvalid = 0
    for row in mydata:
        low = int(row.split('-')[0])
        high = int(row.split(' ')[0].split('-')[1])
        letter = row.split(' ')[1][0]
        password = row.split(' ')[2]

        low -= 1
        high -= 1

        if (password[low] == letter and not password[high] == letter)\
                or (password[high] == letter and not password[low] == letter):
            numvalid += 1

    print(numvalid)

part2()
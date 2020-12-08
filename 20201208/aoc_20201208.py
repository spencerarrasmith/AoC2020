
# --- Day 8: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

testprogram =\
"""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

testlines = [x for x in testprogram.split("\n") if x]

class GameBoy():
    def __init__(self, program, mode=1):
        self.accumulator = 0
        self.ip = 0
        self.program = program
        self.executioncounts = [0 for x in program]
        self.running = False
        self.mode = mode

        self.nopjmpindex = 0
        self.nopjmps = []
        if self.mode == 2:  # part 2
            self.findnopjmp()


    def run(self):
        self.running = True
        self.accumulator = 0
        self.ip = 0
        self.executioncounts = [0 for x in self.program]
        if self.mode == 2:
            print(self.nopjmps[self.nopjmpindex])
            line = self.program[self.nopjmps[self.nopjmpindex]]
            print("Swapping line", self.nopjmps[self.nopjmpindex])
            if "nop" in line:
                line = line.replace("nop","jmp")
            elif "jmp" in line:
                line = line.replace("jmp","nop")
            self.program[self.nopjmps[self.nopjmpindex]] = line

            if self.nopjmpindex > 0:
                prevline = self.program[self.nopjmps[self.nopjmpindex-1]]
                if "nop" in prevline:
                    prevline = prevline.replace("nop", "jmp")
                elif "jmp" in prevline:
                    prevline = prevline.replace("jmp", "nop")
                self.program[self.nopjmps[self.nopjmpindex - 1]] = prevline

            self.nopjmpindex += 1



        #self.program[-2] = self.program[-2].replace('jmp','nop')
        while self.running:
            command = self.program[self.ip].split(' ')[0]
            if self.executioncounts[self.ip] > 0:
                self.running = False
                print("Stopped")
                print("Accumulator is", self.accumulator)
                if self.mode == 1:
                    continue
                elif self.mode == 2:
                    self.run()
                    break

            self.executioncounts[self.ip] += 1
            if command != "nop":
                value = int(self.program[self.ip].split(' ')[1])
            if command == "acc":
                self.acc(value)
                self.ip += 1
            if command == "jmp":
                self.jmp(value)
            if command == "nop":
                self.ip += 1

            if self.ip == len(self.program):
                self.running = False
                print("Finished")
                print(self.program)
                print("Accumulator is", self.accumulator)

    def acc(self, val):
        self.accumulator += val

    def jmp(self, offset):
        self.ip += offset

    def nop(self):
        return

    def findnopjmp(self):
        for i,line in enumerate(self.program):
            if "nop" in line or "jmp" in line:
                self.nopjmps.append(i)




def part1():
    mygameboy = GameBoy(mydata)
    mygameboy.run()


def part2():
    mygameboy = GameBoy(mydata, mode=2)
    mygameboy.run()


part1()


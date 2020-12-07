
# --- Day 7: Handy Haversacks ---
#
#   Part 1: Count possible bags which can contain a shiny gold bag
#   Part 2: Count total number of bags nested in a shiny gold bag
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array

testrules =\
"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

class BagOf():
    def __init__(self, color=""):
        self.color = color
        self.contains = {}

    def addContain(self, color, qty):
        self.contains[color] = qty


def part1():
    rules = testrules.split('\n')
    rules = [x for x in rules if x]
    bags = []

    for rule in mydata:
        mycolor = rule.split("contain")[0][:-6]
        mycontained = rule.split("contain")[1].strip().split(",")
        mycontained = [x.replace('.',' ').strip() for x in mycontained]

        mybag = BagOf(mycolor)
        bags.append(mybag)
        for contained in mycontained:
            if "no " in contained:
                continue
            mycontainedcolor = " ".join(contained.split(" ")[1:-1])
            mybag.addContain(mycontainedcolor, int(contained.split(" ")[0]))


    possibilities = set()
    processed = set()

    for bag in bags:
        if "shiny gold" in bag.contains.keys():
            #print(bag.color)
            possibilities.add(bag.color)

    while possibilities:
        possibility = possibilities.pop()
        if possibility in processed:
            continue
        else:
            for bag in bags:
                if possibility in bag.contains.keys():
                    if possibility not in processed:
                        possibilities.add(bag.color)
                        print(bag.color)

            processed.add(possibility)

    print("Containing bags:", len(processed))


testrules2 =\
"""
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

def part2():

    rules = testrules2.split('\n')
    rules = [x for x in rules if x]
    bags = []

    for rule in mydata:
        mycolor = rule.split("contain")[0][:-6]
        mycontained = rule.split("contain")[1].strip().split(",")
        mycontained = [x.replace('.', ' ').strip() for x in mycontained]

        mybag = BagOf(mycolor)
        if mycolor == "shiny gold":
            goldbag = mybag
        bags.append(mybag)
        for contained in mycontained:
            if "no " in contained:
                continue
            mycontainedcolor = " ".join(contained.split(" ")[1:-1])
            mybag.addContain(mycontainedcolor, int(contained.split(" ")[0]))

    unprocessed = [goldbag]
    total = 0

    while unprocessed:
        current = unprocessed.pop(0)
        total += sum(current.contains.values())
        for color in current.contains.keys():
            for bag in bags:
                if color == bag.color:
                    for i in range(current.contains[color]):
                        unprocessed.append(bag)
                        #total += 1

    print("Bags inside:", total)

part2()

# --- Day 10: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(mode='int')

mydata = a.array


test =\
"""
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

shortest=\
"""
16
10
15
5
1
11
7
19
6
12
4
"""

lines = [int(x) for x in test.split("\n") if x]


def part1(lines):
    lines.sort()
    countone = 1
    countthree = 1

    for i in range(len(lines)-1):
        print(lines[i], lines[i+1])
        if lines[i+1] == lines[i] + 1:
            countone += 1
        if lines[i + 1] == lines[i] + 3:
            countthree += 1

    print(countone*countthree)

class Adapter():
    def __init__(self, value=0):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class AdapterTree():
    def __init__(self, root=None):
        self.root = root
        self.numnodes = 1
        self.currentnode = root
        self.nodes = [root]
        self.leaves = [root]

    def addNode(self, node):
        self.numnodes += 1
        self.nodes.append(node)
        self.currentnode.addChild(node)
        self.leaves.append(node)



def part2(lines, st=0):
    lines.sort()
    print(lines)

    currentvalue = st
    firstnode = Adapter(currentvalue)
    tree = AdapterTree(firstnode)
    ends = 0
    while tree.leaves:
        myleaf = tree.leaves[0]
        tree.currentnode = myleaf
        currentvalue = myleaf.value

        if currentvalue == lines[-1]:
            ends += 1
        if currentvalue + 1 in lines:
            tree.addNode(Adapter(currentvalue+1))
        if currentvalue + 2 in lines:
            tree.addNode(Adapter(currentvalue+2))
        if currentvalue + 3 in lines:
            tree.addNode(Adapter(currentvalue+3))
        tree.leaves.pop(0)

    print(ends)
    return(ends)

def makesections(lines):
    lines.sort()
    sections = [[0]]
    while lines:
        current=lines.pop(0)
        if current == sections[-1][-1] + 3:
            sections.append([current])
        else:
            sections[-1].append(current)
    print(sections)
    return sections

sections = makesections(mydata)
paths = 1
for section in sections:
    paths *= part2(section, section[0])
print(paths)

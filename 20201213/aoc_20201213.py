
# --- Day 13: ####### ---
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
939
7,13,x,x,59,x,31,19
"""

sample = [x for x in sample.split("\n") if x]

def part1():
    mytime = int(mydata[0])
    busids = mydata[1].split(',')

    busids = [int(x) for x in busids if x!='x']
    print(busids)

    mindex = -1
    mintime = 1000000
    for i,id in enumerate(busids):
        wait = -mytime % id
        if wait < mintime:
            mintime = wait
            mindex = i

    print(mintime*busids[mindex])


def primeFactorize(num):
    start = copy.deepcopy(num)
    divisor = 2
    factors = {}
    while divisor <= start/2:
        if num/divisor == int(num/divisor):
            num = int(num/divisor)
            if divisor in factors.keys():
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            print(num, divisor)
        else:
            divisor += 1
    if not factors.keys():
        factors[start] = 1
    return factors


def leastCommonMultiple(num1, num2):
    f1 = primeFactorize(num1)
    f2 = primeFactorize(num2)

    lcm = copy.deepcopy(f1)

    for factor in f2.keys():
        if factor not in lcm.keys():
            lcm[factor] = f2[factor]
        else:
            if f2[factor] > lcm[factor]:
                lcm[factor] = f2[factor]

    return lcm


def leastCommonMultipleOffset(num1, num2, offset):
    if num1 < num2:
        lesser = num1
        greater = num2
    else:
        lesser = num2
        greater = num1

    diff = greater % lesser
    modmod = copy.deepcopy(diff)

    index = 1
    if num1 < num2:
        while modmod != offset:
            modmod += diff
            modmod = modmod % lesser
            index += 1

        print('Num1:', greater * index - offset)
        res1 = greater * index - offset
        print('Num2:', greater * index)
        res2 = greater * index
        print(index - offset)

    else:
        while modmod != lesser-offset:
            modmod += diff
            modmod = modmod % lesser
            index += 1

        print('Num1:', greater * index)
        res1 = greater * index
        print('Num2:', greater * index + offset)
        res2 = greater * index + offset
        print(index)

    return(res1, res2)





    #print(res1, res2)

#print(primeFactorize(67))
#print(leastCommonMultipleOffset(19,37,13))
#print(leastCommonMultipleOffset(17,13,1))




def part2():
    test = "17,x,13,19"
    busids = test.split(',')

    for i,id in enumerate(busids):
        if i < len(busids)-1:
            try:
                int(id)
                offset = 1
                while busids[i+offset] == 'x':
                    offset += 1
            except ValueError:
                continue
            print(busids[i], busids[i+offset], offset)
            leastCommonMultipleOffset(int(busids[i]), int(busids[i+offset]), offset)

    print(busids)



    #for i in range(len(busids))


part2()

# --- Day 4: Passport Processing ---
#
#   Part 1: Determine valid passports by data keys
#   Part 2: Determine valid passports by data
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray(delimiter="\n\n")

mydata = a.array


sample =\
"""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

lines = sample.split("\n\n")

def part1():
    valid = 0
    passports = []
    for line in mydata:
        line = " ".join(line.split("\n"))
        if "ecl" in line and\
            "pid" in line and\
            "eyr" in line and\
            "hcl" in line and\
            "byr" in line and\
            "iyr" in line and\
            "hgt" in line:

            valid += 1
            newpassport = {}
            for item in line.split(" "):
                if ":" in item:
                    newpassport[item.split(":")[0]] = item.split(":")[1]
            passports.append(newpassport)

    print(valid)
    print(passports)


def part2():
    validcount = 0
    passports = []
    for line in mydata:
        line = " ".join(line.split("\n"))
        if "ecl" in line and\
            "pid" in line and\
            "eyr" in line and\
            "hcl" in line and\
            "byr" in line and\
            "iyr" in line and\
            "hgt" in line:


            newpassport = {}
            valid = True
            for item in line.split(" "):
                if ":" in item:
                    newpassport[item.split(":")[0]] = item.split(":")[1]

            print("\n", newpassport)

            if int(newpassport["byr"]) < 1920 or int(newpassport["byr"]) > 2002:
                print("byr bad:", newpassport["byr"])
                valid = False
                continue

            if int(newpassport["iyr"]) < 2010 or int(newpassport["iyr"]) > 2020:
                print("iyr bad:", newpassport["iyr"])
                valid = False
                continue

            if int(newpassport["eyr"]) < 2020 or int(newpassport["eyr"]) > 2030:
                print("eyr bad:", newpassport["eyr"])
                valid = False
                continue

            if "cm" in newpassport["hgt"]:
                try:
                    if int(newpassport["hgt"][0:3]) < 150 or int(newpassport["hgt"][0:3]) > 193:
                        print("hgt bad:", newpassport["hgt"])
                        valid = False
                        continue
                except ValueError:
                    print("hgt bad:", newpassport["hgt"])
                    valid = False
                    continue
            elif "in" in newpassport["hgt"]:
                try:
                    if int(newpassport["hgt"][0:2]) < 59 or int(newpassport["hgt"][0:2]) > 76:
                        print("hgt bad:", newpassport["hgt"])
                        valid = False
                        continue
                except ValueError:
                    print("hgt bad:", newpassport["hgt"])
                    valid = False
                    continue
            else:
                print("hgt bad:", newpassport["hgt"])
                valid = False
                continue

            if len(newpassport["hcl"]) == 7 and newpassport["hcl"][0] == "#":
                try:
                    int(newpassport["hcl"][1:], 16)
                except ValueError:
                    print("hcl bad:", newpassport["hcl"])
                    valid = False
                    continue
            else:
                print("hcl bad:", newpassport["hcl"])
                valid = False
                continue

            if newpassport["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                print("ecl bad:", newpassport["ecl"])
                valid = False
                continue

            if len(newpassport["pid"]) == 9:
                try:
                    int(newpassport["pid"])
                except ValueError:
                    print("pid bad:", newpassport["pid"])
                    valid = False
                    continue
            else:
                print("pid bad:", newpassport["pid"])
                valid = False
                continue

            if valid:
                validcount += 1
                passports.append(newpassport)
                print("Valid!")

    print(validcount)
    print(len(passports))



part2()
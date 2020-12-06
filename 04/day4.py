import re

file = open("input.txt", "r").read().split("\n\n")

keys1 = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']


def part1(input, key_list):
    valid = 0

    for line in input:
        keys = re.findall(r"(\w+):", line)

        if len(set(key_list) - set(keys)) == 0:
            valid += 1

    return valid


def part2(input):
    valid = 0

    for line in input:
        if re.search(r"byr:(19[2-9][0-9]|200[0-2])\b", line)\
        and re.search(r"iyr:(201[0-9]|20[0-2]0)\b", line)\
        and re.search(r"eyr:(202[0-9]|2030)\b", line)\
        and re.search(r"(hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in|hgt:1[5-8][0-9]cm|hgt:19[0-3]cm)\b", line)\
        and re.search(r"hcl:#([0-9]|[a-f]){6}\b", line)\
        and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", line)\
        and re.search(r"pid:([0-9]){9}\b", line):
            valid += 1

    return valid


print(part1(file, keys1))
print(part2(file))

file = open("input.txt", "r")
nums = [int(i) for i in file.read().split("\n")]


def part1(list):
    for i in list:
        for j in list:
            if i+j == 2020:
                return i*j


def part2(list):
    for i in list:
        for j in list:
            for k in list:
                if i+j+k == 2020:
                    return i*j*k


print(part1(nums))
print(part2(nums))

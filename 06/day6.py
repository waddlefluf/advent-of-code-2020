file = [char.replace("\n", "") for char in open("input.txt", "r").read().split("\n\n")]
file_space = [char.replace("\n", " ") for char in open("input.txt", "r").read().split("\n\n")]


def part1(input):
    count = 0

    for line in input:
        count += len(set(line))

    return count


def part2(input):
    count = 0

    for line in input:
        chars = set("abcdefghijklmnopqrstuvwxyz")

        for person in line.split(" "):
            chars = chars.intersection(set(person))

        count += len(chars)

    return count


print(part1(file))
print(part2(file_space))

lines = open("input.txt", "r").readlines()

def part1(passwords):
    valid = 0

    for line in passwords:
        password = line.split(" ")[-1]
        letter = line.split(":", 1)[0].split(" ")[1]
        min = int(line.split(" ")[0].split("-")[0])
        max = int(line.split(" ")[0].split("-")[1])

        if min <= password.count(letter) <= max:
            valid += 1

    return valid


def part2(passwords):
    valid = 0

    for line in passwords:
        password = line.split(" ")[-1]
        letter = line.split(":", 1)[0].split(" ")[1]
        num1 = int(line.split(" ")[0].split("-")[0])
        num2 = int(line.split(" ")[0].split("-")[1])

        if (password[num1-1] == letter) ^ (password[num2-1] == letter):
            valid += 1

    return valid


print(part1(lines))
print(part2(lines))
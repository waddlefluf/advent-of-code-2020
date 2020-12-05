input = open("input.txt", "r").read().split("\n")


def part1(file):
    seats = []

    for line in file:
        row_max = list(range(128))
        col_max = list(range(8))

        for char in line:
            if char == "F":
                row_max = row_max[:len(row_max) // 2]
            elif char == "B":
                row_max = row_max[len(row_max) // 2:]
            elif char == "L":
                col_max = col_max[:len(col_max) // 2]
            elif char == "R":
                col_max = col_max[len(col_max) // 2:]

        seats.append((row_max[0] * 8) + col_max[0])

    return seats


def part2(seat_list):
    for seat in range(min(seat_list), max(seat_list)):
        if seat not in seat_list:
            return seat


print(max(part1(input)))
print(part2(part1(input)))

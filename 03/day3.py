input = open("input.txt").read().split("\n")


def count_trees(grid, x, y):
    count = 0

    rows = len(grid)
    cols = len(grid[0])

    r = 0
    c = 0

    while r < rows:
        r += y
        c += x

        if r >= rows:
            break

        if grid[r][c % cols] == "#":
            count += 1

    return count


a = count_trees(input, 1, 1)
b = count_trees(input, 3, 1)
c = count_trees(input, 5, 1)
d = count_trees(input, 7, 1)
e = count_trees(input, 1, 2)

print(count_trees(input, 3, 1))  # part 1
print(a*b*c*d*e)  # part 2

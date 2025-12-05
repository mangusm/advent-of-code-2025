import pathlib
from copy import copy


def parse_input():
    grid = []
    input = pathlib.Path("inputs/04.txt").read_text()
    for row in input.split("\n"):
        grid.append([cell for cell in row])

    return grid


def part_one():
    answer = 0
    grid = parse_input()

    """
    (-1,-1) (0,-1)  (1,-1)
    (-1,0)  (0,0)   (1,0)
    (-1,1)  (0,1)   (1,1)
    """

    checks = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    for y in range(0, len(grid)):
        row = grid[y]
        for x in range(0, len(row)):
            if grid[y][x] == "@":
                adj_rolls = 0
                for dx, dy in checks:
                    if (
                        x + dx < 0
                        or x + dx > len(row) - 1
                        or y + dy < 0
                        or y + dy > len(grid) - 1
                    ):
                        continue
                    if grid[y + dy][x + dx] == "@":
                        adj_rolls += 1

                if adj_rolls < 4:
                    answer += 1

    return answer


def part_two():
    answer = 0
    current_grid = parse_input()

    """
    (-1,-1) (0,-1)  (1,-1)
    (-1,0)  (0,0)   (1,0)
    (-1,1)  (0,1)   (1,1)
    """

    checks = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    while True:
        removed = 0
        next_grid = copy(current_grid)

        for y in range(0, len(current_grid)):
            row = current_grid[y]
            for x in range(0, len(row)):
                if current_grid[y][x] == "@":
                    adj_rolls = 0
                    for dx, dy in checks:
                        if (
                            x + dx < 0
                            or x + dx > len(row) - 1
                            or y + dy < 0
                            or y + dy > len(current_grid) - 1
                        ):
                            continue
                        if current_grid[y + dy][x + dx] == "@":
                            adj_rolls += 1

                    if adj_rolls < 4:
                        next_grid[y][x] = "."
                        removed += 1
        current_grid = next_grid

        if removed == 0:
            break

        answer += removed

    return answer


part_one_answer = part_one()
part_two_answer = part_two()

print(f"Part One: {part_one_answer}")
print(f"Part Two: {part_two_answer}")

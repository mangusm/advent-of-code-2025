import pathlib

input = pathlib.Path("inputs/01.txt").read_text()


def part_one():
    position = 50
    answer = 0

    rotations = input.split("\n")
    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])
        clicks *= -1 if direction == "L" else 1
        position += clicks
        if position % 100 == 0:
            answer += 1

    return answer


def part_two():
    position = 50
    answer = 0

    rotations = input.split("\n")
    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])
        for _ in range(0, clicks):
            position += 1 if direction == "R" else -1
            if position % 100 == 0:
                answer += 1
    return answer


part_one_answer = part_one()
part_two_answer = part_two()

print(f"Part One: {part_one_answer}")
print(f"Part Two: {part_two_answer}")

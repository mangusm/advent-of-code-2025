import csv
import pathlib


def parse_input():
    ranges = []
    input = pathlib.Path("inputs/02.txt").read_text()
    for product_range in input.split(","):
        product_ids = []
        for product_id in product_range.split("-"):
            product_ids.append(int(product_id))
        ranges.append(product_ids)

    return ranges


def part_one():
    answer = 0
    product_id_ranges = parse_input()
    for id_range in product_id_ranges:
        for id_int in range(id_range[0], id_range[1] + 1):
            if id_int < 10:
                continue
            id_str = str(id_int)
            l = len(id_str)
            if l % 2 == 0:
                if id_str[: l // 2] == id_str[l // 2 :]:
                    answer += id_int

    return answer


def part_two():
    answer = 0
    product_id_ranges = parse_input()
    for id_range in product_id_ranges:
        for id_int in range(id_range[0], id_range[1] + 1):
            if id_int < 10:
                continue
            id_str = str(id_int)
            l = len(id_str)
            for divisor in range(l // 2, 1, -1):
                if l % divisor == 0:
                    pattern = id_str[0:divisor]
                    if pattern * (l // divisor) == id_str:
                        answer += id_int
                        break

    return answer


part_one_answer = part_one()
part_two_answer = part_two()

print(f"Part One: {part_one_answer}")
print(f"Part Two: {part_two_answer}")

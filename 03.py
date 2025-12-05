import pathlib


def parse_input():
    banks = []
    input = pathlib.Path("inputs/03.txt").read_text()
    for bank in input.split("\n"):
        bank_int = [int(battery) for battery in bank]
        banks.append(bank_int)

    return banks


def part_one():
    answer = 0
    banks = parse_input()
    for bank in banks:
        tens = 0
        tens_battery_index = 0
        for i in range(len(bank) - 2, -1, -1):
            battery = bank[i]
            if battery >= tens:
                tens = battery
                tens_battery_index = i

        ones = 0
        for battery in bank[tens_battery_index + 1 :]:
            if battery > ones:
                ones = battery

        answer += tens * 10 + ones

    return answer


def part_two():
    answer = 0
    banks = parse_input()
    for bank in banks:
        index = 0
        num_batteries = len(bank)
        for power in range(11, -1, -1):
            chosen_battery_jolts = 0
            for i in range(index, num_batteries - power):
                choice = bank[i]
                if choice > chosen_battery_jolts:
                    chosen_battery_jolts = choice
                    index = i
            index += 1
            answer += chosen_battery_jolts * 10**power

    return answer


part_one_answer = part_one()
part_two_answer = part_two()

print(f"Part One: {part_one_answer}")
print(f"Part Two: {part_two_answer}")

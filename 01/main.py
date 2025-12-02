# journey of 01.12.2025
# 16:48 - penalty of 10min
# 17:21 - penalty of 10min
# 17:38 - penalty of 10min
# 18:51 - penalty of 10min


from typing import Tuple


def handle_overshoot(raw_sum: int) -> int:
    zeros = 0
    pos = raw_sum

    while pos < 0 or pos >= 100:
        if pos == 0:
            break

        if pos < 0:
            pos += 100
            zeros += 1

        if pos >= 100:
            pos -= 100
            zeros += 1

    return (pos, zeros)


def get_rotation_amount(line: str) -> int:
    direction = line[0]
    abs_amount = int(line[1::])

    if direction == "R":
        amount = abs_amount
    elif direction == "L":
        amount = -1 * abs_amount

    return amount


def part_one():
    print(" ---- part one ---- ")
    with open("input.txt", "r") as directions:
        current_pos = 50
        basic_zeros = 0
        zeros_incl_overturns = 0

        for line in directions:
            amount = get_rotation_amount(line)

            sum = current_pos + amount
            current_pos = sum % 100

            if current_pos == 0:
                basic_zeros += 1

        print(f"solution no1: {basic_zeros}")


def part_two():
    print(" ---- part two ---- ")
    with open("input.txt", "r") as directions:
        current_pos = 50
        zeros = 0

        for line in directions:

            amount = get_rotation_amount(line)

            modifier = amount // abs(amount)  # 1 or -1
            while amount != 0:
                current_pos = (current_pos + modifier) % 100
                amount -= modifier

                if current_pos == 0:
                    zeros += 1

        print(f"solution no2: {zeros}")


part_one()
part_two()

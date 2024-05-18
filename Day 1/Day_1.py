import re

def part_one():
    pattern = re.compile(r'(\d)')

    sum = 0

    with open('input.txt', 'r') as f:
        for line in f:
            digits = pattern.findall(line)
            sum += ((int(digits[0]) * 10) + int(digits[-1]))

    print(sum)

def part_two():
    pattern1 = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
    pattern2 = re.compile(r'.*(\d|one|two|three|four|five|six|seven|eight|nine)')

    mp = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    sum = 0

    with open('input.txt', 'r') as f:
        for line in f:
            tens = pattern1.search(line)
            ones = pattern2.search(line)

            tens_digit = tens.group(1)
            ones_digit = ones.group(1)

            if not tens_digit.isdigit():
                tens_digit = mp[tens_digit]

            if not ones_digit.isdigit():
                ones_digit = mp[ones_digit]

            sum += ((int(tens_digit) * 10) + int(ones_digit))

    print(sum)

part_one()
part_two()

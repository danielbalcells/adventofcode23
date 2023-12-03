STRING_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def get_first_digit(line):
    leftmost_start = 10000
    for string_number in STRING_MAP.keys():
        start = line.find(string_number)
        if start >= 0 and start < leftmost_start:
            leftmost_start = start
            first_digit = STRING_MAP[string_number]
    return first_digit


def get_last_digit(line):
    rightmost_start = -1
    for string_number in STRING_MAP.keys():
        start = line.rfind(string_number)
        if start > rightmost_start:
            rightmost_start = start
            last_digit = STRING_MAP[string_number]
    return last_digit


def get_calibration_value(line):
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    calibration_value = 10 * first_digit + last_digit
    #  print(f'{calibration_value} {line}')
    return calibration_value


def get_calibration_sum(lines):
    calibration_sum = 0
    for line in lines:
        calibration_value = get_calibration_value(line)
        calibration_sum += calibration_value
    return calibration_sum


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]

    calibration_sum = get_calibration_sum(lines)
    print(f'Sum of calibration values: {calibration_sum}')

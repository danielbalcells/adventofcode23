def get_first_and_last_digits(line):
    first_digit = -1
    for c in line:
        try:
            digit = int(c)
            if first_digit < 0:
                first_digit = digit
        except Exception as e:
            pass
    last_digit = digit
    return first_digit, last_digit


def get_calibration_value(line):
    first_digit, last_digit = get_first_and_last_digits(line)
    calibration_value = 10 * first_digit + last_digit
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

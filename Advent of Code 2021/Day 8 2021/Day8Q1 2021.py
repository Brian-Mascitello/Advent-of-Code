"""
Author:     Brian Mascitello
Date:       12/8/2021
Websites:   https://adventofcode.com/2021/day/8
Info:       --- Day 8: Seven Segment Search ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day8Q1 2021 Input.txt')

    io_dict = {}
    for signal_pattern in data.splitlines():
        signal_input, signal_output = signal_pattern.split(' | ')
        io_dict[signal_input] = signal_output

    digits_appear = 0
    for value in io_dict.values():
        signal_input = value.split()
        input_lengths = list(map(len, signal_input))

        for length in input_lengths:
            if length in [2, 3, 4, 7]:
                digits_appear += 1

    print(f'Digits appear {digits_appear} times.')


main()

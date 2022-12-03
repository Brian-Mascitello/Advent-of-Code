"""
Author:     Brian Mascitello
Date:       11/25/2022
Websites:   https://adventofcode.com/2021/day/16
Info:       --- Day 16: Packet Decoder ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def hex_to_bin(input_str):
    hex_to_bin_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                       '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
                       'E': '1110', 'F': '1111'}

    binary_str = ''.join([hex_to_bin_dict[char] for char in input_str])

    return binary_str


def main():
    # Testing
    # data = get_data('Day15Q1 2021 Test Input.txt')
    # Actual
    data = get_data('Day1Q1 2022 Input.txt')

    hex_example_1 = 'D2FE28'
    bin_example_1 = hex_to_bin(hex_example_1)
    print(bin_example_1)


if __name__ == '__main__':
    main()

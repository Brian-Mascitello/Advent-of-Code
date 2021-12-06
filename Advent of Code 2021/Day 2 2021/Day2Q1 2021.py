"""
Author:     Brian Mascitello
Date:       12/5/2021
Websites:   https://adventofcode.com/2021/day/2
Info:       --- Day 2: Dive! ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day2Q1 2021 Input.txt')

    depth_position = 0
    horizontal_position = 0
    for command in data.splitlines():
        instruction, units = command.split()
        units = int(units)
        if instruction == 'forward':
            horizontal_position = horizontal_position + units
        else:
            if instruction == 'down':
                depth_position = depth_position + units
            else:
                depth_position = depth_position - units

    print(f'depth_position: {depth_position}')
    print(f'horizontal_position: {horizontal_position}')
    print(f'multiply: {depth_position*horizontal_position}')


main()

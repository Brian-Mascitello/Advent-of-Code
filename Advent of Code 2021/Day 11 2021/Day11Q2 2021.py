"""
Author:     Brian Mascitello
Date:       12/13/2021
Websites:   https://adventofcode.com/2021/day/11
Info:       --- Day 11: Dumbo Octopus ---
            --- Part Two ---
"""

import numpy as np
from numpy import int64


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day11Q1 2021 Input.txt')

    # test_data1 = """11111\n19991\n19191\n19991\n11111"""
    # data = test_data1

    data_lists = []
    for line in data.splitlines():
        data_lists.append(list(map(int, line)))

    octopuses = np.array(data_lists, dtype=int64)
    print(f'Before any steps:\n{octopuses}')

    flash_count = 0
    keep_stepping = True
    step = 1
    while keep_stepping:
        # print(f'\nAfter step {step}:')
        octopuses += 1
        flashes = list(zip(*np.where(octopuses > 9)))
        for flash in flashes:
            increase_by_flash = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    temp_flash = [flash[0], flash[1]]
                    temp_flash[0] += x
                    temp_flash[1] += y
                    if all(0 <= index < len(octopuses) for index in temp_flash):
                        increase_by_flash.append(temp_flash)
                        octopuses[temp_flash[0]][temp_flash[1]] += 1
                        if octopuses[temp_flash[0]][temp_flash[1]] > 9:
                            if (temp_flash[0], temp_flash[1]) not in flashes:
                                flashes.append((temp_flash[0], temp_flash[1]))

        flash_count += np.count_nonzero(octopuses > 9)
        octopuses[np.where(octopuses > 9)] = 0
        # print(f'Flash Count: {flash_count}')
        # print(octopuses)

        if len(flashes) == octopuses.size:
            print(f'\nFirst step all flash simultaneously: {step}')
            keep_stepping = False
        else:
            step += 1

    print(f'\nFinal Flash Count: {flash_count}')


main()

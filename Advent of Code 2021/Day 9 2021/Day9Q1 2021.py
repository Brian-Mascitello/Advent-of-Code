"""
Author:     Brian Mascitello
Date:       12/9/2021
Websites:   https://adventofcode.com/2021/day/9
Info:       --- Day 9: Smoke Basin ---
"""

import numpy as np
from numpy import int64


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day9Q1 2021 Input.txt')

    data_lists = []
    for line in data.splitlines():
        data_lists.append(list(map(int, line)))

    heightmap = np.array(data_lists, dtype=int64)

    x_list = list(range(heightmap.shape[0]))
    y_list = list(range(heightmap.shape[1]))
    summation = 0
    for x in x_list:
        for y in y_list:
            current = heightmap[x][y]
            low_point = True
            if x - 1 in x_list:
                if heightmap[x - 1][y] <= current:
                    low_point = False
            if x + 1 in x_list:
                if heightmap[x + 1][y] <= current:
                    low_point = False
            if y - 1 in y_list:
                if heightmap[x][y - 1] <= current:
                    low_point = False
            if y + 1 in y_list:
                if heightmap[x][y + 1] <= current:
                    low_point = False
            if low_point:
                summation += (current + 1)

    print(summation)


main()

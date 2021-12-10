"""
Author:     Brian Mascitello
Date:       12/9/2021
Websites:   https://adventofcode.com/2021/day/9
Info:       --- Day 9: Smoke Basin ---
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
    data = get_data('Day9Q1 2021 Input.txt')

    data_lists = []
    for line in data.splitlines():
        data_lists.append(list(map(int, line)))

    heightmap = np.array(data_lists, dtype=int64)

    x_list = list(range(heightmap.shape[0]))
    y_list = list(range(heightmap.shape[1]))
    area = []
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
                basin = [[x, y]]
                for row, column in basin:
                    if row - 1 in x_list and heightmap[row - 1][column] != 9 and [row - 1, column] not in basin:
                        basin.append([row - 1, column])
                    if row + 1 in x_list and heightmap[row + 1][column] != 9 and [row + 1, column] not in basin:
                        basin.append([row + 1, column])
                    if column - 1 in y_list and heightmap[row][column - 1] != 9 and [row, column - 1] not in basin:
                        basin.append([row, column - 1])
                    if column + 1 in y_list and heightmap[row][column + 1] != 9 and [row, column + 1] not in basin:
                        basin.append([row, column + 1])
                area.append(len(basin))

    area.sort(reverse=True)
    # print(area)
    three_largest_basins = area[0:3]
    print(np.prod(three_largest_basins))


main()

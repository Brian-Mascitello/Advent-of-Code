"""
Author:     Brian Mascitello
Date:       12/4/2017
Websites:   http://adventofcode.com/2017/day/3
Info:       --- Day 3: Spiral Memory ---
            --- Part Two ---
"""

from itertools import product, starmap
import numpy as np


def find_valid_neighbors(x, y, maximum):
    neighbors = list(starmap(lambda a, b: [x + a, y + b], product([-1, 0, 1], [-1, 0, 1])))
    neighbors.remove([x, y])
    remove_list = neighbors.copy()
    for coordinates in neighbors:
        for position in coordinates:
            if position < 0 or position >= maximum:
                if coordinates in remove_list:
                    remove_list.remove(coordinates)
    return remove_list


def generate_path(multiplier):
    pathway = list()

    # Right then up
    pathway.append([1, 0])
    for index in range(multiplier - 1):
        pathway.append([0, -1])

    # Left over top
    for index in range(multiplier):
        pathway.append([-1, 0])

    # Down left side
    for index in range(multiplier):
        pathway.append([0, 1])

    # Right to finish
    for index in range(multiplier):
        pathway.append([1, 0])

    return pathway


def print_value(count_value, floating_value):
    print(count_value, '{0:.0f}'.format(floating_value))


def sum_neighbors(neighbors, input_array):
    summation = 0
    for neighbor in neighbors:
        x = neighbor[0]
        y = neighbor[1]
        summation += input_array[x][y]
    return summation


puzzle_input = 347991

length = 19  # odd
spiral_array = np.zeros((length, length))
center = length // 2
spiral_array[center][center] = 1
count = 1
# print_value(count, spiral_array[center][center])

current_x = center
current_y = center
multiple = 0
while current_x < length - 1:
    multiple += 2
    path = generate_path(multiple)
    for step in path:
        count += 1
        current_x += step[0]
        current_y += step[1]
        acquaintances = find_valid_neighbors(current_y, current_x, length)
        spiral_array[current_y][current_x] = sum_neighbors(acquaintances, spiral_array)
        # print(count, '{0:.0f}'.format(spiral_array[current_y][current_x]))
        if spiral_array[current_y][current_x] > puzzle_input:
            next_value = int(spiral_array[current_y][current_x])
            current_x = length
            break

print(next_value)  # 349975

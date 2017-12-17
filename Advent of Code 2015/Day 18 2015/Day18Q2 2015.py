"""
Author:     Brian Mascitello
Date:       12/16/2017
Websites:   http://adventofcode.com/2015/day/18
Info:       --- Day 18: Like a GIF For Your Yard ---
            --- Part Two ---
"""

import copy
from itertools import product, starmap


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


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


data = get_data('Day18Q1 2015 Input.txt')
# data = get_data('Day18Q1 2015 Example.txt')  # Example used for testing.
# data = get_data('Day18Q2 2015 Example.txt')  # Example Q2 used for testing.

data_list = list()
for line in data.splitlines():
    temp_list = list()
    for character in line:
        temp_list.append(character)
    data_list.append(temp_list)

steps = 100
while steps:
    data_list_copy = copy.deepcopy(data_list)
    for row, line in enumerate(data_list):
        for column, character in enumerate(line):
            nearby = find_valid_neighbors(row, column, len(line))

            light_on_count = 0
            for neighbor in nearby:
                if data_list[neighbor[0]][neighbor[1]] == '#':
                    light_on_count += 1

            if data_list[row][column] == '#':
                if light_on_count != 2 and light_on_count != 3:
                    data_list_copy[row][column] = '.'
                else:
                    data_list_copy[row][column] = '#'
            else:
                if light_on_count == 3:
                    data_list_copy[row][column] = '#'
                else:
                    data_list_copy[row][column] = '.'

    # Set four corners to ON
    data_list_copy[0][0] = '#'
    data_list_copy[0][len(line) - 1] = '#'
    data_list_copy[len(line) - 1][0] = '#'
    data_list_copy[len(line) - 1][len(line) - 1] = '#'

    data_list = copy.deepcopy(data_list_copy)
    steps -= 1

# Print result to compare with guide.
# for line in data_list:
#     print(''.join(line))

count = 0
for line in data_list:
    count += line.count('#')

print(count)  # 781

"""
Author:     Brian Mascitello
Date:       12/11/2017
Websites:   http://adventofcode.com/2017/day/11
Info:       --- Day 11: Hex Ed ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def find_furthest(n, e, s, w, furthest_so_far):
    vertical = abs(n - s)
    horizontal = abs(e - w)
    distance = max(vertical, horizontal)
    return distance if distance > furthest_so_far else furthest_so_far


data = get_data("Day11Q1 2017 Input.txt")
direction_list = data.split(',')

north = 0
east = 0
south = 0
west = 0
furthest = 0

for direction in direction_list:
    if 'n' in direction:
        north += 1
    if 'e' in direction:
        east += 1
    if 's' in direction:
        south += 1
    if 'w' in direction:
        west += 1

    furthest = find_furthest(north, east, south, west, furthest)

print("Furthest: ", furthest)

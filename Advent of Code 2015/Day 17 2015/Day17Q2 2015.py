"""
Author:     Brian Mascitello
Date:       12/11/2017
Websites:   http://adventofcode.com/2015/day/17
Info:       --- Day 17: No Such Thing as Too Much ---
            --- Part Two ---
"""

import itertools


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


puzzle_data = get_data('Day17Q1 2015 Input.txt')

containers = list()
for line in puzzle_data.splitlines():
    containers.append(int(line))
containers = sorted(containers)

goal = 150
minimum_containers = goal // max(containers)

summation = 0
maximum_containers = 0
while summation < goal:
    summation += containers[maximum_containers]
    maximum_containers += 1

containers_combo_list = list()
for length in range(minimum_containers, maximum_containers):
    for combo in itertools.combinations(containers, length):
        if sum(combo) == goal:
            containers_combo_list.append(combo)

# print(len(containers_combo_list))  # 1304

smallest_container_combo = len(containers_combo_list[0])
count_of_smallest_combos = 0
for combo in containers_combo_list:
    if len(combo) == smallest_container_combo:
        count_of_smallest_combos += 1

print(count_of_smallest_combos)  # 18

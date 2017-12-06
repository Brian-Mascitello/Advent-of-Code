"""
Author:     Brian Mascitello
Date:       12/5/2017
Websites:   http://adventofcode.com/2017/day/4
Info:       --- Day 5: A Maze of Twisty Trampolines, All Alike ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day5Q1 2017 Input.txt')

data_list = list()
for line in data.splitlines():
    data_list.append(int(line))

current_position = 0
steps = 0
while current_position < len(data_list):
    moving = data_list[current_position]

    if moving >= 3:
        data_list[current_position] -= 1
    else:
        data_list[current_position] += 1

    current_position += moving
    steps += 1

print(steps, 'steps to reach the exit of the maze of jump instructions')  # 27477714

"""
Author:     Brian Mascitello
Date:       12/20/2017
Websites:   http://adventofcode.com/2017/day/19
Info:       --- Day 19: A Series of Tubes ---
            --- Part Two ---
"""


def find_start(input_grid):
    col = 0
    while True:
        tup = (0, col)
        if tup in input_grid.keys():
            if input_grid[tup] == '|':
                return 0, col
        col += 1


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day19Q1 2017 Input.txt')
# data = get_data('Day19Q1 2017 Example.txt')

lines = data.splitlines()

grid = dict()
for row, line in enumerate(lines):
    for column, character in enumerate(line):
        if character != ' ':
            location = (row, column)
            grid[location] = character

current_position = find_start(grid)
direction = 'South'
full_path = grid[current_position]
while True:
    if direction == 'North':
        new_position = (current_position[0] - 1, current_position[1])
        if new_position not in grid.keys():
            direction = 'East'
            new_position = (current_position[0], current_position[1] - 1)
        if new_position not in grid.keys():
            direction = 'West'
            new_position = (current_position[0], current_position[1] + 1)
        if new_position not in grid.keys():
            break
    elif direction == 'East':
        new_position = (current_position[0], current_position[1] - 1)
        if new_position not in grid.keys():
            direction = 'North'
            new_position = (current_position[0] - 1, current_position[1])
        if new_position not in grid.keys():
            direction = 'South'
            new_position = (current_position[0] + 1, current_position[1])
        if new_position not in grid.keys():
            break
    elif direction == 'South':
        new_position = (current_position[0] + 1, current_position[1])
        if new_position not in grid.keys():
            direction = 'East'
            new_position = (current_position[0], current_position[1] - 1)
        if new_position not in grid.keys():
            direction = 'West'
            new_position = (current_position[0], current_position[1] + 1)
        if new_position not in grid.keys():
            break
    elif direction == 'West':
        new_position = (current_position[0], current_position[1] + 1)
        if new_position not in grid.keys():
            direction = 'North'
            new_position = (current_position[0] - 1, current_position[1])
        if new_position not in grid.keys():
            direction = 'South'
            new_position = (current_position[0] + 1, current_position[1])
        if new_position not in grid.keys():
            break

    if new_position in grid.keys():
        full_path += grid[new_position]
        current_position = new_position
    else:
        break

# print(full_path)
letters_path = full_path.replace('|', '').replace('-', '').replace('+', '')
# print(letters_path)  # UICRNSDOK
print(len(full_path))  # 16064

"""
Author:     Brian Mascitello
Date:       12/7/2017
Websites:   http://adventofcode.com/2017/day/7
Info:       --- Day 7: Recursive Circus ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day7Q1 2017 Input.txt')

parent_list = list()
child_list = list()
for line in data.splitlines():
    split = line.split()
    parent_list.append(split[0])

    children = list()
    if len(split) > 2:
        children = split[3:]
    for child in children:
        child_list.append(child.strip(','))

root = set(parent_list) - set(child_list)
root = ''.join(root)  # converts to str

print(root)  # hmvwl

"""
Author:     Brian Mascitello
Date:       12/5/2017
Websites:   http://adventofcode.com/2015/day/13
Info:       --- Day 13: Knights of the Dinner Table ---
            --- Part Two ---
"""

import itertools


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day13Q1 2015 Input.txt')

member_dictionary = dict()
for line in data.splitlines():
    words = line[:-1].split(' ')

    name = words[0]
    net_happiness = int(words[3]) if words[2] == 'gain' else -int(words[3])
    neighbor = words[10]

    if words[0] not in member_dictionary.keys():
        member_dictionary[name] = dict()
    member_dictionary[name][neighbor] = net_happiness

# --- Part Two Code ---
member_dictionary['Yeti'] = dict()
for key in member_dictionary:
    member_dictionary[key]['Yeti'] = 0
    member_dictionary['Yeti'][key] = 0
del member_dictionary['Yeti']['Yeti']

maximum_happiness = None
number_of_attendees = len(member_dictionary.keys())
optimal_seating = None
for perm in itertools.permutations(member_dictionary, number_of_attendees):
    total_happiness = 0

    for index in range(-1, number_of_attendees - 1):
        name = perm[index]
        neighbor = perm[index + 1]
        total_happiness += member_dictionary[name][neighbor]
        total_happiness += member_dictionary[neighbor][name]

    if maximum_happiness is None:
        maximum_happiness = total_happiness
        optimal_seating = perm
    elif total_happiness > maximum_happiness:
        maximum_happiness = total_happiness
        optimal_seating = perm

print(optimal_seating)  # ('Alice', 'Bob', 'George', 'Eric', 'Frank', 'Yeti', 'Carol', 'Mallory', 'David')
print(maximum_happiness)  # 640

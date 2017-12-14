"""
Author:     Brian Mascitello
Date:       12/14/2017
Websites:   http://adventofcode.com/2017/day/12
Info:       --- Day 12: Digital Plumber ---
            --- Part Two ---
"""


def calculate_group_size(input_dictionary, program_ID):
    group = set()
    queue = [program_ID]

    while queue:
        for item in queue:
            group.add(item)
            [queue.append(value) for value in input_dictionary[item] if value not in group]
            queue.remove(item)

    return group.__len__()


def calculate_number_of_groups(input_dictionary):
    program_list = list(input_dictionary.keys())
    group = list()
    groups_list = list()
    queue = list()

    while program_list:
        queue.append(program_list[0])
        while queue:
            for item in queue:
                group.append(item)
                [queue.append(value) for value in input_dictionary[item] if value not in group]
                queue.remove(item)
        groups_list.append(group)
        [program_list.remove(member) for member in group if member in program_list]
        group = list()

    return groups_list.__len__()


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def write_data_dictionary(input_data):
    output_dictionary = dict()
    for line in input_data.splitlines():
        split = line.split(' ')
        split.remove('<->')
        for index in range(0, len(split)):
            split[index] = int(split[index].replace(',', ''))
        output_dictionary[split[0]] = split[1:]
    return output_dictionary


data = get_data('Day12Q1 2017 Input.txt')
# data = get_data('Day12Q1 2017 Example.txt')  # Used for testing

data_dictionary = write_data_dictionary(data)

# print(calculate_group_size(data_dictionary, 0))  # 145
print(calculate_number_of_groups(data_dictionary))

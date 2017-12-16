"""
Author:     Brian Mascitello
Date:       12/15/2017
Websites:   http://adventofcode.com/2017/day/13
Info:       --- Day 13: Packet Scanners ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def move_scanners(input_data, step_number):
    for layer in input_data.keys():
        even_odd_switch = step_number // (len(input_data[layer]) - 1) % 2
        one_location = input_data[layer].index(1)
        input_data[layer][one_location] = 0
        one_location = one_location + 1 if even_odd_switch == 0 else one_location - 1
        input_data[layer][one_location] = 1
    return input_data


def write_dictionary(input_data):
    output_data = dict()
    for line in input_data.splitlines():
        split = line.split(':')
        results = list(map(int, split))
        # Scanner location represented by a 1.
        output_data[results[0]] = [0 * index if index != 0 else 1 for index in range(results[1])]
    return output_data


data = get_data('Day13Q1 2017 Input.txt')
# data = get_data('Day13Q1 2017 Example.txt')  # Used for testing

data_dictionary = write_dictionary(data)

severity = 0
step_counter = 0
while step_counter <= max(data_dictionary.keys()):
    if step_counter in data_dictionary.keys() and data_dictionary[step_counter][0] == 1:
        severity += step_counter * len(data_dictionary[step_counter])

    data_dictionary = move_scanners(data_dictionary, step_counter)

    # print(step_counter, data_dictionary)
    step_counter += 1

print('Severity of whole trip:', severity)  # 1476

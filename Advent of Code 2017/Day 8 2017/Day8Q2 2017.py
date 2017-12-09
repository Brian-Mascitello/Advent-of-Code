"""
Author:     Brian Mascitello
Date:       12/9/2017
Websites:   http://adventofcode.com/2017/day/8
Info:       --- Day 8: I Heard You Like Registers ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def maximum_dictionary_tuple(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    maximum = max(values)
    return keys[values.index(maximum)], maximum


def variable_calculator(input_data):
    variables = dict()
    maximum = 0
    for line in input_data.splitlines():
        split = line.split()

        var1 = split[0]
        if var1 not in variables.keys():
            variables[var1] = 0

        var2 = split[4]
        if var2 not in variables.keys():
            variables[var2] = 0

        var2 = variables[var2]  # Need the value for comparison evaluation.

        if eval(str(var2) + split[5] + split[6]):
            if split[1] == 'inc':
                variables[var1] += int(split[2])
            else:
                variables[var1] -= int(split[2])

            if variables[var1] > maximum:
                maximum = variables[var1]
    return variables, maximum


# data = get_data('Day8Q1 2017 Example.txt')  # Test with example.
data = get_data('Day8Q1 2017 Input.txt')

variable_dictionary, all_time_maximum = variable_calculator(data)

print(variable_dictionary)

max_key, max_value = maximum_dictionary_tuple(variable_dictionary)

print(max_key, max_value)

print(all_time_maximum)

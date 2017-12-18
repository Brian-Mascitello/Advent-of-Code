"""
Author:     Brian Mascitello
Date:       12/17/2017
Websites:   http://adventofcode.com/2015/day/19
Info:       --- Day 19: Medicine for Rudolph ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day19Q1 2015 Input.txt')
# data = get_data('Day19Q1 2015 Example.txt')  # Example used for testing.

data_dictionary = dict()
medicine_molecule = ''
for line in data.splitlines():
    if '=>' in line:
        split = line.split('=>')
        element = split[0].strip()
        replacement = split[1].strip()
        if element in data_dictionary.keys():
            data_dictionary[element].append(replacement)
        else:
            data_dictionary[element] = [replacement]
    elif line != '':
        medicine_molecule = line

molecule_list = set()
for key in data_dictionary.keys():
    if key in medicine_molecule:
        location = 0
        while True:
            location = medicine_molecule.find(key, location)
            if location == -1:
                break
            else:
                for value in data_dictionary[key]:
                    new_molecule = medicine_molecule[:location] + value + medicine_molecule[location + len(key):]
                    molecule_list.add(new_molecule)
                location += 1

print(len(molecule_list))  # 535

"""
Author:     Brian Mascitello
Date:       12/17/2017
Websites:   http://adventofcode.com/2015/day/19
Info:       --- Day 19: Medicine for Rudolph ---
            --- Part Two ---
"""


def distill_input(molecule):
    # Each capital is eventually going to be turned into an electron e, which is lowercase.
    capital_letters = 0

    for letter in molecule:
        if 'A' <= letter <= 'Z':
            capital_letters += 1

    # Ar and Rn occurrences are unable to create new element combos and must be broken down.
    # However both Ar and Rn exist in the same complex groups, and are taken out in the same step.
    ar_count = molecule.count('Ar')
    rn_count = molecule.count('Rn')

    # Y is only found in combos with both Ar and Rn, so it is counted as a capital twice as often as a step to remove.
    y_count = molecule.count('Y') * 2

    minimum_steps = capital_letters - ar_count - rn_count - y_count - 1

    return minimum_steps


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

# print(medicine_molecule)

print(distill_input(medicine_molecule))  # 212

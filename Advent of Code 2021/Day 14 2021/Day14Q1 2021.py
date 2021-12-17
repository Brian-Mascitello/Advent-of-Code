"""
Author:     Brian Mascitello
Date:       12/16/2021
Websites:   https://adventofcode.com/2021/day/14
Info:       --- Day 14: Extended Polymerization ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day14Q1 2021 Input.txt')

    polymer_template = ''
    pair_insertion_rules = {}
    for line in data.splitlines():
        if polymer_template == '':
            polymer_template = line.strip()
        elif ' -> ' in line:
            line = line.split(' -> ')
            pair_insertion_rules[line[0]] = line[1]

    print(f'Template:\t\t{polymer_template}')

    polymer = polymer_template
    for step in range(1, 11):
        polymer_pairs = []
        for index in range(0, len(polymer) - 1, 1):
            polymer_pairs.append(polymer[index: index + 2])
        temp_polymer = ''
        count_pairs = 1
        for pair in polymer_pairs:
            if count_pairs == len(polymer_pairs):
                temp_polymer += pair[0] + pair_insertion_rules[pair] + pair[1]
            else:
                temp_polymer += pair[0] + pair_insertion_rules[pair]
                count_pairs += 1
        polymer = temp_polymer

        print(f'After step {step}:\t{polymer}')

    elements = dict.fromkeys(sorted(list(set(polymer))), 0)
    for element in elements.keys():
        elements[element] = polymer.count(element)

    print(elements)
    desired_quantity = max(elements.values()) - min(elements.values())
    print(f'Desired quantity:\t{desired_quantity}')


if __name__ == '__main__':
    main()

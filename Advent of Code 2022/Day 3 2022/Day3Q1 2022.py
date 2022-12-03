"""
Author:     Brian Mascitello
Date:       12/3/2022
Websites:   https://adventofcode.com/2022/day/3
Info:       --- Day 3: Rucksack Reorganization ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day3Q1 2022 Input.txt')

#     test_rucksacks = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

    lowercase_dictionary = {chr(i + 96): i for i in range(1, 27)}
    uppercase_dictionary = {chr(i + 64): i + 26 for i in range(1, 27)}
    priority_dictionary = lowercase_dictionary | uppercase_dictionary

    priority_summation = 0
    for line in data.splitlines():
        first_half = set(line[:len(line) // 2])
        second_half = set(line[len(line) // 2:])
        intersection_char = list(first_half.intersection(second_half))[0]
        priority_summation += priority_dictionary[intersection_char]

    print(f'The sum of the priorities is {priority_summation}.')


if __name__ == '__main__':
    main()

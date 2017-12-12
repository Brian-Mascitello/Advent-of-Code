"""
Author:     Brian Mascitello
Date:       12/11/2017
Websites:   http://adventofcode.com/2015/day/16
Info:       --- Day 16: Aunt Sue ---
            --- Part Two ---
"""


def create_aunt_dictionary(input_data):
    aunt_dict = dict()
    for line in input_data.splitlines():
        split = line.split(' ')
        fact = split[0][:-1]
        quantity = int(split[1])
        aunt_dict[fact] = quantity
    return aunt_dict


def create_puzzle_dictionary(input_data):
    puzzle_dict = dict()
    for line in input_data.splitlines():
        line = line.replace(':', '')
        line = line.replace(',', '')
        split = line.split(' ')
        number_sue = split[1]

        puzzle_dict[number_sue] = dict()
        for index in range(2, len(split), 2):
            fact = split[index]
            quantity = int(split[index + 1])
            puzzle_dict[number_sue][fact] = quantity
    return puzzle_dict


def find_aunt_sue(aunt_facts, puzzle):
    for aunt_sue in puzzle.keys():
        correct_aunt = True
        for fact in puzzle[aunt_sue]:
            if fact not in aunt_facts.keys():
                continue
            else:
                if fact == 'cats' or fact == 'trees':
                    if puzzle[aunt_sue][fact] <= aunt_facts[fact]:
                        correct_aunt = False
                        break
                elif fact == 'pomeranians' or fact == 'goldfish':
                    if puzzle[aunt_sue][fact] >= aunt_facts[fact]:
                        correct_aunt = False
                        break
                elif puzzle[aunt_sue][fact] != aunt_facts[fact]:
                    correct_aunt = False
                    break
        if correct_aunt:
            return aunt_sue


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


aunt_data = get_data("Day16Q1 2015 Facts.txt")
puzzle_data = get_data("Day16Q1 2015 Input.txt")

aunt_dictionary = create_aunt_dictionary(aunt_data)
puzzle_dictionary = create_puzzle_dictionary(puzzle_data)

print(find_aunt_sue(aunt_dictionary, puzzle_dictionary))  # 241

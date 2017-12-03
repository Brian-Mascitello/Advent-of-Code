"""
Author:     Brian Mascitello
Date:       12/2/2017
Websites:   http://adventofcode.com/2015/day/11
Info:       --- Day 11: Corporate Policy ---
"""


def double_letter_generator():
    doubles_list = list()
    double_letter = 'aa'
    while double_letter != '{{':
        doubles_list.append(double_letter)
        double_letter = straight_increaser(double_letter)
    return doubles_list


def pair_checker(input_string, pairs):
    count = 0
    for pair in pairs:
        if pair in input_string:
            count += 1
    if count >= 2:
        return True
    else:
        return False


def poison_letter(input_string):
    if 'i' in input_string:
        return False
    elif 'l' in input_string:
        return False
    elif 'o' in input_string:
        return False
    else:
        return True


def puzzle_checker(input_string, pairs, straights):
    if run_finder(input_string, straights) and poison_letter(input_string) and pair_checker(input_string, pairs):
        return True
    else:
        return False


def puzzle_incrementer(input_string):
    output = str()
    for letter in reversed(input_string):
        if letter == 'z':
            output += 'a'
            continue
        else:
            output += chr(ord(letter) + 1)
            break
    output = input_string[:len(input_string) - len(output)] + output[::-1]
    return output


def run_finder(input_string, straights):
    for straight in straights:
        if straight in input_string:
            return True
    return False


def straight_generator():
    straights_list = list()
    straight = 'abc'
    while straight != 'yz{':
        straights_list.append(straight)
        straight = straight_increaser(straight)
    return straights_list


def straight_increaser(input_string):
    output = str()
    for letter in input_string:
        output += chr(ord(letter) + 1)
    return output


puzzle_input = 'hepxcrrq'

double_letters = double_letter_generator()
straight_combos = straight_generator()
puzzle_output = puzzle_input
iterate = False
while not iterate:
    puzzle_output = puzzle_incrementer(puzzle_output)
    iterate = puzzle_checker(puzzle_output, double_letters, straight_combos)

print(puzzle_output)  # hepxxyzz

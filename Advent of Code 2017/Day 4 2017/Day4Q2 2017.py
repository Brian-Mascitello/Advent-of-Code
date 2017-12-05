"""
Author:     Brian Mascitello
Date:       12/4/2017
Websites:   http://adventofcode.com/2017/day/4
Info:       --- Day 4: High-Entropy Passphrases ---
            --- Part Two ---
"""

import itertools


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day4Q1 2017 Input.txt')

valid_passphrases = 0
for line in data.splitlines():
    add = True
    full_perms = list()
    words = line.split()
    for word in words:
        perms = list(set(''.join(item) for item in itertools.permutations(word, len(word))))
        full_perms.extend(perms)
        if line.count(word) > 1:
            add = False
            break

    if add:
        permutation_counter = 0
        for perm in full_perms:
            if perm in words:
                permutation_counter += 1

        if permutation_counter == len(words):
            valid_passphrases += 1

print(valid_passphrases)  # 231

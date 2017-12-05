"""
Author:     Brian Mascitello
Date:       12/4/2017
Websites:   http://adventofcode.com/2017/day/4
Info:       --- Day 4: High-Entropy Passphrases ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day4Q1 2017 Input.txt')

valid_passphrases = 0
for line in data.splitlines():
    add = True
    for word in line.split():
        if line.count(word) > 1:
            add = False
            break
    if add:
        valid_passphrases += 1

print(valid_passphrases)  # 337

"""
Author:     Brian Mascitello
Date:       12/2/2018
Websites:   https://adventofcode.com/2018/day/2
Info:       --- Day 2: Inventory Management System ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day2Q1 2018 Input.txt')

two_count = 0
three_count = 0
for line in data.splitlines():
    two_check = False
    three_check = False

    for letter in line:
        letter_count = line.count(letter)

        if letter_count == 2:
            two_check = True
        elif letter_count == 3:
            three_check = True

    if two_check:
        two_count += 1

    if three_check:
        three_count += 1

checksum = two_count * three_count

print(checksum)  # 7221

"""
Author:     Brian Mascitello
Date:       12/5/2017
Websites:   http://adventofcode.com/2015/day/12
Info:       --- Day 12: JSAbacusFramework.io ---
"""

import re


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day12Q1 2015 Input.txt')

regex = r'(-?\d+)'

input_numbers = map(int, re.findall(regex, data))

summation = sum(input_numbers)

print(summation)  # 191164

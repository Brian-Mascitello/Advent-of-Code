"""
Author:     Brian Mascitello
Date:       12/1/2018
Websites:   https://adventofcode.com/2018/day/1
Info:       --- Day 1: Chronal Calibration ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day1Q1 2018 Input.txt')

summation = 0
for line in data.splitlines():
    summation += int(line)

print(summation)  # 437

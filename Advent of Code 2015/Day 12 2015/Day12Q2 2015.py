"""
Author:     Brian Mascitello
Date:       12/5/2017
Websites:   http://adventofcode.com/2015/day/12
Info:       --- Day 12: JSAbacusFramework.io ---
            --- Part Two ---
"""

import json

data = json.load(open('Day12Q1 2015 Input.txt'))


def calculate_sum(input_data):
    summation = 0
    if not isinstance(input_data, (dict, int, list)):
        return 0
    else:
        if isinstance(input_data, dict):
            if "red" in input_data.values():
                return 0
            for value in input_data.values():
                summation += calculate_sum(value)
        elif isinstance(input_data, int):
            return summation + input_data
        else:
            for item in input_data:
                summation += calculate_sum(item)
        return summation


print(calculate_sum(data))  # 87842

"""
Author:     Brian Mascitello
Date:       12/9/2017
Websites:   http://adventofcode.com/2017/day/9
Info:       --- Day 9: Stream Processing ---
"""

import re


def clean_data(input_text):
    modified_data = input_text

    # Clean up ignores and remove them after activation.
    while '!' in modified_data:
        index = modified_data.index('!')
        modified_data = modified_data[:index] + modified_data[index + 2:]

    # Clean up trash, anything between and including <> to be removed.
    regex = r'\<(.*?)\>'
    modified_data = re.sub(regex, '', modified_data)

    # Remove unnecessary commas.
    modified_data = modified_data.replace(',', '')

    return modified_data


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def score_calculator(input_text):
    score = 0
    depth = 0
    for character in input_text:
        if character == '{':
            depth += 1
            score += depth
        else:
            depth -= 1
    return score


data = get_data('Day9Q1 2017 Input.txt')

data = clean_data(data)

total_score = score_calculator(data)

print(total_score)  # 11089

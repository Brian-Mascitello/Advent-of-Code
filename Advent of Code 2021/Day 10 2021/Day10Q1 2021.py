"""
Author:     Brian Mascitello
Date:       12/11/2021
Websites:   https://adventofcode.com/2021/day/10
Info:       --- Day 10: Syntax Scoring ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day10Q1 2021 Input.txt')

    lines = []
    for line in data.splitlines():
        lines.append(list(line))

    illegal_chars = []
    for line in lines:
        chunk_openers = []
        for char in line:
            if char in '([{<':
                chunk_openers.append(char)
            else:
                if chunk_openers[-1] == '(' and char == ')':
                    chunk_openers.pop()
                elif chunk_openers[-1] == '[' and char == ']':
                    chunk_openers.pop()
                elif chunk_openers[-1] == '{' and char == '}':
                    chunk_openers.pop()
                elif chunk_openers[-1] == '<' and char == '>':
                    chunk_openers.pop()
                else:
                    illegal_chars.append(char)
                    break

    syntax_score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    illegal_scores = [syntax_score_dict[index] for index in illegal_chars]
    illegal_sum = sum(illegal_scores)
    print(illegal_sum)


main()

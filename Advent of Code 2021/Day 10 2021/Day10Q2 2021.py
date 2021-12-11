"""
Author:     Brian Mascitello
Date:       12/11/2021
Websites:   https://adventofcode.com/2021/day/10
Info:       --- Day 10: Syntax Scoring ---
            --- Part Two ---
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

    illegal_lines = []
    incomplete_chunks = []
    for line in lines:
        add_chunk = True
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
                    add_chunk = False
                    illegal_lines.append(line)
                    break
        if add_chunk:
            incomplete_chunks.append(chunk_openers[::-1])

    # incomplete_lines = [item for item in lines if item not in illegal_lines]
    # print(incomplete_lines)
    # print(incomplete_chunks)

    syntax_score_dict = {'(': 1, '[': 2, '{': 3, '<': 4}
    completion_scores = []
    for chunk in incomplete_chunks:
        current_score = 0
        for char in chunk:
            current_score *= 5
            current_score += syntax_score_dict[char]
        completion_scores.append(current_score)

    completion_scores.sort()
    middle_score = completion_scores[len(completion_scores)//2]
    print(middle_score)


main()

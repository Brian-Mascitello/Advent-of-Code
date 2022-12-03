"""
Author:     Brian Mascitello
Date:       12/3/2022
Websites:   https://adventofcode.com/2022/day/2#part2
Info:       --- Day 2: Rock Paper Scissors ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day2Q1 2022 Input.txt')

    # strategy_guide_example = """A Y
    # B X
    # C Z"""

    score_dictionary = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }

    total_score = 0
    for line in data.splitlines():
        total_score += score_dictionary[line.strip()]

    print(f'The total score following the strategy guide is {total_score} points.')


if __name__ == '__main__':
    main()

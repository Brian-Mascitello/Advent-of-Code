"""
Author:     Brian Mascitello
Date:       12/2/2022
Websites:   https://adventofcode.com/2022/day/2
Info:       --- Day 2: Rock Paper Scissors ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day2Q1 2022 Input.txt')

    strategy_guide_example = """A Y
    B X
    C Z"""

    total_score = 0
    for line in data.splitlines():
        round_list = line.strip().split(' ')

        # Shape you selected points.
        round_score = ord(round_list[1]) - 87

        # Outcome of the round points.
        round_ord_difference = ord(round_list[1]) - ord(round_list[0])

        # Win 21 or 24.
        if round_ord_difference in (21, 24):
            round_score += 6
        # Draw 23.
        elif round_ord_difference == 23:
            round_score += 3
        # Lose 22 or 25, no need to add zero.

        total_score += round_score

    print(f'The total score following the strategy guide is {total_score} points.')


if __name__ == '__main__':
    main()

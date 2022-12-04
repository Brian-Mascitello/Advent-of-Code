"""
Author:     Brian Mascitello
Date:       12/3/2022
Websites:   https://adventofcode.com/2022/day/4#part2
Info:       --- Day 4: Camp Cleanup ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day4Q1 2022 Input.txt')

    # section_assignments = """2-4,6-8
    # 2-3,4-5
    # 5-7,7-9
    # 2-8,3-7
    # 6-6,4-6
    # 2-6,4-8"""

    overlap_counter = 0
    for pair in data.splitlines():
        section = pair.split(',')
        x0, y0 = map(int, section[0].split('-'))
        x1, y1 = map(int, section[1].split('-'))
        section0_ints = set(range(x0, y0 + 1))
        section1_ints = set(range(x1, y1 + 1))
        overlap_len = len(section0_ints.intersection(section1_ints))
        if overlap_len:
            overlap_counter += 1

    print(f'There are {overlap_counter} assignment pairs that fully contain the other?')


if __name__ == '__main__':
    main()

"""
Author:     Brian Mascitello
Date:       12/5/2021
Websites:   https://adventofcode.com/2021/day/1
Info:       --- Day 1: Sonar Sweep ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day1Q1 2021 Input.txt')

    depth_increased_counter = 0
    last_depth = 0
    for line in data.splitlines():
        current_depth = int(line)
        if last_depth != 0:
            if current_depth > last_depth:
                depth_increased_counter = depth_increased_counter + 1
        last_depth = current_depth

    print(depth_increased_counter)


main()

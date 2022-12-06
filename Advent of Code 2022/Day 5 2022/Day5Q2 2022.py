"""
Author:     Brian Mascitello
Date:       12/5/2022
Websites:   https://adventofcode.com/2022/day/5#part2
Info:       --- Day 5: Supply Stacks ---
            --- Part Two ---
"""

import re


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day5Q1 2022 Input.txt')

#     test_input = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

    crates = []
    rearrangement_procedures = []

    whitespace_flag = True
    for line in data.splitlines():
        if line == '':
            whitespace_flag = False
        elif whitespace_flag:
            temp_line = re.findall('.{2,4}', line)
            temp_line = [re.sub(r'\W+', '', temp) for temp in temp_line]
            crates.append(temp_line)
        else:
            temp_line = list(map(int, re.findall('\d+', line)))
            rearrangement_procedures.append(temp_line)

    # Reorder and remove numeric crates.
    for crate in crates:
        while len(crate) < len(max(crates, key=len)):
            crate.append('')
    crates = crates[::-1][1:]

    # Convert crates to a dictionary of lists.
    crate_dict = {}
    for index in range(1, len(max(crates, key=len)) + 1):
        crate_dict[index] = [x[index - 1] for x in crates if x[index - 1] != '']

    # Follow the procedure to move the crates around in the proper order.
    for task in rearrangement_procedures:
        temp_stack = []
        for index in range(0, task[0]):
            temp_stack.append(crate_dict[task[1]].pop())
        crate_dict[task[2]].extend(temp_stack[::-1])

    # Solve the message by combining the top letter of each stack of crates.
    message = ''
    for key, value in crate_dict.items():
        message += value[-1]
    print(message)


if __name__ == '__main__':
    main()

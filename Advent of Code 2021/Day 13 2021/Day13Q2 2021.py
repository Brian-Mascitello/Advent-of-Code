"""
Author:     Brian Mascitello
Date:       12/13/2021
Websites:   https://adventofcode.com/2021/day/13
Info:       --- Day 13: Transparent Origami ---
            --- Part Two ---
"""

import numpy as np


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day13Q1 2021 Input.txt')

    list_of_dots = []
    fold_instructions = []
    for line in data.splitlines():
        if ',' in line:
            list_of_dots.append(tuple(map(int, line.split(','))))
        elif '=' in line:
            line = line[11:]
            line = line.split('=')
            fold_instructions.append(tuple([line[0], int(line[1])]))

    max_x = max(list_of_dots, key=lambda x: x[0])[0] + 1
    max_y = max(list_of_dots, key=lambda x: x[1])[1] + 1

    # x, y flipped in np array.
    transparent_paper = np.zeros(shape=(max_y, max_x), dtype=int)

    for dot in list_of_dots:
        transparent_paper[dot[1]][dot[0]] = 1

    visible_dots = 0
    for fold in fold_instructions:
        if fold[0] == 'x':
            transparent_paper_left = transparent_paper[:, :fold[1]]
            transparent_paper_right = np.fliplr(transparent_paper[:, fold[1] + 1:])
            transparent_paper = np.add(transparent_paper_left, transparent_paper_right)
        elif fold[0] == 'y':
            transparent_paper_top = transparent_paper[:fold[1], ]
            transparent_paper_bottom = np.flipud(transparent_paper[fold[1] + 1:, ])
            transparent_paper = np.add(transparent_paper_top, transparent_paper_bottom)

        transparent_paper = np.where(transparent_paper > 0, 1, 0)
        visible_dots = np.count_nonzero(transparent_paper)
        # break

    print(transparent_paper)
    print(visible_dots)

    transparent_paper_print = np.where(transparent_paper > 0, '#', '.')
    transparent_paper_print.astype(str).tolist()
    transparent_paper_print = [''.join(row) for row in transparent_paper_print]
    for row in transparent_paper_print:
        print(row)


if __name__ == '__main__':
    main()

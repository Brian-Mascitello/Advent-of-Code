"""
Author:     Brian Mascitello
Date:       12/6/2021
Websites:   https://adventofcode.com/2021/day/4
Info:       --- Day 4: Giant Squid ---
"""

import numpy as np


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    bingo_grid_lists = []
    current_card = []
    random_bingo_numbers = 0
    for data in get_data('Day4Q1 2021 Input.txt').splitlines():
        if random_bingo_numbers == 0:
            random_bingo_numbers = list(map(int, data.split(',')))
        elif data != '':
            current_card.append(list(map(int, data.split())))
            if len(current_card) == 5:
                bingo_grid_lists.append(current_card)
                current_card = []

    bingo_arrays = []
    for card in bingo_grid_lists:
        bingo_arrays.append(np.array(card))

    winner = False
    for number in random_bingo_numbers:
        if winner:
            break

        for index in range(len(bingo_arrays)):
            if winner:
                break

            if number in bingo_arrays[index]:
                bingo_arrays[index] = np.where(bingo_arrays[index] == number, 0, bingo_arrays[index])
                count_zeros = np.where(bingo_arrays[index] == 0)[0].size
                if count_zeros > 4:
                    if 0 in np.count_nonzero(bingo_arrays[index], axis=0) or \
                            0 in np.count_nonzero(bingo_arrays[index], axis=1):
                        winner = True
                        print(bingo_arrays[index])
                        print(bingo_arrays[index].sum() * number)


main()

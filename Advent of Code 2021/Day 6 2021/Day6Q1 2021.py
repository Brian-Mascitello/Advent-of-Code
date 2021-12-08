"""
Author:     Brian Mascitello
Date:       12/7/2021
Websites:   https://adventofcode.com/2021/day/6
Info:       --- Day 6: Lanternfish ---
"""

import numpy as np


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day6Q1 2021 Input.txt')
    data = list(map(int, data.split(',')))

    # initial_state = np.array([3, 4, 3, 1, 2])
    initial_state = np.array(data)
    state_after_days = initial_state.copy()
    print(state_after_days)
    for days in range(1, 81):
        spawn = state_after_days[np.where(state_after_days == 0)].size
        state_after_days = state_after_days - 1
        state_after_days = np.where(state_after_days == -1, 6, state_after_days)
        spawn_list = [8] * spawn
        state_after_days = np.append(state_after_days, spawn_list)
        print(state_after_days, int(state_after_days.size))


main()

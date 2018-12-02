"""
Author:     Brian Mascitello
Date:       12/1/2018
Websites:   https://adventofcode.com/2018/day/1
Info:       --- Day 1: Chronal Calibration ---
            --- Part Two ---
"""

import time


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day1Q1 2018 Input.txt')

current_time = 0
loops = 0
match_found = False
start_time = time.time()
summation = 0
sum_set = set()
while not match_found and loops < 1000:
    for line in data.splitlines():
        summation += int(line)

        if summation in sum_set:
            match_found = True
            break
        else:
            sum_set.add(summation)

    current_time = time.time() - start_time

    if not match_found:
        loops += 1

        # Used to time the process. Sets are way more efficient than lists.
        # if loops % 10 == 0:
        #     current_time = time.time() - start_time
        #     print('Completed {0} loops in {1} seconds.'.format(loops, round(current_time, 3)))

print('The first repeated frequency is {0}.'.format(summation))  # 655
print('Completed {0} loops in {1} seconds.'.format(loops, round(current_time, 3)))

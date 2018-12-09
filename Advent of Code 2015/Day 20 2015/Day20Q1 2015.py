"""
Author:     Brian Mascitello
Date:       12/2/2018
Websites:   https://adventofcode.com/2015/day/20
Info:       --- Day 20: Infinite Elves and Infinite Houses ---
"""

import math
import time


factors = set()  # removes the need to check if x == house // x before appending to a list
goal = 34000000 // 10
house = 1
presents = 0
start_time = time.time()

while presents < goal:

    for x in range(1, int(math.sqrt(house))):
        if house % x == 0:
            factors.add(x)
            factors.add(house // x)

    presents = sum(factors)

    if presents < goal:
        factors = set()  # faster than clearing with factors.clear()
        house += 1

    # if house % 10000 == 0:
    #     current_time = time.time() - start_time
    #     print('Completed {0} loops in {1} seconds.'.format(house, round(current_time, 3)))

print('House {0} got {1} presents.'.format(house, presents))
final_time = time.time() - start_time
print('Found in {0} seconds.'.format(round(final_time, 3)))


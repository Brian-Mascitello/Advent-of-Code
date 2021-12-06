"""
Author:     Brian Mascitello
Date:       12/9/2018
Websites:   https://adventofcode.com/2015/day/20
Info:       --- Day 20: Infinite Elves and Infinite Houses ---
            --- Part Two ---
"""

import math
import time

gift_multiplier = 11
goal = 34000000
house = 1
maximum_visits = 50
presents = 0
records = dict()
start_time = time.time()


def remove_tired_elves(facts, max_visits):
    fresh_elves = list()

    for item in facts:
        if item in records:
            if records[item] < max_visits:
                fresh_elves.append(item)
        else:
            fresh_elves.append(item)

    return fresh_elves


def update_records(facts):
    for item in facts:
        if item in records:
            records[item] += 1
        else:
            records[item] = 1


while presents < goal:
    # factors = set()  # removes the need to check if x == house // x before appending to a list
    factors = list()  # faster than set on my pc

    for x in range(1, int(math.sqrt(house))):
        if house % x == 0:
            # factors.add(x)
            # factors.add(house // x)

            factors.append(x)

            if not x == house // x:
                factors.append(house // x)

    factors = remove_tired_elves(factors, maximum_visits)

    presents = sum(factors) * gift_multiplier

    if presents < goal:
        update_records(factors)
        house += 1

    if house % 10000 == 0:
        current_time = time.time() - start_time
        print('Completed {0} loops in {1} seconds.'.format(house, round(current_time, 3)))

print('House {0} got {1} presents.'.format(house, presents))
final_time = time.time() - start_time
print('Found in {0} seconds.'.format(round(final_time, 3)))
print(sorted(factors))

# House 831600 got 35780206 presents.
# Found in 65.293 seconds.
# [16632, 17325, 18480, 18900, 19800, 20790, 23100, 23760, 25200, 27720, 29700, 30800, 33264, 34650, 37800, 39600,
# 41580, 46200, 51975, 55440, 59400, 69300, 75600, 83160, 92400, 103950, 118800, 138600, 166320, 207900, 277200,
# 415800, 831600]

"""
Author:     Brian Mascitello
Date:       12/17/2017
Websites:   http://adventofcode.com/2017/day/17
Info:       --- Day 17: Spinlock ---
            --- Part Two ---
"""

from collections import deque

data = 370
spinlock_deque = deque([0])

for number in range(1, 50000001):
    spinlock_deque.rotate(-data)
    spinlock_deque.append(number)

zero_index = spinlock_deque.index(0)
print(spinlock_deque[zero_index + 1])  # 1244

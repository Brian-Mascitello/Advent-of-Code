"""
Author:     Brian Mascitello
Date:       12/17/2017
Websites:   http://adventofcode.com/2017/day/17
Info:       --- Day 17: Spinlock ---
"""

from collections import deque

data = 370
spinlock_deque = deque([0])

for number in range(1, 2018):
    spinlock_deque.rotate(-data)
    spinlock_deque.append(number)

print(spinlock_deque[0])  # 1244

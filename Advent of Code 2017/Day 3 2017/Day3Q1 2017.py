"""
Author:     Brian Mascitello
Date:       12/4/2017
Websites:   http://adventofcode.com/2017/day/3
Info:       --- Day 3: Spiral Memory ---
"""

import math

puzzle_input = 347991

square_root_input = math.sqrt(puzzle_input)  # Long decimal likely.
if square_root_input.is_integer():
    large_square = int(square_root_input - 1)
else:
    large_square = math.ceil(square_root_input)  # Rounded up.

# puzzle_input lies inside large_square perimeter.
if not large_square & 1:
    large_square += 1

# Minimum and maximum steps to get to destination.
maximum_steps = large_square - 1
minimum_steps = maximum_steps // 2

current_position = large_square ** 2
distance = maximum_steps
next_change = 'decreasing'

while current_position > puzzle_input:
    current_position -= 1

    if next_change == 'decreasing':
        distance -= 1
    else:
        distance += 1

    if distance == minimum_steps:
        next_change = 'increasing'
    elif distance == maximum_steps:
        next_change = 'decreasing'

print(distance)  # 480

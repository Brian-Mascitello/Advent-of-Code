"""
Author:     Brian Mascitello
Date:       12/2/2017
Websites:   http://adventofcode.com/2015/day/10
Info:       --- Day 10: Elves Look, Elves Say ---
"""

puzzle_input = '1113122113'

temporary_input = puzzle_input
for x in range(0, 40):
    previous = None
    current = None
    number_repetitions = 1
    puzzle_output = str()
    for digit in temporary_input:
        current = digit
        if previous == current:
            number_repetitions += 1
        else:
            if previous is not None:
                puzzle_output += str(number_repetitions)
                puzzle_output += str(previous)
            previous = current
            number_repetitions = 1
    puzzle_output += str(number_repetitions)
    puzzle_output += str(previous)
    temporary_input = puzzle_output
    
print(len(puzzle_output))  # 360154

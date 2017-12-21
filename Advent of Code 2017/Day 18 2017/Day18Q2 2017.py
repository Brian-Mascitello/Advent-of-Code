"""
Author:     Brian Mascitello
Date:       12/18/2017
Websites:   http://adventofcode.com/2017/day/18
Info:       --- Day 18: Duet ---
            --- Part Two ---

Credit to https://www.reddit.com/user/vash3r
https://www.reddit.com/r/adventofcode/comments/7kj35s/2017_day_18_solutions/dreth75/

I was frustrated with how my code was turning out, and near verbatim copied vash3r's code. I liked the way they had a
function to check if a value was a number or letter as opposed to my 'try: int(value) except ValueError: dict[value]'.
"""

from collections import defaultdict


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def in_alphabet(value):
    if value in 'abcdefghijklmnopqrstuvwxyz':
        return current_registers[value]
    return int(value)


data = get_data('Day18Q1 2017 Input.txt')
# data = get_data('Day18Q2 2017 Example.txt')  # Used for testing.

lines = [item.split(' ') for item in data.splitlines()]

# Registers for both programs.
program_0_registers = defaultdict(int)
program_1_registers = defaultdict(int)
register_list = [program_0_registers, program_1_registers]

# Initialize value p for each program.
program_0_registers['p'] = 0
program_1_registers['p'] = 1

# Number of times program_1 sent values to program_2.
program_1_sends = 0

# Program instruction indices, which line in lines of data they are on.
index = [0, 0]

# Queues for each program.
queues = [[], []]

# State each program is currently in.
# 'Running' = Able to be ran.
# 'Receiving' = Waiting for other program to send data.
# 'End' = Finished, will no longer send data.
state = ['Running', 'Running']

# Current program being executed.
current_program = 0
current_registers = register_list[current_program]
current_index = index[current_program]

while True:
    if lines[current_index][0] == 'snd':
        if current_program == 1:
            program_1_sends += 1
        queues[current_program].append(in_alphabet(lines[current_index][1]))
    elif lines[current_index][0] == 'set':
        current_registers[lines[current_index][1]] = in_alphabet(lines[current_index][2])
    elif lines[current_index][0] == 'add':
        current_registers[lines[current_index][1]] += in_alphabet(lines[current_index][2])
    elif lines[current_index][0] == 'mul':
        current_registers[lines[current_index][1]] *= in_alphabet(lines[current_index][2])
    elif lines[current_index][0] == 'mod':
        current_registers[lines[current_index][1]] %= in_alphabet(lines[current_index][2])
    elif lines[current_index][0] == 'rcv':
        if queues[1 - current_program]:
            state[current_program] = 'Running'
            current_registers[lines[current_index][1]] = queues[1 - current_program].pop(0)
        else:  #
            if state[1 - current_program] == 'End':
                break
            if len(queues[current_program]) == 0 and state[1 - current_program] == 'Receiving':
                break
            index[current_program] = current_index
            state[current_program] = 'Receiving'
            current_program = 1 - current_program
            current_index = index[current_program] - 1
            current_registers = register_list[current_program]
    elif lines[current_index][0] == 'jgz':
        if in_alphabet(lines[current_index][1]) > 0:
            current_index += in_alphabet(lines[current_index][2]) - 1
    current_index += 1
    if not 0 <= current_index < len(lines):
        if state[1 - current_program] == 'End':
            break
        state[current_program] = 'End'
        index[current_program] = current_index
        current_program = 1 - current_program
        current_index = index[current_program]
        current_registers = register_list[current_program]

print(program_1_sends)

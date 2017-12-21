"""
Author:     Brian Mascitello
Date:       12/18/2017
Websites:   http://adventofcode.com/2017/day/18
Info:       --- Day 18: Duet ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day18Q1 2017 Input.txt')
# data = get_data('Day18Q1 2017 Example.txt')  # Used for testing

index = 0
last_sound_played = 0
lines = data.splitlines()
sound_dictionary = dict()
while index < len(lines):
    split = lines[index].split(' ')
    instruction = split[0]
    register = split[1]

    if register not in sound_dictionary:
        sound_dictionary[register] = 0

    if instruction == 'snd':
        last_sound_played = sound_dictionary[register]
    elif instruction == 'set':
        try:
            sound_dictionary[register] = int(split[2])
        except ValueError:
            sound_dictionary[register] = sound_dictionary[split[2]]
    elif instruction == 'add':
        try:
            sound_dictionary[register] += int(split[2])
        except ValueError:
            sound_dictionary[register] += sound_dictionary[split[2]]
    elif instruction == 'mul':
        try:
            sound_dictionary[register] *= int(split[2])
        except ValueError:
            sound_dictionary[register] *= sound_dictionary[split[2]]
    elif instruction == 'mod':
        try:
            sound_dictionary[register] %= int(split[2])
        except ValueError:
            sound_dictionary[register] %= sound_dictionary[split[2]]
    elif instruction == 'rcv':
        if sound_dictionary[register] != 0:
            print(last_sound_played)  # 8600
            break
    else:  # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
        if sound_dictionary[register] > 0:
            index += int(split[2]) - 1

    index += 1

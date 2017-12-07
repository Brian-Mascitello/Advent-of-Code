"""
Author:     Brian Mascitello
Date:       12/7/2017
Websites:   http://adventofcode.com/2017/day/6
Info:       --- Day 6: Memory Reallocation ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def memory_reallocate(memory):
    memory_to_redistribute = max(memory)
    index = memory.index(memory_to_redistribute)
    memory[index] = 0
    while memory_to_redistribute > 0:
        index += 1
        if index == len(memory):
            index = 0
        memory[index] += 1
        memory_to_redistribute -= 1
    return memory


data = get_data('Day6Q1 2017 Input.txt')

memory_banks = list()
for item in data.split():
    memory_banks.append(int(item))

historical_memory = list()
while memory_banks not in historical_memory:
    historical_memory.append(memory_banks.copy())
    memory_banks = memory_reallocate(memory_banks)

print(len(historical_memory) - historical_memory.index(memory_banks))  # 8038

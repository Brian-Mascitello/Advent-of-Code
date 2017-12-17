"""
Author:     Brian Mascitello
Date:       12/16/2017
Websites:   http://adventofcode.com/2017/day/15
Info:       --- Day 15: Dueling Generators ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def last_16_binary(input_number):
    output_binary = bin(input_number)[2:]
    output_binary = output_binary.zfill(16)
    output_binary = output_binary[-16:]
    return output_binary


data = get_data('Day15Q1 2017 Input.txt')

# Test Case
# generator_A = 65
# generator_B = 8921
#
# factor_A = 16807
# factor_B = 48271
#
# max_int = 2147483647
#
# judge = 0
# for index in range(0, 40000000):
#     generator_A = (factor_A * generator_A) % max_int
#     generator_B = (factor_B * generator_B) % max_int
#
#     binary_A = last_16_binary(generator_A)
#     binary_B = last_16_binary(generator_B)
#
#     if binary_A == binary_B:
#         judge += 1
#
# print(judge)  # 588

input_list = list()
for lines in data.splitlines():
    split = lines.split(' ')
    input_list.append(int(split[-1]))

generator_A = input_list[0]
generator_B = input_list[1]

factor_A = 16807
factor_B = 48271

max_int = 2147483647

judge = 0
for index in range(0, 40000000):
    generator_A = (factor_A * generator_A) % max_int
    generator_B = (factor_B * generator_B) % max_int

    binary_A = last_16_binary(generator_A)
    binary_B = last_16_binary(generator_B)

    if binary_A == binary_B:
        judge += 1

print(judge)  # 567


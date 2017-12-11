"""
Author:     Brian Mascitello
Date:       12/10/2017
Websites:   http://adventofcode.com/2017/day/10
Info:       --- Day 10: Knot Hash ---
            --- Part Two ---
"""

import copy
from functools import reduce


def construct_dense_hash(sparse_hash):
    constructed_hash = list()
    groups_of_sixteen = [sparse_hash[index:index + 16] for index in range(0, len(sparse_hash), 16)]
    for group in groups_of_sixteen:
        xor = reduce((lambda x, y: x ^ y), group)
        constructed_hash.append(xor)
    return constructed_hash


def determine_ordinals_list(input_data):
    data_length_list = list()
    for item in input_data:
        data_length_list.append(ord(item))
    return data_length_list


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def knot_hash(input_list, length_list, rounds):
    copy_input_list = copy.copy(input_list)
    current_position = 0
    skip_size = 0
    while rounds:
        for item in length_list:
            end_position = (current_position + item) % len(copy_input_list)
            if current_position <= end_position:
                copy_input_list[current_position: end_position] = list(
                    reversed(copy_input_list[current_position: end_position]))
            else:
                sub_list = copy_input_list[current_position:]
                sub_list_first_size = len(sub_list)
                sub_list.extend(copy_input_list[:end_position])
                sub_list.reverse()  # Reverses the sub_list before modifying input_list values.
                copy_input_list[current_position:] = sub_list[:sub_list_first_size]
                copy_input_list[:end_position] = sub_list[sub_list_first_size:]
            current_position = (end_position + skip_size) % len(copy_input_list)
            skip_size += 1
        rounds -= 1
    return copy_input_list


def list_to_hex_string(list_of_numbers):
    hex_str = ''
    for number in list_of_numbers:
        hex_str += hex(number)[2:]
    return hex_str


# standard_list = list(range(256))
# data = get_data('Day10Q1 2017 Input.txt')
# data_split = data.split(',')
# lengths_list = list(map(int, data_split))
#
# # ex_lengths_list = [3, 4, 1, 5]
# # ex_input_list = [0, 1, 2, 3, 4]
# # ex_knot_list = knot_hash(ex_input_list, ex_lengths_list)
# # print(ex_knot_list)  # [3, 4, 2, 1, 0]
# # print(ex_knot_list[0] * ex_knot_list[1])  # 12
#
# knot_list = knot_hash(standard_list, lengths_list)
# print(knot_list)
# print(knot_list[0] * knot_list[1])  # 9656

standard_list = list(range(256))
data = get_data('Day10Q1 2017 Input.txt')
lengths_list = determine_ordinals_list(data)
lengths_list.extend([17, 31, 73, 47, 23])
knot_list = knot_hash(standard_list, lengths_list, 64)
dense_hash = construct_dense_hash(knot_list)
hexadecimal_string = list_to_hex_string(dense_hash)
print(hexadecimal_string)

"""
Author:     Brian Mascitello
Date:       12/15/2017
Websites:   http://adventofcode.com/2017/day/14
Info:       --- Day 14: Disk Defragmentation ---
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
        temp_list = list()
        for char in item:
            temp_list.append(ord(char))
        temp_list.extend([17, 31, 73, 47, 23])
        data_length_list.append(temp_list)
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


def make_data_list(input_data, rounds):
    output_list = list()
    for index in range(0, rounds):
        output_list.append(input_data + '-' + str(index))
    return output_list


standard_list = list(range(256))
# data = 'flqrgnkx'  # test 8108
data = 'jxqlasbh'
data_list = make_data_list(data, 128)
lengths_list = determine_ordinals_list(data_list)

knots_list = list()
for length in lengths_list:
    knots_list.append(knot_hash(standard_list, length, 64))

dense_list = list()
for knot in knots_list:
    dense_list.append(construct_dense_hash(knot))

hex_list = list()
for dense in dense_list:
    hex_list.append(list_to_hex_string(dense))

binary_list = list()
for hex_value in hex_list:
    temp_bin = list()
    for character in hex_value:
        # https://stackoverflow.com/questions/1425493/convert-hex-to-binary
        temp_bin.append(bin(int(character, 16))[2:].zfill(4))
    binary_list.append(''.join(temp_bin))

count_used_squares = 0
for binary_value in binary_list:
    for character in binary_value:
        if character == '1':
            count_used_squares += 1

print(count_used_squares)  # 8140

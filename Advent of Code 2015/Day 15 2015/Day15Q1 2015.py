"""
Author:     Brian Mascitello
Date:       12/11/2017
Websites:   http://adventofcode.com/2015/day/15
Info:       --- Day 15: Science for Hungry People ---
"""

import itertools


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def obtain_high_score(ingredient_dict):
    best_combination_score = 0
    for combo in itertools.combinations_with_replacement(ingredient_dict.keys(), 100):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0

        for ingredient in combo:
            capacity += ingredient_dict[ingredient]['capacity']
            durability += ingredient_dict[ingredient]['durability']
            flavor += ingredient_dict[ingredient]['flavor']
            texture += ingredient_dict[ingredient]['texture']

        if capacity < 1 or durability < 1 or flavor < 1 or texture < 1:
            continue

        combo_score = capacity * durability * flavor * texture

        if combo_score > best_combination_score:
            best_combination_score = combo_score

    return best_combination_score


def write_ingredient_dictionary(input_data):
    ingredient_dict = dict()
    lines = input_data.splitlines()

    for line in lines:
        split = line.split(' ')
        ingredient = split[0][:-1]
        ingredient_dict[ingredient] = dict()

        for index in range(1, len(split), 2):
            attribute = split[index]
            attribute_value = int(split[index + 1].replace(',', ''))
            ingredient_dict[ingredient][attribute] = attribute_value

    return ingredient_dict


data = get_data("Day15Q1 2015 Input.txt")

ingredient_dictionary = write_ingredient_dictionary(data)

print(ingredient_dictionary)

top_score = obtain_high_score(ingredient_dictionary)

print(top_score)  # 21367368

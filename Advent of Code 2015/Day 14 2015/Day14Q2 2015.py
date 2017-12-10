"""
Author:     Brian Mascitello
Date:       12/9/2017
Websites:   http://adventofcode.com/2015/day/14
Info:       --- Day 14: Reindeer Olympics ---
            --- Part Two ---
"""

import copy


def build_reindeer_dictionary(input_data):
    reindeer = dict()

    for line in input_data.splitlines():
        split = line.split()

        deer = split[0]
        pace = int(split[3])
        pace_duration = int(split[6])
        rest_duration = int(split[13])

        if deer not in reindeer.values():
            reindeer[deer] = [pace, pace_duration, rest_duration]

    return reindeer


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def maximum_dictionary_keys(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    maximum = max(values)
    key_list = list()
    for item in keys:
        if dictionary[item] == maximum:
            key_list.append(item)
    return key_list, maximum


def simulate_race(reindeer_info, race_duration):
    reindeer_race_info = copy.deepcopy(reindeer_info)

    reindeer_race_distances = dict.fromkeys(reindeer_info.keys())
    reindeer_race_points = dict.fromkeys(reindeer_info.keys())

    for key in reindeer_info:
        reindeer_race_distances[key] = 0
        reindeer_race_points[key] = 0

    race_time = race_duration
    while race_time:
        for key in reindeer_race_info:
            stepped = False
            while not stepped:
                if reindeer_race_info[key][1]:
                    reindeer_race_distances[key] += reindeer_race_info[key][0]
                    reindeer_race_info[key][1] -= 1
                    stepped = True
                elif reindeer_race_info[key][2]:
                    reindeer_race_info[key][2] -= 1
                    stepped = True
                else:
                    reindeer_race_info[key][1] = reindeer_info[key][1]
                    reindeer_race_info[key][2] = reindeer_info[key][2]
        race_time -= 1

        furthest_deers, furthest_distance = maximum_dictionary_keys(reindeer_race_distances)

        for deer in furthest_deers:
            reindeer_race_points[deer] += 1

    return reindeer_race_points


data = get_data('Day14Q1 2015 Input.txt')

reindeer_dictionary = build_reindeer_dictionary(data)

race_results = simulate_race(reindeer_dictionary, 2503)

fastest_deers, points = maximum_dictionary_keys(race_results)

print(fastest_deers[0], points)  # Blitzen 1256

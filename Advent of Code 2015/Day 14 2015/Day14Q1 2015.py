"""
Author:     Brian Mascitello
Date:       12/9/2017
Websites:   http://adventofcode.com/2015/day/14
Info:       --- Day 14: Reindeer Olympics ---
"""


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


def maximum_dictionary_tuple(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    maximum = max(values)
    return keys[values.index(maximum)], maximum


def simulate_race(reindeer_info, race_duration):
    reindeer_race_distances = dict.fromkeys(reindeer_info.keys())
    for key in reindeer_race_distances:
        pace = reindeer_info[key][0]
        pace_duration = reindeer_info[key][1]
        rest_duration = reindeer_info[key][2]

        distance_traveled = 0
        race_time = race_duration
        while race_time:
            if pace_duration:
                distance_traveled += pace
                pace_duration -= 1
                race_time -= 1
            elif rest_duration:
                rest_duration -= 1
                race_time -= 1
            else:
                pace_duration = reindeer_info[key][1]
                rest_duration = reindeer_info[key][2]

        reindeer_race_distances[key] = distance_traveled

    return reindeer_race_distances


data = get_data('Day14Q1 2015 Input.txt')

reindeer_dictionary = build_reindeer_dictionary(data)

race_results = simulate_race(reindeer_dictionary, 2503)

fastest_deer, max_distance = maximum_dictionary_tuple(race_results)

print(fastest_deer, max_distance)  # Vixen 2660

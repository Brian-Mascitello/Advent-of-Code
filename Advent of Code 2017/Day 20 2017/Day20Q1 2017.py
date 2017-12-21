"""
Author:     Brian Mascitello
Date:       12/20/2017
Websites:   http://adventofcode.com/2017/day/20
Info:       --- Day 20: Particle Swarm ---
"""

import re


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day20Q1 2017 Input.txt')
# data = get_data('Day19Q1 2017 Example.txt')

particle_list = list()
pattern = re.compile(r'\<(.*?)\>')
for line in data.splitlines():
    group = pattern.findall(line)
    position = list(map(int, group[0].split(',')))
    velocity = list(map(int, group[1].split(',')))
    acceleration = list(map(int, group[2].split(',')))
    particle_list.append([position, velocity, acceleration])

closest_particle_dictionary = dict()
measurements_to_make = 1000

while measurements_to_make:
    # Increase velocities by accelerations
    for particle in particle_list:
        for index in range(3):
            particle[1][index] += particle[2][index]

    # Increase positions by velocities
    for particle in particle_list:
        for index in range(3):
            particle[0][index] += particle[1][index]

    # Find nearest particle
    nearest_distance = abs(particle_list[0][0][0]) + abs(particle_list[0][0][1]) + abs(particle_list[0][0][2])
    nearest_particle = 0
    for index in range(1, len(particle_list)):
        distance = abs(particle_list[index][0][0]) + abs(particle_list[index][0][1]) + abs(particle_list[index][0][2])
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_particle = index

    if nearest_particle in closest_particle_dictionary.keys():
        closest_particle_dictionary[nearest_particle] += 1
    else:
        closest_particle_dictionary[nearest_particle] = 1

    measurements_to_make -= 1

max_key = None
for key in closest_particle_dictionary.keys():
    if max_key is None:
        max_key = key
    else:
        if closest_particle_dictionary[key] > closest_particle_dictionary[max_key]:
            max_key = key

print(max_key)  # 457

"""
Author:     Brian Mascitello
Date:       12/2/2017
Websites:   http://adventofcode.com/2015/day/9
Info:       --- Day 9: All in a Single Night ---
            --- Part Two ---
"""

import itertools


def build_graph(graph_raw_data):
    graph = dict()
    for line in graph_raw_data.splitlines():
        split_data = line.split()

        first_node = split_data[0]
        second_node = split_data[2]
        distance = int(split_data[4])  # This is the distance between first_node and second_node.

        if first_node not in graph:
            graph[first_node] = dict()
        graph[first_node][second_node] = distance

        if second_node not in graph:
            graph[second_node] = dict()
        graph[second_node][first_node] = distance
    return graph


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def get_locations(graph):
    location_list = list()
    for item in graph:
        if item not in location_list:
            location_list.append(item)
        for thing in graph[item]:
            if thing not in location_list:
                location_list.append(thing)
    return location_list


def find_longest(graph, location_list):
    furthest_distance = 0
    lengthiest_path = list()
    for perm in itertools.permutations(location_list):
        travel_distance = 0
        for index in range(0, len(perm) - 1):
            travel_distance += graph[perm[index]][perm[index + 1]]
        if travel_distance > furthest_distance:
            furthest_distance = travel_distance
            lengthiest_path = perm
    return furthest_distance, lengthiest_path


data = get_data('Day9Q1 2015 Input.txt')
route_graph = build_graph(data)
locations = get_locations(route_graph)
longest_distance, longest_path = find_longest(route_graph, locations)

print(longest_distance)  # 898
print(longest_path)  # ('Tristram', 'Faerun', 'Arbre', 'Straylight', 'AlphaCentauri', 'Norrath', 'Tambi', 'Snowdin')

"""
Author:     Brian Mascitello
Date:       11/22/2022
Websites:   https://adventofcode.com/2021/day/15#part2
Info:       --- Day 15: Chiton ---
            --- Part Two ---
Docs:       https://python-tcod.readthedocs.io/en/latest/
"""

import numpy as np
import pandas as pd
import re
import tcod


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    # Testing
    # data = get_data('Day15Q1 2021 Test Input.txt')
    # Actual
    data = get_data('Day15Q1 2021 Input.txt')

    # Get the dimensions of the array and form it from the input string in the data_array.
    dir_len = data.count('\n') + 1
    data_str = re.sub('', ' ', data)
    data_array = np.fromstring(string=data_str, dtype=int, sep=' ')
    data_array = data_array.reshape(dir_len, dir_len)

    # Now need to convert the data_array into the full five-times-as-large version described for part two.
    # Work the array from top to bottom first.
    tall_array = np.concatenate((data_array, data_array + 1, data_array + 2, data_array + 3, data_array + 4),
                                axis=0)
    tall_array = np.where(tall_array > 9, tall_array - 9, tall_array)
    full_array = np.concatenate((tall_array, tall_array + 1, tall_array + 2, tall_array + 3, tall_array + 4),
                                axis=1)
    full_array = np.where(full_array > 9, full_array - 9, full_array)

    # Set up the tcod graph for analysis.
    full_dir_len = dir_len * 5
    graph = tcod.path.CustomGraph((full_dir_len, full_dir_len))
    cost = np.copy(full_array)
    cardinal = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    graph.add_edges(edge_map=cardinal, cost=cost)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root((0, 0))
    pf.resolve()
    lowest_total_risk = pf.distance[full_dir_len - 1, full_dir_len - 1]
    print(pf.distance)
    print('lowest_total_risk:', lowest_total_risk)

    # Save Results
    df = pd.DataFrame(pf.distance)
    df.to_csv('pf distance3.csv')


if __name__ == '__main__':
    main()

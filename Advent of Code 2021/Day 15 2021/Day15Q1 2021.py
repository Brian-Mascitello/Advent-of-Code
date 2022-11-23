"""
Author:     Brian Mascitello
Date:       11/22/2022
Websites:   https://adventofcode.com/2021/day/15
Info:       --- Day 15: Chiton ---
Docs:       https://python-tcod.readthedocs.io/en/latest/
"""

# from itertools import permutations as perms
from sympy.utilities.iterables import multiset_permutations as mset_perms
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

    # Set up the tcod graph for analysis.
    graph = tcod.path.CustomGraph((dir_len, dir_len))
    cost = np.copy(data_array)

    # I was mistaken, Cardinal directions are okay!
    cardinal = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    # left_down_only = [
    #     [0, 0, 0],
    #     [0, 0, 1],
    #     [0, 1, 0],
    # ]

    graph.add_edges(edge_map=cardinal, cost=cost)
    pf = tcod.path.Pathfinder(graph)
    pf.add_root((0, 0))
    pf.resolve()
    lowest_total_risk = pf.distance[dir_len - 1, dir_len - 1]
    print(pf.distance)
    print('lowest_total_risk:', lowest_total_risk)

    # Save Results
    df = pd.DataFrame(pf.distance)
    df.to_csv('pf distance2.csv')

    """
    Test Case:
    [[ 0  1  7 10 17 22 23 30 34 36]
     [ 1  4 12 11 14 21 24 30 37 38]
     [ 3  4  7 13 18 19 20 23 25 33]
     [ 6 10 16 17 26 22 21 26 31 40]
     [13 14 20 20 24 23 28 27 28 29]
     [14 17 18 27 25 25 33 28 31 36]
     [15 18 23 32 34 26 28 32 33 34]
     [18 19 21 26 30 28 29 35 36 43]
     [19 21 30 29 30 31 37 40 38 39]
     [21 24 25 26 35 35 39 44 46 40]]
    """

    """
    # Create a string to iterate over to find all the possible move combinations as all_moves.
    move_length = dir_len - 1
    down_moves = 'D' * move_length
    right_moves = 'R' * move_length
    all_moves = down_moves + right_moves

    # Use the multiset_permutations of all_moves to try to find the optimal path.
    bad_perms = []
    lowest_total_risk = (len(all_moves) + 1) * 9
    # steps = 0
    for perm in mset_perms(all_moves):
        # Attempt to optimize calculation time by eliminating known bad paths.
        calculate_perm = True
        if len(bad_perms):
            for bad_perm in bad_perms:
                if bad_perm == perm[:len(bad_perm)]:
                    calculate_perm = False
                    break
        if calculate_perm:
            # steps += 1
            # Starting point is not counted, so current_risk = 0 not data_array[x][y].
            current_risk = 0
            move_count = 0
            x = 0
            y = 0
            for direction in perm:
                move_count += 1
                if direction == 'R':
                    x += 1
                else:
                    y += 1

                current_risk += data_array[x][y]

                if current_risk > lowest_total_risk:
                    # print(direction, move_count, perm[:move_count])
                    # bad_perms.append(perm[:move_count])  # Trying single list to see if steps are the same.
                    bad_perms = perm[:move_count]  # Steps larger, but comparisons much less it seems.
                    break

            if current_risk < lowest_total_risk:
                lowest_total_risk = current_risk
                print('New lower risk:', current_risk)

    # print(steps)
    """


if __name__ == '__main__':
    main()

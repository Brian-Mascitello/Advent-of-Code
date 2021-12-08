"""
Author:     Brian Mascitello
Date:       12/8/2021
Websites:   https://adventofcode.com/2021/day/6
Info:       --- Day 6: Lanternfish ---
            --- Part Two ---
Credit:     plan-x64
            https://github.com/plan-x64/advent-of-code-2021/blob/main/advent/day6.py
Note:       I was stuck on this one, kept filling my computer memory with NumPy arrays. Use a few math shortcuts other
            than remainder function to try to come up with a pure math solution, but attempts lead to approximations at
            best. Finally, got bored with this problem, which is not my goal for Advent of Code, and found plan-x64's
            solution to be the best explained.
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def grow_population(initial, days_to_grow):
    current = initial

    if days_to_grow == 0:
        return current

    for day in range(days_to_grow):
        due_index = day % 9
        due_count = current[due_index]

        current[(day + 7) % 9] += due_count
        current[(day + 9) % 9] += due_count
        current[due_index] = max(0, current[due_index] - due_count)

    return current


def initial_population(pop_input):
    population = [0] * 9
    for fish_age in pop_input:
        population[fish_age] += 1

    return population


def main():
    data = get_data('Day6Q1 2021 Input.txt')
    data_list_ints = list(map(int, data.split(',')))
    print("Part1: {}".format(sum(grow_population(initial_population(data_list_ints), 80))))
    print("Part2: {}".format(sum(grow_population(initial_population(data_list_ints), 256))))


main()

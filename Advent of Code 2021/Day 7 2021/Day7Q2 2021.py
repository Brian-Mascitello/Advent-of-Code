"""
Author:     Brian Mascitello
Date:       12/8/2021
Websites:   https://adventofcode.com/2021/day/7
Info:       --- Day 7: The Treachery of Whales ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day7Q1 2021 Input.txt')
    data = list(map(int, data.split(',')))

    # data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    fuel_cost_calculations = {}
    for position in range(min(data), max(data)+1):
        original_position = position

        sum_position = 0
        count = 1
        while position > 0:
            position -= 1
            sum_position += count
            count += 1

        fuel_cost_calculations[original_position] = sum_position

    print(fuel_cost_calculations)

    fuel_cost_simulation = {}
    for position in range(min(data), max(data)):
        fuel_cost = 0
        for crab in data:
            fuel_cost += fuel_cost_calculations[abs(crab - position)]
        fuel_cost_simulation[position] = fuel_cost

    print(fuel_cost_simulation)

    min_key = min(fuel_cost_simulation, key=fuel_cost_simulation.get)
    print(min_key, fuel_cost_simulation[min_key])

    max_key = max(fuel_cost_simulation, key=fuel_cost_simulation.get)
    print(max_key, fuel_cost_simulation[max_key])


main()

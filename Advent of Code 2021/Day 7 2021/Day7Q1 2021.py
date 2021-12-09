"""
Author:     Brian Mascitello
Date:       12/8/2021
Websites:   https://adventofcode.com/2021/day/7
Info:       --- Day 7: The Treachery of Whales ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day7Q1 2021 Input.txt')
    data = list(map(int, data.split(',')))

    fuel_cost_dict = {}
    for position in range(min(data), max(data)):
        fuel_cost = 0
        for crab in data:
            fuel_cost += abs(crab - position)
        fuel_cost_dict[position] = fuel_cost
        
    min_key = min(fuel_cost_dict, key=fuel_cost_dict.get)
    print(min_key, fuel_cost_dict[min_key])

    max_key = max(fuel_cost_dict, key=fuel_cost_dict.get)
    print(max_key, fuel_cost_dict[max_key])


main()

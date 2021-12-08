"""
Author:     Brian Mascitello
Date:       12/7/2021
Websites:   https://adventofcode.com/2021/day/5
Info:       --- Day 5: Hydrothermal Venture ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def get_range(first, second):
    if first >= second:
        temp_range = list(range(first, second - 1, -1))
    else:
        temp_range = list(range(first, second + 1))
    return temp_range


def main():
    data = get_data('Day5Q1 2021 Input.txt')
    line_ints = []
    for line in data.splitlines():
        line_commas = line.replace(' -> ', ',')
        line_ints.append(list(map(int, line_commas.split(','))))

    field_of_hydrothermal_vents = {}
    for coordinates in line_ints:
        x1, y1, x2, y2 = coordinates

        # Consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if (x, y) in field_of_hydrothermal_vents.keys():
                        field_of_hydrothermal_vents[(x, y)] = field_of_hydrothermal_vents[(x, y)] + 1
                    else:
                        field_of_hydrothermal_vents[(x, y)] = 1

        # you need to also consider diagonal lines
        elif abs(x1 - x2) == abs(y1 - y2):
            x_range = get_range(x1, x2)
            y_range = get_range(y1, y2)
            final_range = [(x_range[index], y_range[index]) for index in range(len(x_range))]
            for x, y in final_range:
                if (x, y) in field_of_hydrothermal_vents.keys():
                    field_of_hydrothermal_vents[(x, y)] = field_of_hydrothermal_vents[(x, y)] + 1
                else:
                    field_of_hydrothermal_vents[(x, y)] = 1

    lines_overlap = 0
    for key, value in field_of_hydrothermal_vents.items():
        if value > 1:
            lines_overlap = lines_overlap + 1

    print(lines_overlap)


main()

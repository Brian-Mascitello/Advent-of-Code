"""
Author:     Brian Mascitello
Date:       12/2/2022
Websites:   https://adventofcode.com/2022/day/1
Info:       --- Day 1: Calorie Counting ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day1Q1 2022 Input.txt')

    # calories_list_example = """1000
    # 2000
    # 3000
    #
    # 4000
    #
    # 5000
    # 6000
    #
    # 7000
    # 8000
    # 9000
    #
    # 10000
    # """

    elf_dict = {}
    elf_number = 1
    for line in data.splitlines():
        stripped_line = line.strip()
        if stripped_line == '':
            elf_number += 1
        else:
            if elf_number in elf_dict.keys():
                elf_dict[elf_number] += int(stripped_line)
            else:
                elf_dict[elf_number] = int(stripped_line)

    most_calories = max(elf_dict.values())
    print(f'The most calories an elf is carrying is {most_calories}.')


if __name__ == '__main__':
    main()

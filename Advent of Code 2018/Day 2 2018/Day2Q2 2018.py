"""
Author:     Brian Mascitello
Date:       12/2/2018
Websites:   https://adventofcode.com/2018/day/2
Info:       --- Day 2: Inventory Management System ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day2Q1 2018 Input.txt')

boxes = []
for line in data.splitlines():
    boxes.append(line)

found = False
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        if len(set(boxes[i]) - set(boxes[j])) <= 1:
            if len(set(boxes[j]) - set(boxes[i])) <= 1:
                count = 0
                last_discrepancy = 0

                for x in range(len(boxes[i])):
                    if boxes[i][x] != boxes[j][x]:
                        count += 1
                        last_discrepancy = x

                if count == 1:
                    print(boxes[i][0:last_discrepancy] + boxes[i][last_discrepancy + 1:])
                    found = True

        if found:
            break

    if found:
        break

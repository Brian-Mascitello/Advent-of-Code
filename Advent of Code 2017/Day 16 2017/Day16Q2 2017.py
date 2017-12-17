"""
Author:     Brian Mascitello
Date:       12/16/2017
Websites:   http://adventofcode.com/2017/day/16
Info:       --- Day 16: Permutation Promenade ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


data = get_data('Day16Q1 2017 Input.txt')
dance_moves = data.split(',')
program_list = [chr(x) for x in range(ord('a'), ord('q'))]

dance_result_list = [''.join(program_list)]
while True:
    for move in dance_moves:
        if move[0] == 's':
            # Spin
            spin_size = int(move[1:])
            program_list = program_list[-spin_size:] + program_list[:len(program_list) - spin_size]
        elif move[0] == 'x':
            # Exchange
            pos_1, pos_2 = map(int, move[1:].split('/'))
            program_list[pos_1], program_list[pos_2] = program_list[pos_2], program_list[pos_1]
        else:
            # Partner
            program_1, program_2 = move[1:].split('/')
            pos_1, pos_2 = program_list.index(program_1), program_list.index(program_2)
            program_list[pos_1], program_list[pos_2] = program_list[pos_2], program_list[pos_1]
    dance_results = ''.join(program_list)
    if dance_results not in dance_result_list:
        dance_result_list.append(dance_results)
    else:
        break

# print(dance_result_list)
# print(1000000000 % 60)  # 40

print(dance_result_list[40])  # fbmcgdnjakpioelh

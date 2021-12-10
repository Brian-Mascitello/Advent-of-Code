"""
Author:     Brian Mascitello
Date:       12/8/2021
Websites:   https://adventofcode.com/2021/day/8
Info:       --- Day 8: Seven Segment Search ---
            --- Part Two ---
"""


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    data = get_data('Day8Q1 2021 Input.txt')

    # data = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

    io_dict = {}
    for signal_pattern in data.splitlines():
        signal_input, signal_output = signal_pattern.split(' | ')
        io_dict[signal_input] = signal_output

    sum_output_values = 0
    for key, value in io_dict.items():
        signal_input = key.split()
        signal_input = [''.join(sorted(code)) for code in signal_input]
        signal_output = value.split()
        signal_output = [''.join(sorted(code)) for code in signal_output]

        code_to_number = {}
        number_to_code = {}
        for code in signal_input:
            if len(code) == 2:
                code_to_number[code] = 1
                number_to_code[1] = code
            elif len(code) == 3:
                code_to_number[code] = 7
                number_to_code[7] = code
            elif len(code) == 4:
                code_to_number[code] = 4
                number_to_code[4] = code
            elif len(code) == 7:
                code_to_number[code] = 8
                number_to_code[8] = code

        remaining_signals = list(set(signal_input) - set(list(code_to_number.keys())))

        for code in remaining_signals:
            one_letters = list(number_to_code[1])
            four_letters = list(number_to_code[4])
            if len(code) == 5:
                if all(letter in code for letter in one_letters):
                    code_to_number[code] = 3
                    number_to_code[3] = code
                elif sum(letter in code for letter in four_letters) == 2:
                    code_to_number[code] = 2
                    number_to_code[2] = code
                else:
                    code_to_number[code] = 5
                    number_to_code[5] = code
            else:
                if all(letter in code for letter in four_letters):
                    code_to_number[code] = 9
                    number_to_code[9] = code
                elif sum(letter in code for letter in one_letters) == 1:
                    code_to_number[code] = 6
                    number_to_code[6] = code
                else:
                    code_to_number[code] = 0
                    number_to_code[0] = code

        output_values = int(''.join([str(code_to_number[index]) for index in signal_output]))
        sum_output_values += output_values
        # print(code_to_number)
        # print(signal_output, output_values, sum_output_values)

    print(sum_output_values)


main()

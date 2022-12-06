"""
Author:     Brian Mascitello
Date:       12/5/2022
Websites:   https://adventofcode.com/2022/day/6
Info:       --- Day 6: Tuning Trouble ---
"""


def find_marker(input_str: str = '', marker_len: int = 4):
    if input_str:
        counter = 0
        marker_value = counter + marker_len
        temp_str = input_str[counter:marker_value]
        while len(set(temp_str)) != len(temp_str):
            counter += 1
            marker_value += 1
            temp_str = input_str[counter:marker_value]
        return marker_value
    else:
        return -1


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    return data_from_file


def main():
    data = get_data('Day6Q1 2022 Input.txt')
    result = find_marker(data)
    print(result)

    # ex0 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'  #: first marker after character 7
    # ex1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'  #: first marker after character 5
    # ex2 = 'nppdvjthqldpwncqszvftbrmjlhg'  #: first marker after character 6
    # ex3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'  #: first marker after character 10
    # ex4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'  #: first marker after character 11
    # examples = [ex0, ex1, ex2, ex3, ex4]
    # for example in examples:
    #     result = find_marker(example)
    #     print(f'{example}: first marker after character {result}')


if __name__ == '__main__':
    main()

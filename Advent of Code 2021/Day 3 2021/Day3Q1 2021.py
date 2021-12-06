"""
Author:     Brian Mascitello
Date:       12/5/2021
Websites:   https://adventofcode.com/2021/day/3
Info:       --- Day 3: Binary Diagnostic ---
"""

import pandas as pd


def main():
    df = pd.read_csv('Day3Q1 2021 Input.txt', names=['Original Binary'], dtype=str)
    df = df['Original Binary'].str.split('', expand=True)
    df = df.shift(periods=-1, axis='columns')
    df = df.drop(df.columns[-2:], axis=1)
    df = df.astype(int)

    gamma_rate = []
    epsilon_rate = []
    df_column_sum = df.sum(axis=0)
    for summation in df_column_sum:
        if summation > len(df.index) / 2:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')

    gamma_rate = int(''.join(gamma_rate), base=2)
    epsilon_rate = int(''.join(epsilon_rate), base=2)

    print(f'gamma_rate: {gamma_rate}')
    print(f'epsilon_rate: {epsilon_rate}')
    print(f'multiply: {gamma_rate * epsilon_rate}')


main()

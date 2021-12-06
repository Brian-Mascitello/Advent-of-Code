"""
Author:     Brian Mascitello
Date:       12/5/2021
Websites:   https://adventofcode.com/2021/day/3
Info:       --- Day 3: Binary Diagnostic ---
            --- Part Two ---
"""

import pandas as pd


def df_to_int(df):
    df = df.astype(str)
    df['String'] = df.apply(''.join, axis=1)
    return_str = df['String'].iloc[0]
    return_int = int(return_str, base=2)
    return return_int


def filter_df(df, least_common=False):
    variable = (1, 0)
    if least_common:
        variable = (0, 1)

    start = 0
    while len(df.index) >= 2:
        df_column_sum = df[start].sum(axis=0)
        if df_column_sum >= len(df.index) / 2:
            df = df[df[start] == variable[0]]
        else:
            df = df[df[start] == variable[1]]
        start = start + 1

    return df


def prep_df():
    df = pd.read_csv('Day3Q1 2021 Input.txt', names=['Original Binary'], dtype=str)
    df = df['Original Binary'].str.split('', expand=True)
    df = df.shift(periods=-1, axis='columns')
    df = df.drop(df.columns[-2:], axis=1)
    df = df.astype(int)
    return df


def main():
    df = prep_df()
    df = filter_df(df)
    oxygen_generator_rating = df_to_int(df)

    df2 = prep_df()
    df2 = filter_df(df2, least_common=True)
    co2_scrubber_rating = df_to_int(df2)

    print(f'oxygen_generator_rating: {oxygen_generator_rating}')
    print(f'co2_scrubber_rating: {co2_scrubber_rating}')
    print(f'multiply: {oxygen_generator_rating * co2_scrubber_rating}')


main()

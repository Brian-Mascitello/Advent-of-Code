"""
Author:     Brian Mascitello
Date:       12/5/2021
Websites:   https://adventofcode.com/2021/day/1
Info:       --- Day 1: Sonar Sweep ---
            --- Part Two ---
"""

import pandas as pd


def get_data(input_text):
    with open(input_text) as file:
        data_from_file = file.read()
    file.close()
    return data_from_file


def main():
    df = pd.read_csv('Day1Q1 2021 Input.txt', names=['Depth Measurement'])
    df['Rolling Sum'] = df['Depth Measurement'].rolling(3).sum()
    df['Depth Increased'] = 0

    last_depth = 0
    for index, row in df.iterrows():
        if pd.isnull(row['Rolling Sum']):
            df.loc[index, 'Depth Increased'] = '(N/A - no previous sum)'
        else:
            current_depth = row['Rolling Sum']

            if last_depth == 0:
                df.loc[index, 'Depth Increased'] = '(N/A - no previous sum)'
            else:
                if current_depth > last_depth:
                    df.loc[index, 'Depth Increased'] = '(increased)'
                elif current_depth < last_depth:
                    df.loc[index, 'Depth Increased'] = '(decreased)'
                else:
                    df.loc[index, 'Depth Increased'] = '(no change)'

            last_depth = current_depth

    print(df['Depth Increased'].value_counts())


main()

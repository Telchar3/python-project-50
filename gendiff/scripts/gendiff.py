#!/usr/bin/env python3
import argparse
import json
from gendiff.generate_diff2 import generate_diff

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')

    parser.add_argument('-f', '--format', type= str, help='set format of output')

    args = parser.parse_args()
    print(f'Comparing files: {args.first_file} and {args.second_file}')
    if args.format:
        print(f'Output format: {args.format}')

    file1_data = read_json(args.first_file)
    file2_data = read_json(args.second_file)

    diff = generate_diff(file1_data, file2_data)
    print(diff)




if __name__ == '__main__':
    main()


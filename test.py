#!/usr/bin/env python3

filename = input('Enter the file name: ')

with open(filename) as f:
    count = 0
    for line in f:
        count += 1
        print(line)
    print('Lines:', count)

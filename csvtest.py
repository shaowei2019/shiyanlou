#!/usr/bin/env python3
import csv
with open('test.csv') as f:
    data = list(csv.reader(f))

for i in data:
    print(i)



with open('test_w.csv','w') as f:
    csv.writer(f).writerows(data)

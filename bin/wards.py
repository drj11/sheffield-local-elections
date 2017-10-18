#!/usr/bin/env python3

import re
import sys

def as_wards(inp):
    import csv

    rows = csv.reader(inp)
    for row in rows:
        if re.search(r'\d', row[0]):
            yield [0] + row
            continue
        if re.match(r'Elected:|Electorate', row[0]):
            yield [0] + row
            continue
        yield [1] + row

def wards(inp):
    for row in as_wards(inp):
        if row[0]:
            print("\nWARD: {}\n".format(row[1]))
        else:
            print(row[1])
    

def main():
    with open("source/2016local.csv") as f:
        wards(f)


if __name__ == '__main__':
    sys.exit(main())

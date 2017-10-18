#!/usr/bin/env python3

import csv
import re
import sys

def as_wards(inp):
    rows = csv.reader(inp)
    ward = None
    for row in rows:
        if row[0].startswith('Elected'):
            yield [ward, "elected"] + row
            continue
        if row[0].startswith('Electorate'):
            yield [ward, "turnout"] + row
            continue
        if re.search(r'\d', row[0]):
            yield [ward, "candidate"] + candidate(row)
            continue
        ward = row[0]

def wards(inp):
    out = csv.writer(sys.stdout)
    for row in as_wards(inp):
        out.writerow(row)

def candidate(row):
    """Convert (1-element) list into more structured candidate
    list."""

    m = re.match(r'(.*),\s*([^,]*):\s*(.*)', row[0])
    cells = list(m.groups())
    cells[-1] = cells[-1].replace(',', '')
    return cells
    

def main():
    with open("source/2016local.csv") as f:
        wards(f)


if __name__ == '__main__':
    sys.exit(main())

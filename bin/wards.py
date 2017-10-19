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

def ward_poll(row):
    if row[1] == "candidate":
        return (row[0], row[1], int(row[4]))
    else:
        return (row[0], row[1])

def wards(inp, outf):
    out = csv.writer(outf)
    for row in sorted(as_wards(inp), key=ward_poll):
        out.writerow(row)

def candidate(row):
    """Convert (1-element) list into more structured candidate
    list."""

    m = re.match(r'(.*),\s*([^,]*):\s*(.*)', row[0])
    cells = list(m.groups())
    cells[-1] = cells[-1].replace(',', '')
    return cells
    

def main():
    with open("source/2016local.csv") as f,\
        open("out/2016local.csv", 'w') as out:
        wards(f, out)


if __name__ == '__main__':
    sys.exit(main())

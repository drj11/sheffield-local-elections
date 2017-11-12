#!/usr/bin/python3

import csv
import re
import sys

def turnout(rows):
    out = csv.writer(open('out/2016turnout.csv', 'w'))
    for row in rows:
        if 'turnout' != row[1]:
            continue
        t = row[2]
        m = re.match(r'.*Electorate:\s+([\d,]+).*Turnout:\s+([.\d]+)', t)
        assert m
        electorate, turnout = m.groups()
        electorate = int(electorate.replace(',', ''))
        turnout = float(turnout)
        out.writerow([row[0], electorate, turnout])

def main(argv=None):
    if argv is None:
        argv = sys.argv

    with open("out/2016local.csv") as fd:
        turnout(csv.reader(fd))

if __name__ == '__main__':
    main()

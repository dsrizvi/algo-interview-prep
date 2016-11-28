#!/bin/python3

import sys
from operator import sub


def calculate_fine(return_date, due_date):
    DAY = 0
    MONTH = 1
    YEAR = 2
    DAILY_FINE = 15
    MONTHLY_FINE = 500
    YEAR_FINE = 10000

    diff = list(map(sub, return_date, due_date))

    if diff[DAY] > 0 and diff[MONTH] == 0 and diff[YEAR] == 0:
        return diff[DAY]*DAILY_FINE
    if diff[MONTH] > 0 and diff[YEAR] == 0:
        return diff[MONTH]*MONTHLY_FINE
    if diff[YEAR] > 0:
        return YEAR_FINE

    return 0

def main():
    d1,m1,y1 = input().strip().split(' ')
    d1,m1,y1 = [int(d1),int(m1),int(y1)]
    d2,m2,y2 = input().strip().split(' ')
    d2,m2,y2 = [int(d2),int(m2),int(y2)]

    print(calculate_fine([d1,m1,y1], [d2, m2, y2]))

if __name__ == '__main__':
    main()
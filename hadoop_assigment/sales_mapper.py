#!/usr/bin/env python
"""sales_mapper.py"""
import sys

skip_first_row = True

for line in sys.stdin:

    if skip_first_row:
        skip_first_row = False
        continue

    line = line.strip()
    words = line.split(',')

    for indx,word in enumerate(words):
        if indx == 4:
            order_priority = word
        elif indx == 13:
            total_profit = word

    print('%s\t%s' % (order_priority,total_profit))



#!/usr/bin/env python
"""sales_reducer.py"""
from operator import itemgetter
import sys

cur_key = None
cur_value = 0.0

for line in sys.stdin:

    line = line.strip()

    key, value = line.split('\t', 1)

    try:
        value = float(value)
    except ValueError:
        print("cannot conver this value!")
        continue

    if cur_key == key:
        cur_value += value
    else:
        if cur_key:
            print('%s\t%s' % (cur_key,cur_value))
        cur_key = key
        cur_value = value





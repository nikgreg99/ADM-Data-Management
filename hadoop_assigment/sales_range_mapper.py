#!/usr/bin/env python
"""sales_range_mapper.py"""

import sys
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

START_DATE = datetime(2012, 1, 1)
END_DATE = datetime(2014, 12, 31)

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
        elif indx == 5:
            order_date =  word
            try:
                order_date = datetime.strptime(order_date, DATE_FORMAT)
            except:
                order_date = None
                print(word)
        elif indx == 13:
            total_profit = word

    if  order_date and order_date >= START_DATE and order_date <= END_DATE:
        print('%s\t%s' % (order_priority,total_profit))

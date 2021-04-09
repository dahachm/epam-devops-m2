# Task 8*
#
# Do all the same AWK tasks from AWK Homework 3-4 using Python.
#
# 2. Show number of requests per month for ip 193.106.31.130 
# (for example: Sep 2016 - 100500 reqs, Oct 2016 - 0 reqs, Nov 2016 - 2 reqs...)
#
# Pleas start this script with path/to/access.log 
# as the first argument

import sys

filepath = sys.argv[1]
req_per_month = {}

with open(filepath,'r') as f:
    for line in f.readlines():
        if line.split(' ')[0] == '193.106.31.130':
            date = line.split(' ')[3][4:12]
            try:
                req_per_month[date] += 1
            except KeyError:
                req_per_month[date] = 1      

for (key, value) in req_per_month.items():
    print('{} - {} reqs'.format(key, value))
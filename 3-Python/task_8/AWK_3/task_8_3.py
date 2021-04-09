# Task 8*
#
# Do all the same AWK tasks from AWK Homework 3-4 using Python.
#
# Show total amount of data which server has provided for each 
# unique ip (i.e. 100500 bytes for 1.2.3.4; 9001 bytes for 5.4.3.2 and so on)
#
# Pleas start this script with path/to/access.log 
# as the first argument

import sys

filepath = sys.argv[1]
data_provided = {}
num = 1
with open(filepath,'r') as f:
    for line in f.readlines():
        ip = line.split(' ')[0]
        try:
            data = int(line.split(' ')[9])
            try:
                data_provided[ip] += data
            except KeyError:
                data_provided[ip] = data
        except:
             continue    

for (key, value) in data_provided.items():
    print('%10d bytes for %s' % (value, key))
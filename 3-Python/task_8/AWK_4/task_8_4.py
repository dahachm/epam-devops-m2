# Task 8*
#
# Do all the same AWK tasks from AWK Homework 3-4 using Python.
#
# 4. Show list of unique ips, who made more then 50 requests to the 
# same url within 10 minutes (for example too many requests to "/").
#
# Pleas start this script with path/to/access.log 
# as the first argument

import sys

def find_timerange(time):
    if time[1] == '3' and time[3] == '5':
        time = time + '0 - 00:00'
    elif time[3] == '5':
        time = time + '0 - ' + str(int(time[:2])+1) + ':00'
    else:
        time = time + '0 - ' + time[:2] + ':' + str(int(time[-1])+1) + '0'  
    return time


filepath = sys.argv[1]
requests_stat = {}

with open(filepath,'r') as f:
    for line in f.readlines():
        ip   = line.split(' ')[0]
        url  = line.split('"')[3]
        time = line.split(' ')[3][1:17]
        try:
            requests_stat[(ip, url, time)] += 1
        except KeyError:
            requests_stat[(ip, url, time)] = 1

annoying_list = set()

print('    DATE    	     TIME     	REQ	     IP     	          URL')
for (key, value) in requests_stat.items():
    if value > 50:
        annoying_list.add(key[0])

        date = key[2][:11]
        time = find_timerange(key[2][12:16])

        print('%s    %s    %3d    %s    %s' % (date, time, value, key[0], key[1]))


print('\nList of unique IPs, who made more then 50 requests to the same url within 10 minutes:')
for ip in annoying_list:
    print(ip)       

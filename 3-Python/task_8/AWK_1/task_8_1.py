# Task 8*
#
# Do all the same AWK tasks from AWK Homework 3-4 using Python.
#
# 1. What is the most frequent browser (user agent) in given access.log?
#
#
# Pleas start this script with path/to/access.log 
# as the first argument

import sys

filepath = sys.argv[1]
agents = {}

with open(filepath,'r') as f:
    for line in f.readlines():
        useragent = line.split('"')[5]
        try:
            agents[useragent] += 1
        except KeyError:
            agents[useragent] = 1    

sorted_agents = sorted(((value, key) for (key,value) in agents.items()), reverse=True)

print('The most frequently used user agent is "{}" ({} times).'.format(sorted_agents[0][1], sorted_agents[0][0]))
       
        
    
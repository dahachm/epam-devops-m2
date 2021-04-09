# Task 7

# Develop a procedure that will have a size argument and print a table where num of columns and rows 
# will be of this size. Cells of table should contain numbers from 1 to n ** 2 placed in a spiral fashion. 
# Spiral should start from top left cell and has a clockwise direction (see the example below).
# 
# example:
# 
# >>> print_spiral(5)
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

def print_spiral(n):

    val = 0
    ans = [[0] * n for i in range(n)]

    for k in range(0, n//2 + n%2):
        i = 0 + k
        for j in range(0+k, n-k):
            val += 1
            ans[i][j] = val

        j = n - k - 1
        for i in range(1+k, n-k):
            val += 1
            ans[i][j] = val
        
        i = n - k - 1
        for j in list(range(n-k-2, 0+k-1, -1)):
            val += 1
            ans[i][j] = val
        
        j = 0 + k
        for i in list(range(n-k-2, 1+k-1, -1)):
            val += 1
            ans[i][j] = val
                       

    for i in range(0, n):
        for j in range(0, n):
            print ('%6d ' % ans[i][j], end='')
        print()    

    

# To use this module before calling python call following command in /bin/bash:
# ```
# export PYTHONPATH=/path/to/task_7.py
# ```
# 
# Then in python3 (or in your python script):
# >>> from task_7 import sprint_spiral
# >>> print_spiral(7)
#     
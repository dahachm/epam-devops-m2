# Task 6

# Create a function that will take a string as an argument and 
# return a dictionary where keys are symbols from the string and 
# values are the count of inclusion of that symbol.

def numberIt(_str):
    mydict = {i:_str.count(i) for i in _str}
    print(mydict)
    return mydict


print('\n    --- TEST #1 ---')
test_1 = 'aaaaa'
numberIt(test_1)

print('\n    --- TEST #2 ---')
test_2 = 'aaabbaaa'
numberIt(test_2)

# numberIt() uses dictionary comprehension to make a dictionary 
# with items, where *key* is a symbol from the given string
# and  *value* is - number of inclusion this of this symbol 
# in the given string 


